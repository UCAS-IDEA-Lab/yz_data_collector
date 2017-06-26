# -*- coding: utf-8 -*-

from common import MyThread, calc_percent
from settings import batch, data_path
from remote_call import upload

import time
import logging
import re
import json

LOG = logging.getLogger()

# TODO: subclass defined based on data_type
class Agent(MyThread):
    def __init__(self, no, data_type):
        """
        _file_name: data file's name, e.g. "2017/04/04/${data_type}/044"
        _offset: offset inside the data file
        """
        super(Agent, self).__init__('Agent', no)
        self._delay = 0
        self._rec_fd = open('/var/lib/yz_agent/offset.rec', 'rb+')
        _, self._file_name, self._offset = re.split('\s+', self._rec_fd.read())
        self._offset = int(self._offset)
        self._data_fd = open('%s/%s' % (data_path, self._file_name))
    
    def __del__(self):
        self._rec_fd.close()
        self._data_fd.close()

    def _work(self):
        self._scratch()
        time.sleep(self._delay)

    def _scratch(self):
        """
        Get data from data file.
        """
        for _ in xrange(batch):
            line = self._data_fd.readline()
            # TODO: handle end of file
            ret = upload(self._transform(line))

    # TODO: Based on data_type
    @abc.abstractmathod
    def _transform(self, raw_str, data_type):
        """
        Transform data to message type, and serialize using protobuf.
        """
        return {
            'id': '',
            'data': json.loads(raw_str),
            'type': data_type,
            'usage': ''
        }

    def _update_record(self, file_name, index):
        self._rec_fd.seek(0)
        self._rec_fd.write('%32s%16d' % (file_name, index))

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

