# -*- coding: utf-8 -*-

from os import path
import random
import re

# Agent Configuration 
api_port = '36563'
batch = 1000
data_path = '/var/log/yz'
log_start_date = None # '2017/03/04'
wait_for_new_data = 10

# Log
log_file_path = '/var/log/yz_agent.log'
log_level = 'INFO'

# Manager
manager_url = 'http://127.0.0.1:45954'

# Data upload
upload_url = ['http://127.0.0.1:54999','http://127.0.0.1:54999']
load_balance_strategy = 'rr' # 'rr', 'ra' (round-robin, random)
report_url = None

# Get configuration from the configure file
conf_file_path = '/etc/yz_agent.conf'
if path.exists(conf_file_path):
    with open(conf_file_path, 'r') as f:
        conf = globals()
        for line in f:
            if not re.match('\s*#', line) \
                    and not re.match('\s+', line):
                l = re.split('=', line)
                # TODO: handle each key
                key = l[0].strip()
                if key == 'batch' or key == 'wait_for_new_data':
                    conf[key] = int(l[1].strip())
                elif key == 'upload_url':
                    conf[key] = [url.strip() for url in l[1].strip().split(',')]
                else:
                    conf[key] = l[1].strip()

random.shuffle(upload_url)
# NOTE: just for debug
# print globals()

