# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: worker_reply.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12worker_reply.proto\"h\n\x15RegisterFunctionReply\x12\"\n\x06status\x18\x01 \x01(\x0e\x32\r.WorkerStatusH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\t\n\x07_statusB\n\n\x08_message\"K\n\x0bWorkerReply\x12\x33\n\x11register_function\x18\x01 \x01(\x0b\x32\x16.RegisterFunctionReplyH\x00\x42\x07\n\x05reply*c\n\x0cWorkerStatus\x12\x1d\n\x19WORKER_STATUS_UNSPECIFIED\x10\x00\x12\x19\n\x15WORKER_STATUS_SUCCESS\x10\x01\x12\x19\n\x15WORKER_STATUS_FAILURE\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'worker_reply_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WORKERSTATUS._serialized_start=205
  _WORKERSTATUS._serialized_end=304
  _REGISTERFUNCTIONREPLY._serialized_start=22
  _REGISTERFUNCTIONREPLY._serialized_end=126
  _WORKERREPLY._serialized_start=128
  _WORKERREPLY._serialized_end=203
# @@protoc_insertion_point(module_scope)
