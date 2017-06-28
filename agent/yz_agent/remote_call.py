# -*- coding: utf-8 -*-

from common import do_get, do_post
from settings import manager_url, upload_url

def register_myself():
    url = manager_url + '/api/agent'
    data = {}
    return do_post(url, data)

def upload(data):
    return {'success': True}
    # TODO: load balance based on strategy
    if data is None:
        return {'success': False}
    url = upload_url
    return do_post(url, data)

