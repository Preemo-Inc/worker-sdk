# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: endpoints/batch_get_artifact.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"endpoints/batch_get_artifact.proto\x12\tendpoints\"\x13\n\x11GetArtifactConfig\"\xd0\x01\n\x17\x42\x61tchGetArtifactRequest\x12[\n\x16\x63onfigs_by_artifact_id\x18\x01 \x03(\x0b\x32;.endpoints.BatchGetArtifactRequest.ConfigsByArtifactIdEntry\x1aX\n\x18\x43onfigsByArtifactIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.endpoints.GetArtifactConfig:\x02\x38\x01\";\n\x11GetArtifactResult\x12\x17\n\npart_count\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\r\n\x0b_part_count\"\xd2\x01\n\x18\x42\x61tchGetArtifactResponse\x12\\\n\x16results_by_artifact_id\x18\x01 \x03(\x0b\x32<.endpoints.BatchGetArtifactResponse.ResultsByArtifactIdEntry\x1aX\n\x18ResultsByArtifactIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.endpoints.GetArtifactResult:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'endpoints.batch_get_artifact_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BATCHGETARTIFACTREQUEST_CONFIGSBYARTIFACTIDENTRY._options = None
  _BATCHGETARTIFACTREQUEST_CONFIGSBYARTIFACTIDENTRY._serialized_options = b'8\001'
  _BATCHGETARTIFACTRESPONSE_RESULTSBYARTIFACTIDENTRY._options = None
  _BATCHGETARTIFACTRESPONSE_RESULTSBYARTIFACTIDENTRY._serialized_options = b'8\001'
  _GETARTIFACTCONFIG._serialized_start=49
  _GETARTIFACTCONFIG._serialized_end=68
  _BATCHGETARTIFACTREQUEST._serialized_start=71
  _BATCHGETARTIFACTREQUEST._serialized_end=279
  _BATCHGETARTIFACTREQUEST_CONFIGSBYARTIFACTIDENTRY._serialized_start=191
  _BATCHGETARTIFACTREQUEST_CONFIGSBYARTIFACTIDENTRY._serialized_end=279
  _GETARTIFACTRESULT._serialized_start=281
  _GETARTIFACTRESULT._serialized_end=340
  _BATCHGETARTIFACTRESPONSE._serialized_start=343
  _BATCHGETARTIFACTRESPONSE._serialized_end=553
  _BATCHGETARTIFACTRESPONSE_RESULTSBYARTIFACTIDENTRY._serialized_start=465
  _BATCHGETARTIFACTRESPONSE_RESULTSBYARTIFACTIDENTRY._serialized_end=553
# @@protoc_insertion_point(module_scope)
