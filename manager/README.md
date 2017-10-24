# 管理端软件

## 运行环境
Linux CentOS 7

## 安装
```shell
./setup.sh
```
See "Setup successfully" means finished.

## 升级(代码或配置）

```shell
python setup.py install
```

## 执行

### 启动 && 检查
```shell
systemctl start yz_manager
systemctl status yz_manager
```

### 测试
```shell
```

### 停机 && 节点
```shell
systemctl stop yz_manager
systemctl status yz_manager
```

### 日志
Default is stored at /var/log/yz_manager.log.

### 配置
Configuration file is located at /etc/yz_manager.conf

