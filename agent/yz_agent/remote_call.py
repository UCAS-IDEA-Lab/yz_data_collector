# -*- coding: utf-8 -*-

from common import do_get, do_post
from settings import manager_url, upload_url, load_balance_strategy, \
        agent_id
from serialize.flume_msg_pb2 import FlumeMsgList

import json
import logging
import random

LOG = logging.getLogger(__name__)

def register_myself():
    url = manager_url + '/api/agent/'
    data = {
        'id': agent_id,
        'addr': '127.0.0.1'
    }
    return do_post(url, data)

# tmp_timer = 0
rr_num = 0
def upload(data_list, topic):
    """
    :param data_list: list, an array of message body
    :param topic: string, message topic
    """
    # NOTE: Debug code
    # if data is None:
        # return {'success': False}
    # global tmp_timer
    # if tmp_timer % 10000 == 0:
        # LOG.debug([{'headers': {}, 'body': json.dumps(data)}])
    # tmp_timer += 1
    # return {'success': True}

    if data_list is None:
        return {'success': False}

    if load_balance_strategy == 'rr':
        global rr_num
        url = upload_url[rr_num]
        rr_num = (rr_num + 1) % len(upload_url)
    else:
        url = random.choice(upload_url)

    msg_list = FlumeMsgList()
    for data in data_list:
        msg = msg_list.msg.add()
        msg.headers.topic = topic
        msg.body = data

    return do_post(url, msg_list.SerializeToString(), \
            headers={"Content-Type":"application/octet-stream","Connection":"keep-alive"})

