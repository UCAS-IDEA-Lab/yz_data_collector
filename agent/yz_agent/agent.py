# -*- coding: utf-8 -*-

from common import MyThread, calc_percent

import time
import logging

LOG = logging.getLogger()

class Agent(MyThread):
    def __init__(self, no):
        super(Agent, self).__init__('Agent', no)
        self._delay = 0
        self._rec_fd = open('/var/lib/yz_agent/offset.rec', 'rw')
    
    def __del__(self):
        self._rec_fd.close()

    def _work(self):
        time.sleep(self._delay)

    def _scratch(self):
        """
        Get data from data file.
        """
        pass

    def _transform(self):
        """
        Transform data to message type, and serialize using protobuf.
        """
        pass

    def _report(self):
        """
        Report to collector server, and update offsets if success.
        """
        pass

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

