# 企业端数据采集代理

## 运行环境
Linux CentOS 7

## 安装过程
```shell
./setup.sh
```
看到 "Setup successfully" 意味安装成功。

## 升级过程 (代码或配置）
```shell
python setup.py install
```

## 运行代理

### 启动 && 检查
```shell
systemctl start yz_agent
systemctl status yz_agent
```

### 系统测试
```shell
yz_test_data_gen -h
```

### 停机和检查
```shell
systemctl stop yz_agent
systemctl status yz_agent
```

### 日志文件
Default is stored at /var/log/yz_agent.log.

### 配置文件
Configuration file is located at /etc/yz_agent.conf

