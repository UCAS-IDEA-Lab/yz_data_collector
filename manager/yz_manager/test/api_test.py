# -*- coding: utf-8 -*-

import sys
sys.path.append('/root/workspace/yz_data_collector/manager')

import requests
import unittest

from yz_manager.settings import api_port

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:' + api_port
        self.client = requests

    def test_api_agent_post(self):
        url = self.url + '/api/agent/'
        data = {
            'id': '123456',
            'addr': '192.168.1.123'
        }
        re = self.client.post(url, data=data, timeout=2)
        self.assertEqual(re.status_code, 201)

    def test_api_agent_delete(self):
        url = self.url + '/api/agent/123456'
        re = self.client.delete(url, timeout=2)
        self.assertEqual(re.status_code, 200)

    def test_api_agent_get(self):
        url = self.url + '/api/agent/123456'
        re = self.client.get(url, timeout=2)
        self.assertEqual(re.status_code, 200)

    def test_api_agents_get(self):
        url = self.url + '/api/agents'
        re = self.client.get(url, timeout=2)
        self.assertEqual(re.status_code, 200)

    def test_api_agent_speedup(self):
        url = self.url + '/api/agent/123456/speedup'
        re = self.client.post(url, timeout=2)
        self.assertEqual(re.status_code, 200)

    def test_api_agent_slowdown(self):
        url = self.url + '/api/agent/123456/slowdown'
        re = self.client.post(url, timeout=2)
        self.assertEqual(re.status_code, 200)

    def test_api_agent_start(self):
        url = self.url + '/api/agent/123456/start'
        re = self.client.post(url, timeout=2)
        self.assertEqual(re.status_code, 200)

    def test_api_agent_stop(self):
        url = self.url + '/api/agent/123456/stop'
        re = self.client.post(url, timeout=2)
        self.assertEqual(re.status_code, 200)

    def test_api_agent_strategy(self):
        url = self.url + '/api/agent/123456/strategy'
        re = self.client.post(url, timeout=2)
        self.assertEqual(re.status_code, 200)

    def test_api_handler_post(self):
        url = self.url + '/api/handler/'
        data = {
            'id': '123456',
            'addr': '192.168.1.123'
        }
        re = self.client.post(url, data=data, timeout=2)
        self.assertEqual(re.status_code, 201)

    def test_api_handler_delete(self):
        url = self.url + '/api/handler/123456'
        re = self.client.delete(url, timeout=2)
        self.assertEqual(re.status_code, 200)

    def test_api_handler_get(self):
        url = self.url + '/api/handler/123456'
        re = self.client.get(url, timeout=2)
        self.assertEqual(re.status_code, 200)

    def test_api_handlers_get(self):
        url = self.url + '/api/handlers'
        re = self.client.get(url, timeout=2)
        self.assertEqual(re.status_code, 200)

if __name__ == '__main__':
    unittest.main()

