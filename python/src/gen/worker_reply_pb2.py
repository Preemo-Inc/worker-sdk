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


from shared import status_pb2 as shared_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12worker_reply.proto\x1a\x13shared/status.proto\"b\n\x15RegisterFunctionReply\x12\x1c\n\x06status\x18\x01 \x01(\x0e\x32\x07.StatusH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\t\n\x07_statusB\n\n\x08_message\"K\n\x0bWorkerReply\x12\x33\n\x11register_function\x18\x01 \x01(\x0b\x32\x16.RegisterFunctionReplyH\x00\x42\x07\n\x05replyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'worker_reply_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTERFUNCTIONREPLY._serialized_start=43
  _REGISTERFUNCTIONREPLY._serialized_end=141
  _WORKERREPLY._serialized_start=143
  _WORKERREPLY._serialized_end=218
# @@protoc_insertion_point(module_scope)
