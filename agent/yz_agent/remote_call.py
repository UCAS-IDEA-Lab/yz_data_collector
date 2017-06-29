# -*- coding: utf-8 -*-

from common import do_get, do_post
from settings import manager_url, upload_url

import logging

LOG = logging.getLogger()

def register_myself():
    url = manager_url + '/api/agent'
    data = {}
    return do_post(url, data)

tmp_timer = 0
def upload(data):
    # NOTE: Debug code
    if data is None:
        return {'success': False}
    global tmp_timer
    if tmp_timer % 10000 == 0:
        LOG.debug(data)
    tmp_timer += 1
    return {'success': True}

    # TODO: load balance based on strategy
    if data is None:
        return {'success': False}
    url = upload_url
    return do_post(url, data)

