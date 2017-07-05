# -*- coding: utf-8 -*-

from common import do_get, do_post
from settings import manager_url, upload_url, load_balance_strategy
from serialize.flume_msg_pb2 import FlumeMsgList

import json
import logging
import random
from google.protobuf import json_format as jf

LOG = logging.getLogger()

def register_myself():
    url = manager_url + '/api/agent'
    data = {}
    return do_post(url, data)

tmp_timer = 0
def upload(data, **kw):
    """
    :param data: string, message body
    """
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
    pb = FlumeMsgList()
    # TODO: must be a json string!
    jf.Parse([{'headers': kw, 'body': data}], pb)
    return do_post(url, , \
            headers={"Content-Type":"application/octet-stream","Connection":"keep-alive"})

