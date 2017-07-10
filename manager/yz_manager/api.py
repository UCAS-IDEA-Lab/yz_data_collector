# -*- coding: utf-8 -*-

import web
import json
import logging

LOG = logging.getLogger()

urls = (
    '/api/agents', 'Agents',
    '/api/agent/(\w*)', 'Agent',
    '/api/agent/(\w+)/(\w+)', 'AgentAction',
    '/api/handlers', 'Handlers',
    '/api/Handler/(\w*)', 'Handler',
)

class Agents:
    def GET(self):
        pass

class Agent:
    def POST(self):
        pass

    def GET(self, agent):
        pass

    def DELETE(self, agent):
        print 'delete %s' % agent
        return web.ok()

class AgentAction:
    def POST(self, agent, action):
        """
        :param action: speedup, slowdown, start, stop, strategy
        """
        pass

class Handlers:
    def GET(self):
        pass

class Handler:
    def POST(self):
        pass

    def GET(self, handler):
        pass

    def DELETE(self, handler):
        pass

def run(*args, **kwargs):
    app = web.application(urls, globals(), *args, **kwargs)
    app.run()

if __name__ == '__main__':
    run()

