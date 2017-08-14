# -*- coding: utf-8 -*-

from common import MyThread

import time
import abc

class Routine(MyThread):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, rid, interval):
        super(Routine, self).__init__(name, rid)
        self._interval = interval

    def _work(self):
        self._rouine_job()
        time.sleep(self._interval)

    @abc.abstractmethod
    def _rouine_job(self):
        """
        Routine job implemented by subclasses.
        """

class PingRoutine(Routine):
    
    def _rouine_job(self):
        # TODO: use co-routine to ping multi-agents
        print "Ping agent"

