# -*- coding: utf-8 -*-

from os import path
import random
import re

# Manager Configuration 
api_port = '45954'

mysql_addr = 'localhost'
mysql_port = 3306
mysql_user = 'root'
mysql_pwd = ''
mysql_db = 'yz'

# Agent Configuration
agent_api_port = '36563'

# Log
log_file_path = '/var/log/yz_manager.log'
log_level = 'DEBUG'

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

# NOTE: just for debug
# print globals()

