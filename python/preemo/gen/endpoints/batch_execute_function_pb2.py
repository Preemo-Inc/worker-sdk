# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: endpoints/batch_execute_function.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from models import registered_function_pb2 as models_dot_registered__function__pb2
from models import value_pb2 as models_dot_value__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&endpoints/batch_execute_function.proto\x12\tendpoints\x1a models/registered_function.proto\x1a\x12models/value.proto\"\x98\x02\n\x1b\x42\x61tchExecuteFunctionRequest\x12<\n\x13\x66unction_to_execute\x18\x01 \x01(\x0b\x32\x1a.models.RegisteredFunctionH\x00\x88\x01\x01\x12Z\n\x13parameters_by_index\x18\x02 \x03(\x0b\x32=.endpoints.BatchExecuteFunctionRequest.ParametersByIndexEntry\x1aG\n\x16ParametersByIndexEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.models.Value:\x02\x38\x01\x42\x16\n\x14_function_to_execute\"\xbb\x01\n\x1c\x42\x61tchExecuteFunctionResponse\x12U\n\x10results_by_index\x18\x01 \x03(\x0b\x32;.endpoints.BatchExecuteFunctionResponse.ResultsByIndexEntry\x1a\x44\n\x13ResultsByIndexEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.models.Value:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'endpoints.batch_execute_function_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BATCHEXECUTEFUNCTIONREQUEST_PARAMETERSBYINDEXENTRY._options = None
  _BATCHEXECUTEFUNCTIONREQUEST_PARAMETERSBYINDEXENTRY._serialized_options = b'8\001'
  _BATCHEXECUTEFUNCTIONRESPONSE_RESULTSBYINDEXENTRY._options = None
  _BATCHEXECUTEFUNCTIONRESPONSE_RESULTSBYINDEXENTRY._serialized_options = b'8\001'
  _BATCHEXECUTEFUNCTIONREQUEST._serialized_start=108
  _BATCHEXECUTEFUNCTIONREQUEST._serialized_end=388
  _BATCHEXECUTEFUNCTIONREQUEST_PARAMETERSBYINDEXENTRY._serialized_start=293
  _BATCHEXECUTEFUNCTIONREQUEST_PARAMETERSBYINDEXENTRY._serialized_end=364
  _BATCHEXECUTEFUNCTIONRESPONSE._serialized_start=391
  _BATCHEXECUTEFUNCTIONRESPONSE._serialized_end=578
  _BATCHEXECUTEFUNCTIONRESPONSE_RESULTSBYINDEXENTRY._serialized_start=510
  _BATCHEXECUTEFUNCTIONRESPONSE_RESULTSBYINDEXENTRY._serialized_end=578
# @@protoc_insertion_point(module_scope)
