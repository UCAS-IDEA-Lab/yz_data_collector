# -*- coding: utf-8 -*-

import sys
sys.path.append('/root/workspace/yz_data_collector/manager')

import unittest
import time

from yz_manager.routine import PingRoutine

class TestRoutine(unittest.TestCase):

    def test_ping_routine(self):
        ping = PingRoutine('PingRoutine', 1, 1)
        ping.start()
        time.sleep(10)
        ping.stop()
        self.assertTrue(True)

