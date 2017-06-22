# -*- coding: utf-8 -*-

# API
api_port = '36563'

# Log
log_file_path = '/var/log/yz_agent.log'
log_level = 'INFO'

# Manager
manager_url = 'http://127.0.0.1:45954'

# Data upload
upload_url = 'http://127.0.0.1:54999'
report_url = None

if not path.exists('/etc/yz_agent.conf'):
    continue
with open('/etc/yz_agent.conf') as f:
    conf = globals()
    for line in f:
        if not re.match('\s*#', line) \
                and not re.match('\s+', line):
            l = re.split('=', line)
            conf[l[0].strip()] = l[1].strip()

