# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: worker_request.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14worker_request.proto\"V\n\x12RegisteredFunction\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tnamespace\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\x0c\n\n_namespace\"j\n\x17RegisterFunctionRequest\x12\x36\n\x14\x66unction_to_register\x18\x01 \x01(\x0b\x32\x13.RegisteredFunctionH\x00\x88\x01\x01\x42\x17\n\x15_function_to_register\"Q\n\rWorkerRequest\x12\x35\n\x11register_function\x18\x01 \x01(\x0b\x32\x18.RegisterFunctionRequestH\x00\x42\t\n\x07requestb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'worker_request_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTEREDFUNCTION._serialized_start=24
  _REGISTEREDFUNCTION._serialized_end=110
  _REGISTERFUNCTIONREQUEST._serialized_start=112
  _REGISTERFUNCTIONREQUEST._serialized_end=218
  _WORKERREQUEST._serialized_start=220
  _WORKERREQUEST._serialized_end=301
# @@protoc_insertion_point(module_scope)