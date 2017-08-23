# -*- coding: utf-8 -*-

import web
import json
import logging
import random

from agent import exp_agent, exp_state_agent

LOG = logging.getLogger(__name__)

urls = (
    '/api/action/(\w+)', 'Action',
    '/api/strategy', 'Strategy',
    '/api/ping', 'Ping',
    '/api/report', 'Report'
)

def _start():
    try:
        exp_agent.resume()
        exp_state_agent.resume()
    except Exception, e:
        LOG.error(e)
        return web.internalerror()
    
    return web.ok()

def _stop():
    try:
        exp_agent.pause()
        exp_state_agent.pause()
    except Exception, e:
        LOG.error(e)
        return web.internalerror()
    
    return web.ok()

def _speedup():
    pass

def _slowdown():
    pass

class Action:
    __handlers__ = {
        'start': _start,
        'stop': _stop,
        'speedup': _speedup,
        'slowdown': _slowdown
    }

    def POST(self, action):
        return self.__handlers__[action]()

class Strategy:
    def POST(self):
        pass

class Ping:
    def GET(self):
        return json.dumps({
            'volume': exp_agent.volume+exp_state_agent.volume,
            'status': 2 if exp_agent.toPause or exp_state_agent.toPause else 1
        })
        # return '{"volume":%.2f}' % (exp_agent.volume+exp_state_agent.volume)

class Report:
    def POST(self):
        pass

def run(*args, **kwargs):
    app = web.application(urls, globals(), *args, **kwargs)
    app.run()

if __name__ == '__main__':
    run()

