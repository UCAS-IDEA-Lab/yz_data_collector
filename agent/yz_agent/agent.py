# -*- coding: utf-8 -*-

from common import MyThread, next_day
from settings import batch, data_path, log_start_date, wait_for_new_data
from remote_call import upload
from serialize.exp_pb2 import ExpMsg
from serialize.exp_state_pb2 import ExpStateMsg

import time
import logging
import re
import json
from os import path
from google.protobuf import json_format as jf

LOG = logging.getLogger()

DATA_TYPE = {
    'ErrorHandle': '00',
    'ExpressContract': '01',
    'ExpressContractState': '02'
}

class Agent(MyThread):

    serialize_class = None
    data_type = None

    def __init__(self, name, no):
        """
        _file_name: data file's name, e.g. "2017/04/04/${data_type}/00044"
        _offset: offset inside the data file
        """
        LOG.info('Initialize Agent %s-%d' % (name, no))
        super(Agent, self).__init__(name, no)

        self._rec_fd, self._data_file_name, self._offset = self._rec_init(self.data_type)
        self._data_fd = self._data_file_init()
        self._delay = 0
    
    def __del__(self):
        LOG.info('Release Agent %s-%d' % (self.name, self.threadID))
        self._rec_fd.close()
        self._data_fd.close()

    @property
    def interval(self):
        return self._delay

    def _rec_init(self, data_type):
        """
        1. Get start from last record;
        2. If not, get start from today.
        """

        def _new_record(t):
            start_date = log_start_date
            if start_date is None:
                start_date = time.strftime('%Y/%m/%d', time.localtime())
            name = '%s/%s/00000' % (start_date, DATA_TYPE[t])
            offset = 0
            return name, offset

        rec_file_name = '/var/lib/yz_agent/offset_%s.rec' % DATA_TYPE[data_type]
        try:
            rec_fd = open(rec_file_name, 'rb+')
            _, data_file_name, data_file_offset = re.split('\s+', rec_fd.read())
        except IOError, e:
            LOG.warning(e)
            rec_fd = open(rec_file_name, 'wb+')
            data_file_name, data_file_offset = _new_record(data_type)
        except ValueError, e:
            LOG.error(e)
            LOG.error('Empty in record file')
            data_file_name, data_file_offset = _new_record(data_type)

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
        _ = 0
        while _ < batch:
            line = self._data_fd.readline()
            if line.startswith('END'):
                LOG.debug('Handle the end of a data file')
                self._next_file()
                continue
            elif line == '':
                LOG.debug('No new data')
                time.sleep(wait_for_new_data)
                continue
            else:
                ret = upload(self._transform(line), self.data_type)
                # LOG.debug('Message send, ret: %s' % ret)
                if ret['success']:
                    _ += 1
                    self._offset += 1
                    # LOG.debug('Message send, offset: %5d' % self._offset)
                else:
                    LOG.debug('Send failed, seek to last line')
                    self._data_fd.seek(-len(line), 1)
        # Make sure at most a batch size of data re-transmitted
        self._update_record()
        LOG.debug('%d message send' % batch)

    def _transform(self, raw_str):
        """
        Transform data to message type, and serialize using protobuf.
        """
        try:
            # TODO: use simple message format
            msg = json.dumps({
                'id': '%s#%d' % (self._id_prefix, self._offset),
                'data': json.loads(raw_str),
                'type': self.data_type,
                'usage': 'upload'
            })
            if self.serialize_class is None:
                return msg
            else:
                pb = self.serialize_class()
                pb = jf.Parse(msg, pb)
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

class ExpAgent(Agent):
    serialize_class = ExpMsg
    data_type = 'ExpressContract'

class ExpStateAgent(Agent):
    serialize_class = ExpStateMsg
    data_type = 'ExpressContractState'

class ErrorHandleAgent(Agent):
    """
    Handle Message Reupload
    """
    def __init__(self, name, no):
        super(ErrorHandleAgent, name, no, 'ErrorHandle')

    def _rec_init(self):
        pass

