# Manager

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
systemctl start yz_manager
systemctl status yz_manager
```

### Test
```shell
```

### Stop && Check
```shell
systemctl stop yz_manager
systemctl status yz_manager
```

### Log
Default is stored at /var/log/yz_manager.log.

You can configure it at yz_manager.settings.py.

