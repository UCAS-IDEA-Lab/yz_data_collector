# -*- coding: utf-8 -*-

import httpclient

from optparse import OptionParser
import sys
import logging

LOG = logging.getLogger(__name__)

__commands = {
    'list': {
        'agents': httpclient.list_agents,
        'handlers': httpclient.list_handlers
    },
    'show': {
        'agent': httpclient.show_agent,
        'handler': httpclient.show_handler
    },
    'start': {
        'agent': httpclient.start_agent
    },
    'stop': {
        'agent': httpclient.stop_agent
    },
    'speedup': {
        'agent': httpclient.speedup_agent
    },
    'slowdown': {
        'agent': httpclient.slowdown_agent
    }
}

def main():
    usage = """
    %prog [options] subcmd arg0 [arg1 ...]
    subcmd:
        list agents|handlers
        show agent $agent_id|handler $handler_id
        start agent $agent_id
        stop agent $agent_id
        speedup agent $agent_id
        slowdown agent $agent_id
    """
    parser = OptionParser(usage=usage)
    parser.add_option('-H', '--host', dest='host', \
            default='localhost', \
            help='The address of manager, default is localhost.')
    parser.add_option('-P', '--port', dest='port', \
            default='45954', \
            help='The port of manager, default is 45954.')
    options, args = parser.parse_args()

    if len(args) < 2 \
            or args[0] not in __commands.keys() \
            or args[1] not in __commands[args[0]].keys():
        parser.print_help()
        sys.exit(1)
    
    ret = __commands[args[0]][args[1]](options.host, options.port, *args[2:])
    if ret is not None:
        print ret.text
    
    sys.exit(0)

if __name__ == '__main__':
    main()

