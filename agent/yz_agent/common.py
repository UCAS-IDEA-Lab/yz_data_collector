# -*- coding: utf-8 -*-

# Thread model
from threading import Thread, Condition
import logging
import abc

LOG = logging.getLogger()

class MyThread(Thread):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, tid):
        super(MyThread, self).__init__()
        self.threadID = tid
        self.name = name
        self._cond = Condition()
        self._exit = False
        self._pause = False

    def run(self):
        LOG.info("%s-%d started" % (self.name, self.threadID))
        while not self._exit:
            self._cond.acquire()
            if self._pause:
                self._cond.wait()
            self._cond.release()
            self._work()

    @abc.abstractmethod
    def _work(self):
        """
        Should be implemented by subclasses.
        """
    
    @property
    def cond(self):
        return self._cond

    @property
    def toExit(self):
        return self._exit

    @property
    def toPause(self):
        return self._pause

    def stop(self):
        self._exit = True
        LOG.info("%s-%d stoped" % (self.name, self.threadID))

    def pause(self):
        self._pause = True
        LOG.info("%s-%d paused" % (self.name, self.threadID))

    def resume(self):
        self._pause = False
        self._cond.acquire()
        self._cond.notify()
        self._cond.release()
        LOG.info("%s-%d resumed" % (self.name, self.threadID))

# HTTP client
import requests
import json

def do_get(url):
    try:
        re = requests.get(url, timeout=2)
        ret = {
            'success': True,
            'status': re.status_code,
            'data': re.json()
        }
        LOG.info("GET %s" % url)
    except ValueError, e:
        ret = {
            'success': True,
            'status': re.status_code,
            'data': re.text
        }
        LOG.info("GET %s: %s" % (url, e))
    except Exception, e:
        ret = {
            'success': False,
            'data': e
        }
        LOG.error("GET %s: %s" % (url, e))
    return ret

def do_post(url, data):
    try:
        re = requests.post(url, data=json.dumps(data), timeout=2)
        ret = {
            'success': True,
            'status': re.status_code
        }
        LOG.info("POST %s" % url)
    except Exception, e:
        ret = {
            'success': False,
            'data': e
        }
        LOG.error("POST %s: %s" % (url, e))
    return ret

