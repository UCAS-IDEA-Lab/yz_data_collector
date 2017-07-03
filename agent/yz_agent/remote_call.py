# -*- coding: utf-8 -*-

from common import do_get, do_post
from settings import manager_url, upload_url, load_balance_strategy

import json
import logging
import random

LOG = logging.getLogger()

def register_myself():
    url = manager_url + '/api/agent'
    data = {}
    return do_post(url, data)

tmp_timer = 0
def upload(data):
    # NOTE: Debug code
    # if data is None:
        # return {'success': False}
    # global tmp_timer
    # if tmp_timer % 10000 == 0:
        # LOG.debug([{'headers': {}, 'body': json.dumps(data)}])
    # tmp_timer += 1
    # return {'success': True}

    if data is None:
        return {'success': False}
    # TODO: load balance based on strategy, maintain a client pool
    # if load_balance_strategy == 'ra':
    url = random.choice(upload_url)
    return do_post(url, [{'headers': {}, 'body': json.dumps(data)}], \
            headers={"Content-Type":"application/json","Connection":"keep-alive"})

