# -*- coding: utf-8 -*-

from settings import log_file_path, log_level, api_port, ping_interval
import api as api_server
from routine import PingRoutine

import sys
import logging

_log_level = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR
}

logging.basicConfig(\
        level=_log_level[log_level], \
        format='[%(asctime)s] [%(levelname)-8s] [%(threadName)-16s] %(filename)-12s(line%(lineno)4d): %(message)s', \
        datefmt='%m-%d %H:%M', \
        filename=log_file_path, \
        filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(threadName)-16s: [%(filename)-12s(line%(lineno)4d)] %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

LOG = logging.getLogger(__name__)

def main():
    # Start Routines
    ping_routine = PingRoutine('PingRoutine', 1, ping_interval)
    ping_routine.start()

    # Start API
    sys.argv.append(api_port)
    sys.argv[1] = api_port
    api_server.run()

if __name__ == '__main__':
    main()

