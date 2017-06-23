# -*- coding: utf-8 -*-

from settings import log_file_path, log_level, api_port
from remote_call import register_myself
import api as api_server

import logging
import sys

_log_level = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR
}

logging.basicConfig(\
        level=_log_level[log_level], \
        format='[%(asctime)s] %(name)-12s %(levelname)-8s %(message)s', \
        datefmt='%m-%d %H:%M', \
        filename=log_file_path, \
        filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

LOG = logging.getLogger(__name__)

def main():
    ret = register_myself()
    if not ret['success']:
        LOG.error(ret['data'])
        sys.exit(1)

    while True:
        try:
            # TODO: Start Agent

            # Start API
            sys.argv[1] = int(api_port)
            api_server.run()

        except Exception, e:
            LOG.error(e)

if __name__ == '__main__':
    main()

