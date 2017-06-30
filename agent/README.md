# Agent

## Environment
CentOS 7

## Setup
```shell
./setup.sh
```
See "Setup successfully" means finished.

## Update(code or settings):
```shell
python setup.py install
```

## Run

### Start && Check
```shell
systemctl start yz_agent
systemctl status yz_agent
```

### Test
```shell
yz_test_data_gen -h
```

### Stop && Check
```shell
systemctl stop yz_agent
systemctl status yz_agent
```

### Log
Default is stored at /var/log/yz_agent.log.

### Configuration
Configuration file is located at /etc/yz_agent.conf

