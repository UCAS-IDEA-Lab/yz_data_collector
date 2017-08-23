# -*- coding: utf-8 -*-

import web
import json
import logging

LOG = logging.getLogger()

from agent_views import agent_view

urls = (
    '/api/agents', 'Agents',
    '/api/agent/(\w*)', 'Agent',
    '/api/agent/(\w+)/(\w+)', 'AgentAction',
    '/api/handlers', 'Handlers',
    '/api/handler/(\w*)', 'Handler',
)

class Agents:
    def GET(self):
        return agent_view.list_agents()

class Agent:
    def POST(self, agent):
        info = web.input()
        re = agent_view.register_agent(info)
        if re['success']:
            return web.created()
        else:
            return web.badrequest(message=re['reason'])

    def GET(self, agent):
        return agent_view.show_agent(agent)

    def DELETE(self, agent):
        LOG.debug('delete %s' % agent)
        return web.ok()

class AgentAction:
    def POST(self, agent, action):
        """
        :param action: speedup, slowdown, start, stop, strategy
        """
        LOG.debug("%s, %s" % (agent, action))
        return agent_view.agent_action(agent, action)

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

