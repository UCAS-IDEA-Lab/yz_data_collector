# -*- coding: utf-8 -*-

from os import path

# Agent Configuration 
api_port = '36563'
batch = 10
data_path = '/var/log/yz'
log_start_date = None # '2017/03/04'
wait_for_new_data = 10

# Log
log_file_path = '/var/log/yz_agent.log'
log_level = 'DEBUG'

# Manager
manager_url = 'http://127.0.0.1:45954'

# Data upload
upload_url = ['http://127.0.0.1:54999','http://127.0.0.1:54999']
load_balance_strategy = 'rr' # 'rr', 'ra' (round-robin, random)
report_url = None

if path.exists('/etc/yz_agent.conf'):
    with open('/etc/yz_agent.conf') as f:
        conf = globals()
        for line in f:
            if not re.match('\s*#', line) \
                    and not re.match('\s+', line):
                l = re.split('=', line)
                conf[l[0].strip()] = l[1].strip()

