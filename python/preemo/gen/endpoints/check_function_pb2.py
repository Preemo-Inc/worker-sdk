# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: endpoints/check_function.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from models import registered_function_pb2 as models_dot_registered__function__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x65ndpoints/check_function.proto\x12\tendpoints\x1a models/registered_function.proto\"l\n\x14\x43heckFunctionRequest\x12<\n\x13registered_function\x18\x01 \x01(\x0b\x32\x1a.models.RegisteredFunctionH\x00\x88\x01\x01\x42\x16\n\x14_registered_function\"\x17\n\x15\x43heckFunctionResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'endpoints.check_function_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHECKFUNCTIONREQUEST._serialized_start=79
  _CHECKFUNCTIONREQUEST._serialized_end=187
  _CHECKFUNCTIONRESPONSE._serialized_start=189
  _CHECKFUNCTIONRESPONSE._serialized_end=212
# @@protoc_insertion_point(module_scope)