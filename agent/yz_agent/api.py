# -*- coding: utf-8 -*-

import web
import json
import logging

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
        pass

class Report:
    def POST(self):
        pass

def run(*args, **kwargs):
    app = web.application(urls, globals(), *args, **kwargs)
    app.run()

if __name__ == '__main__':
    run()

