# Protocol Buffer Message Format

## Pre-require
```shell
yum install protobuf
```

## Python
```shell
protoc --python_out=../agent/yz_agent/serialize/ msg.proto
```

## Java
```shell
protoc --Java_out=../flume-protobuf-handler/src/main/java flume_msg.proto
```

