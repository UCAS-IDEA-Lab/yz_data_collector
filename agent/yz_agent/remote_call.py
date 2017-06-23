# -*- coding: utf-8 -*-

from common import do_get, do_post
from settings import manager_url

def register_myself():
    url = manager_url + '/api/agent'
    data = {}
    return do_post(url, data)

