# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: endpoints/execute_function.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from models import registered_function_pb2 as models_dot_registered__function__pb2
from models import value_pb2 as models_dot_value__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n endpoints/execute_function.proto\x12\tendpoints\x1a models/registered_function.proto\x1a\x12models/value.proto\"\xa3\x01\n\x16\x45xecuteFunctionRequest\x12<\n\x13\x66unction_to_execute\x18\x01 \x01(\x0b\x32\x1a.models.RegisteredFunctionH\x00\x88\x01\x01\x12%\n\tparameter\x18\x02 \x01(\x0b\x32\r.models.ValueH\x01\x88\x01\x01\x42\x16\n\x14_function_to_executeB\x0c\n\n_parameter\"H\n\x17\x45xecuteFunctionResponse\x12\"\n\x06result\x18\x01 \x01(\x0b\x32\r.models.ValueH\x00\x88\x01\x01\x42\t\n\x07_resultb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'endpoints.execute_function_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EXECUTEFUNCTIONREQUEST._serialized_start=102
  _EXECUTEFUNCTIONREQUEST._serialized_end=265
  _EXECUTEFUNCTIONRESPONSE._serialized_start=267
  _EXECUTEFUNCTIONRESPONSE._serialized_end=339
# @@protoc_insertion_point(module_scope)
