package com.iscas;

import org.apache.flume.Context;
import org.apache.flume.Event;
import org.apache.flume.event.EventBuilder;
import org.apache.flume.source.http.HTTPBadRequestException;
import org.apache.flume.source.http.HTTPSourceHandler;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.iscas.FlumeMsgListProtos.FlumeMsgList;
import com.iscas.FlumeMsgListProtos.Headers;

import javax.servlet.http.HttpServletRequest;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.io.IOException;

/**
 * HTTP Source Handler for messages use protobuf
 *
 */
public class ProtobufHandler implements HTTPSourceHandler {

  private static final Logger LOG = LoggerFactory.getLogger(ProtobufHandler.class);

  @Override
  public List<Event> getEvents(HttpServletRequest request) throws HTTPBadRequestException, Exception {
    final List<Event> events;
    FlumeMsgList msgList;
    
    try {
      msgList = FlumeMsgList.parseFrom(request.getInputStream());
    } catch(IOException ex) {
      throw new HTTPBadRequestException("Request has invalid Protobuf Syntax.", ex);
    }

    int eventCount = msgList.getMsgCount();
    events = new ArrayList<Event>(eventCount);

    for(FlumeMsgList.FlumeMsg msg: msgList.getMsgList()) {
      Headers headers = msg.getHeaders();
      Map<String, String> eventHeaders = new HashMap<String, String>();
      if(headers.hasTopic()) {
        eventHeaders.put("topic", headers.getTopic());
      }

      events.add(EventBuilder.withBody(msg.getBody().toByteArray(), eventHeaders));
    }

    return events;
  }

  @Override
  public void configure(Context context) {
  }
}

