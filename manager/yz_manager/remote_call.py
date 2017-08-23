# -*- coding: utf-8 -*-

from common import do_get, do_post
from settings import agent_api_port

def agent_start(addr):
    url = "http://%s:%s/api/action/start" % (addr, agent_api_port)
    return do_post(url)

def agent_stop(addr):
    url = "http://%s:%s/api/action/stop" % (addr, agent_api_port)
    return do_post(url)

def agent_speedup(addr):
    url = "http://%s:%s/api/action/speedup" % (addr, agent_api_port)
    return do_post(url)

def agent_slowdown(addr):
    url = "http://%s:%s/api/action/slowdown" % (addr, agent_api_port)
    return do_post(url)

