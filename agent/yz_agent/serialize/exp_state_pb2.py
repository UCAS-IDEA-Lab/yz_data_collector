# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exp_state.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='exp_state.proto',
  package='youzhen',
  serialized_pb='\n\x0f\x65xp_state.proto\x12\x07youzhen\":\n\x0c\x45xpStateInfo\x12\x1a\n\x12logisticproviderid\x18\x01 \x02(\t\x12\x0e\n\x06mailno\x18\x02 \x02(\t\"\x89\x01\n\rExpStateState\x12\x0c\n\x04time\x18\x01 \x02(\x01\x12\x0c\n\x04\x64\x65sc\x18\x02 \x02(\t\x12\x0c\n\x04\x63ity\x18\x03 \x02(\t\x12\x14\n\x0c\x66\x61\x63ilitytype\x18\x04 \x02(\t\x12\x12\n\nfacilityno\x18\x05 \x02(\t\x12\x14\n\x0c\x66\x61\x63ilityname\x18\x06 \x02(\t\x12\x0e\n\x06\x61\x63tion\x18\x07 \x02(\t\":\n\x0f\x45xpStateContact\x12\x11\n\tcontacter\x18\x01 \x02(\t\x12\x14\n\x0c\x63ontactphone\x18\x02 \x02(\t\"\x81\x01\n\x08\x45xpState\x12#\n\x04info\x18\x01 \x02(\x0b\x32\x15.youzhen.ExpStateInfo\x12%\n\x05state\x18\x02 \x02(\x0b\x32\x16.youzhen.ExpStateState\x12)\n\x07\x63ontact\x18\x03 \x02(\x0b\x32\x18.youzhen.ExpStateContact\"W\n\x0b\x45xpStateMsg\x12\n\n\x02id\x18\x01 \x02(\t\x12\x1f\n\x04\x64\x61ta\x18\x02 \x02(\x0b\x32\x11.youzhen.ExpState\x12\x0c\n\x04type\x18\x03 \x02(\t\x12\r\n\x05usage\x18\x04 \x02(\t')




_EXPSTATEINFO = _descriptor.Descriptor(
  name='ExpStateInfo',
  full_name='youzhen.ExpStateInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logisticproviderid', full_name='youzhen.ExpStateInfo.logisticproviderid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mailno', full_name='youzhen.ExpStateInfo.mailno', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=28,
  serialized_end=86,
)


_EXPSTATESTATE = _descriptor.Descriptor(
  name='ExpStateState',
  full_name='youzhen.ExpStateState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='youzhen.ExpStateState.time', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desc', full_name='youzhen.ExpStateState.desc', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city', full_name='youzhen.ExpStateState.city', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='facilitytype', full_name='youzhen.ExpStateState.facilitytype', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='facilityno', full_name='youzhen.ExpStateState.facilityno', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='facilityname', full_name='youzhen.ExpStateState.facilityname', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='youzhen.ExpStateState.action', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=89,
  serialized_end=226,
)


_EXPSTATECONTACT = _descriptor.Descriptor(
  name='ExpStateContact',
  full_name='youzhen.ExpStateContact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contacter', full_name='youzhen.ExpStateContact.contacter', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contactphone', full_name='youzhen.ExpStateContact.contactphone', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=228,
  serialized_end=286,
)


_EXPSTATE = _descriptor.Descriptor(
  name='ExpState',
  full_name='youzhen.ExpState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='youzhen.ExpState.info', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='youzhen.ExpState.state', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contact', full_name='youzhen.ExpState.contact', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=289,
  serialized_end=418,
)


_EXPSTATEMSG = _descriptor.Descriptor(
  name='ExpStateMsg',
  full_name='youzhen.ExpStateMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='youzhen.ExpStateMsg.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='youzhen.ExpStateMsg.data', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='youzhen.ExpStateMsg.type', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usage', full_name='youzhen.ExpStateMsg.usage', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=420,
  serialized_end=507,
)

_EXPSTATE.fields_by_name['info'].message_type = _EXPSTATEINFO
_EXPSTATE.fields_by_name['state'].message_type = _EXPSTATESTATE
_EXPSTATE.fields_by_name['contact'].message_type = _EXPSTATECONTACT
_EXPSTATEMSG.fields_by_name['data'].message_type = _EXPSTATE
DESCRIPTOR.message_types_by_name['ExpStateInfo'] = _EXPSTATEINFO
DESCRIPTOR.message_types_by_name['ExpStateState'] = _EXPSTATESTATE
DESCRIPTOR.message_types_by_name['ExpStateContact'] = _EXPSTATECONTACT
DESCRIPTOR.message_types_by_name['ExpState'] = _EXPSTATE
DESCRIPTOR.message_types_by_name['ExpStateMsg'] = _EXPSTATEMSG

class ExpStateInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXPSTATEINFO

  # @@protoc_insertion_point(class_scope:youzhen.ExpStateInfo)

class ExpStateState(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXPSTATESTATE

  # @@protoc_insertion_point(class_scope:youzhen.ExpStateState)

class ExpStateContact(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXPSTATECONTACT

  # @@protoc_insertion_point(class_scope:youzhen.ExpStateContact)

class ExpState(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXPSTATE

  # @@protoc_insertion_point(class_scope:youzhen.ExpState)

class ExpStateMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXPSTATEMSG

  # @@protoc_insertion_point(class_scope:youzhen.ExpStateMsg)


# @@protoc_insertion_point(module_scope)
