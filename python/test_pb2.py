# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='test',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\ntest.proto\x12\x04test\"\x17\n\x08HelloReq\x12\x0b\n\x03pic\x18\x01 \x01(\t\"\x1a\n\x08HelloRes\x12\x0e\n\x06result\x18\x01 \x01(\t23\n\x05Hello\x12*\n\x08HelloLys\x12\x0e.test.HelloReq\x1a\x0e.test.HelloResb\x06proto3'
)




_HELLOREQ = _descriptor.Descriptor(
  name='HelloReq',
  full_name='test.HelloReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pic', full_name='test.HelloReq.pic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=43,
)


_HELLORES = _descriptor.Descriptor(
  name='HelloRes',
  full_name='test.HelloRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.HelloRes.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=71,
)

DESCRIPTOR.message_types_by_name['HelloReq'] = _HELLOREQ
DESCRIPTOR.message_types_by_name['HelloRes'] = _HELLORES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloReq = _reflection.GeneratedProtocolMessageType('HelloReq', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQ,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloReq)
  })
_sym_db.RegisterMessage(HelloReq)

HelloRes = _reflection.GeneratedProtocolMessageType('HelloRes', (_message.Message,), {
  'DESCRIPTOR' : _HELLORES,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloRes)
  })
_sym_db.RegisterMessage(HelloRes)



_HELLO = _descriptor.ServiceDescriptor(
  name='Hello',
  full_name='test.Hello',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=73,
  serialized_end=124,
  methods=[
  _descriptor.MethodDescriptor(
    name='HelloLys',
    full_name='test.Hello.HelloLys',
    index=0,
    containing_service=None,
    input_type=_HELLOREQ,
    output_type=_HELLORES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLO)

DESCRIPTOR.services_by_name['Hello'] = _HELLO

# @@protoc_insertion_point(module_scope)