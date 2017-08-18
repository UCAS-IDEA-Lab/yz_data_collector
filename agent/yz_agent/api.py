# -*- coding: utf-8 -*-

import web
import json
import logging
import random

from agent import exp_agent, exp_state_agent

LOG = logging.getLogger()

urls = (
    '/api/speedup', 'Speedup',
    '/api/slowdown', 'Slowdown',
    '/api/start', 'Start',
    '/api/stop', 'Stop',
    '/api/strategy', 'Strategy',
    '/api/ping', 'Ping',
    '/api/report', 'Report'
)

class Speedup:
    def POST(self):
        pass

class Slowdown:
    def POST(self):
        pass

class Start:
    def POST(self):
        pass

class Stop:
    def POST(self):
        pass

class Strategy:
    def POST(self):
        pass

class Ping:
    def GET(self):
        return '{"volume":%.2f}' % (exp_agent.volume+exp_state_agent.volume)

class Report:
    def POST(self):
        pass

def run(*args, **kwargs):
    app = web.application(urls, globals(), *args, **kwargs)
    app.run()

if __name__ == '__main__':
    run()

