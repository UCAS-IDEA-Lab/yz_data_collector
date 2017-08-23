# -*- coding: utf-8 -*-

import requests
import logging

LOG = logging.getLogger(__name__)

# Agent
def list_agents(host, port):
    url = "http://%s:%s/api/agents" % (host, port)
    return __http_client('get', url)

def show_agent(host, port, agent_id):
    url = "http://%s:%s/api/agent/%s" % (host, port, agent_id)
    return __http_client('get', url)

def start_agent(host, port, agent_id):
    url = "http://%s:%s/api/agent/%s/start" % (host, port, agent_id)
    return __http_client('post', url)

def stop_agent(host, port, agent_id):
    url = "http://%s:%s/api/agent/%s/stop" % (host, port, agent_id)
    return __http_client('post', url)

def speedup_agent(host, port, agent_id):
    url = "http://%s:%s/api/agent/%s/speedup" % (host, port, agent_id)
    return __http_client('post', url)

def slowdown_agent(host, port, agent_id):
    url = "http://%s:%s/api/agent/%s/slowdown" % (host, port, agent_id)
    return __http_client('post', url)

# Handler
def list_handlers(host, port):
    url = "http://%s:%s/api/handlers" % (host, port)
    return __http_client('get', url)

def show_handler(host, port, handler_id):
    url = "http://%s:%s/api/handler/%s" % (host, port, handler_id)
    return __http_client('get', url)

def __http_client(method, url, data=None):
    def __get(url, data):
        try:
            return requests.get(url, timeout=2)
        except Exception, e:
            LOG.error(e)
            return None

    def __post(url, data):
        try:
            return requests.post(url, data=data, timeout=2)
        except Exception, e:
            LOG.error(e)
            return None

    def __delete(url, data):
        try:
            return requests.delete(url, timeout=2)
        except Exception, e:
            LOG.error(e)
            return None

    methods = {
        'get': __get,
        'post': __post,
        'delete': __delete
    }

    return methods[method](url, data)

