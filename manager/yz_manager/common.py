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
            try:
                self._cond.acquire()
                if self._pause:
                    self._cond.wait()
                self._cond.release()
                self._work()
            except Exception, e:
                LOG.error(e)

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

def do_get(url, **kwarg):
    try:
        re = requests.get(url, timeout=2, **kwarg)
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

def do_post(url, data=None, **kwarg):
    try:
        re = requests.post(url, data=data, timeout=2, **kwarg)
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

# Date calc
Small_Month = [4, 6, 9, 11]
Big_Month = [1, 3, 5, 7, 8, 10, 12]

def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def next_day(year, month, day):
    """
    Get the date of next day
    :param year: the year of today, e.g. '2017'
    :param month: the month of today, e.g. '12'
    :param day: the day of today, e.g. '12'
    :return: '2017', '12', '13'
    """
    year = int(year)
    month = int(month)
    day = int(day)
    if month in Small_Month and day >= 30 \
            or month in Big_Month and day >= 31 \
            or month == 2 and is_leap_year(year) and day >= 29 \
            or month == 2 and not is_leap_year(year) and day >= 28:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    else:
        day += 1

    return str(year), '%02d' % month, '%02d' % day

