# Flume-protobuf-handler

## Pre-required
Apache Maven
```shell
yum install maven
```

## Package
```shell
mvn package
```
This command will generate a jar file called flume-protobuf-handler.jar.

## Deploy
Place flume-protobuf-hander.jar under $FLUME_HOME/plugins.d/$Any_name/lib.

If $FLUME_HOME was not set, starting agent with "--plugin-path $Any_Path/plugins.d".

