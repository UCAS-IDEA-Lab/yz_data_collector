# -*- coding: utf-8 -*-

from common import MyThread, next_day
from settings import batch, data_path, log_start_date, wait_for_new_data, msg_batch
from remote_call import upload
from serialize.msg_pb2 import MsgBody as PbMsgBody
from serialize.json_msg import MsgBody as JsonMsgBody

import time
import logging
import re
import json
from os import path
from google.protobuf import json_format as jf

LOG = logging.getLogger()

class Agent(MyThread):

    serialize_class = JsonMsgBody
    data_type = None
    data_type_code = None

    def __init__(self, name, no):
        """
        _file_name: data file's name, e.g. "2017/04/04/${data_type}/00044"
        _offset: offset inside the data file
        _volume: volume of this agent
        """
        LOG.info('Initialize Agent %s-%d' % (name, no))
        super(Agent, self).__init__(name, no)

        self._rec_fd, self._data_file_name, self._offset = self._rec_init()
        self._data_fd = self._data_file_init()
        self._delay = 0
        self._volume = 0
        self._timestramp = time.time()
    
    def __del__(self):
        LOG.info('Release Agent %s-%d' % (self.name, self.threadID))
        self._rec_fd.close()
        self._data_fd.close()

    @property
    def interval(self):
        return self._delay

    @property
    def volume(self):
        """
        :return: KB/s
        """
        return self._volume

    def _rec_init(self):
        """
        1. Get start from last record;
        2. If not, get start from today.
        """

        def _new_record(tc):
            start_date = log_start_date
            if start_date is None:
                start_date = time.strftime('%Y/%m/%d', time.localtime())
            name = '%s/%s/00000' % (start_date, tc)
            offset = 0
            return name, offset

        rec_file_name = '/var/lib/yz_agent/offset_%s.rec' % self.data_type_code
        try:
            rec_fd = open(rec_file_name, 'rb+')
            _, data_file_name, data_file_offset = re.split('\s+', rec_fd.read())
        except IOError, e:
            LOG.warning(e)
            rec_fd = open(rec_file_name, 'wb+')
            data_file_name, data_file_offset = _new_record(self.data_type_code)
        except ValueError, e:
            LOG.error(e)
            LOG.error('Empty in record file')
            data_file_name, data_file_offset = _new_record(self.data_type_code)

        return rec_fd, data_file_name, int(data_file_offset)

    def _data_file_init(self):
        while True:
            try:
                data_file = '%s/%s' % (data_path, self._data_file_name)
                data_fd = open(data_file, 'rb')
                LOG.info('Loading data from %s...' % data_file)
                for _ in xrange(self._offset):
                    data_fd.readline()
                self._id_prefix = self._data_file_name.replace('/', '')

                return data_fd
            except IOError, e:
                LOG.error(e)
                time.sleep(wait_for_new_data)

    def _next_file(self):

        def _new_data_file(next_file):
            data_file = '%s/%s' % (data_path, self._data_file_name)
            LOG.debug('Next file: %s' % data_file)
            if path.exists(data_file):
                self._data_file_name = next_file
                self._offset = 0
                self._data_fd = self._data_file_init()
                return True
            return False

        info = self._data_file_name.split('/')
        while True:
            info[4] = '%05d' % (int(info[4]) + 1)
            if _new_data_file('/'.join(info)):
                LOG.debug('Same day, next file')
                return
            
            info[0], info[1], info[2] = next_day(info[0], info[1], info[2])
            info[4] = '00000'
            if _new_data_file('/'.join(info)):
                LOG.debug('Next day, next file')
                return

            # No new data file
            time.sleep(wait_for_new_data)

    def _update_record(self):
        self._rec_fd.seek(0)
        self._rec_fd.write('%32s%16d' % (self._data_file_name, self._offset))
        self._rec_fd.flush()

    def _work(self):
        self._scratch()
        time.sleep(self._delay)

    def _scratch(self):
        """
        Get data from data file.
        """
        def __calc_volume(ts, v):
            ts_now = time.time()
            return ts_now, round(float(v)/(ts_now-ts)/1024, 2)

        _ = 0
        while _ < batch:
            send_data_size = 0
            lines = self._data_fd.readlines(msg_batch)
            msg_num = len(lines)
            if msg_num == 0:
                LOG.debug('No new data')
                time.sleep(wait_for_new_data)
            else:
                file_end = False
                if lines[-1].startswith('END'):
                    lines.pop()
                    file_end = True
                ret = upload(map(self._transform, lines, range(len(lines))[::-1]), self.data_type)
                # LOG.debug('Message send, ret: %s' % ret)
                if ret['success']:
                    _ += msg_num
                    self._offset += msg_num
                    send_data_size = ret['data_size']
                    # LOG.debug('Message send, offset: %5d' % self._offset)
                    if file_end:
                        LOG.debug('Handle the end of a data file')
                        self._next_file()
                else:
                    LOG.debug('Send failed, seek to last line')
                    size = reduce(lambda x, y: x+y, [len(line) for line in lines])
                    self._data_fd.seek(-size, 1)

            self._timestramp, self._volume = __calc_volume(self._timestramp, send_data_size)
        # Make sure at most a batch size of data re-transmitted
        self._update_record()
        LOG.debug('%d message send' % _)

    def _transform(self, raw_str, sub_off):
        """
        Transform data to message type, and serialize using protobuf.
        """
        try:
            pb = self.serialize_class()
            pb.id = '%s#%d' % (self._id_prefix, self._offset-sub_off)
            pb.data = raw_str
            pb.type = self.data_type
            pb.usage = 'upload'
            return pb.SerializeToString()
        except ValueError, e:
            LOG.error(e)
            return None

    def speedup(self):
        """
        Reduce self._delay, if it is bigger than 0
        """
        pass

    def slowdown(self):
        """
        Accumulate self._delay, if it is smaller than 10
        """
        pass

# 
# 'ErrorHandle': '00',
# 'ExpressContract': '01',
# 'ExpressContractState': '02'
# 
class ExpAgent(Agent):
    serialize_class = PbMsgBody
    data_type = 'ExpressContract'
    data_type_code = '01'

class ExpStateAgent(Agent):
    serialize_class = PbMsgBody
    data_type = 'ExpressContractState'
    data_type_code = '02'

class ErrorHandleAgent(Agent):
    """
    Handle Message Reupload
    """
    serialize_class = PbMsgBody
    data_type = 'ErrorHandle'
    data_type_code = '00'

    def _rec_init(self):
        pass

exp_agent = ExpAgent('ExpAgent', 1)
exp_state_agent = ExpStateAgent('ExpStateAgent', 1)

