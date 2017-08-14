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
    '/api/handler/(\w*)', 'Handler',
)

class Agents:
    def GET(self):
        return web.ok()

class Agent:
    def POST(self, agent):
        return web.created()

    def GET(self, agent):
        return web.ok()

    def DELETE(self, agent):
        print 'delete %s' % agent
        return web.ok()

class AgentAction:
    def POST(self, agent, action):
        """
        :param action: speedup, slowdown, start, stop, strategy
        """
        print agent, action
        return web.ok()

class Handlers:
    def GET(self):
        return web.ok()

class Handler:
    def POST(self, handler):
        return web.created()

    def GET(self, handler):
        return web.ok()

    def DELETE(self, handler):
        return web.ok()

def run(*args, **kwargs):
    app = web.application(urls, globals(), *args, **kwargs)
    app.run()

if __name__ == '__main__':
    run()

