# -*- coding: utf-8 -*-

from settings import log_file_path, log_level, api_port
from remote_call import register_myself
import api as api_server
from agent import Agent, ErrorHandleAgent

import logging
import sys
import time

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
    # TODO: Register first
    # ret = register_myself()
    # if not ret['success']:
        # LOG.error(ret['data'])
        # sys.exit(1)

    # Start Agent
    exp_agent = Agent('ExpAgent', 1, 'ExpressContract')
    exp_state_agent = Agent('ExpStateAgent', 1, 'ExpressContractState')
    
    exp_agent.start()
    exp_state_agent.start()

    # Start API
    sys.argv.append(api_port)
    sys.argv[1] = api_port
    api_server.run()

if __name__ == '__main__':
    main()

