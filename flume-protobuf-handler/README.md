# Flume-protobuf-handler 安装

## 预安装包管理软件
Apache Maven
```shell
yum install maven
```

## 安装包
```shell
mvn package
```
This command will generate a jar file called flume-protobuf-handler.jar.

## 部署
Place flume-protobuf-hander.jar under $FLUME_HOME/plugins.d/$Any_name/lib.

If $FLUME_HOME was not set, starting agent with "--plugin-path $Any_Path/plugins.d".

