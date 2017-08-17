# -*- coding: utf-8 -*-

from common import MyThread
from agent_views import agent_view

import time
import abc
import logging

LOG = logging.getLogger()

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
        LOG.debug("Ping agents")
        agent_view.ping_agents()

