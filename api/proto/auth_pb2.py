# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth.proto',
  package='auth',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nauth.proto\x12\x04\x61uth\"\x16\n\x05Token\x12\r\n\x05token\x18\x01 \x01(\t\"H\n\x07Profile\x12\x17\n\x0fhas_valid_token\x18\x01 \x01(\x08\x12\n\n\x02id\x18\x02 \x01(\x03\x12\x18\n\x04role\x18\x03 \x01(\x0e\x32\n.auth.Role*\x1b\n\x04Role\x12\x08\n\x04User\x10\x00\x12\t\n\x05\x41\x64min\x10\x01\x32,\n\x04\x41uth\x12$\n\x06Verify\x12\x0b.auth.Token\x1a\r.auth.Profileb\x06proto3'
)

_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='auth.Role',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='User', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Admin', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=118,
  serialized_end=145,
)
_sym_db.RegisterEnumDescriptor(_ROLE)

Role = enum_type_wrapper.EnumTypeWrapper(_ROLE)
User = 0
Admin = 1



_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='auth.Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='auth.Token.token', index=0,
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
  serialized_end=42,
)


_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='auth.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='has_valid_token', full_name='auth.Profile.has_valid_token', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='auth.Profile.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='auth.Profile.role', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=44,
  serialized_end=116,
)

_PROFILE.fields_by_name['role'].enum_type = _ROLE
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.enum_types_by_name['Role'] = _ROLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.Token)
  })
_sym_db.RegisterMessage(Token)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), {
  'DESCRIPTOR' : _PROFILE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.Profile)
  })
_sym_db.RegisterMessage(Profile)



_AUTH = _descriptor.ServiceDescriptor(
  name='Auth',
  full_name='auth.Auth',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=147,
  serialized_end=191,
  methods=[
  _descriptor.MethodDescriptor(
    name='Verify',
    full_name='auth.Auth.Verify',
    index=0,
    containing_service=None,
    input_type=_TOKEN,
    output_type=_PROFILE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTH)

DESCRIPTOR.services_by_name['Auth'] = _AUTH

# @@protoc_insertion_point(module_scope)
