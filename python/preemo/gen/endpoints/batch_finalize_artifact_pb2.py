# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: endpoints/batch_finalize_artifact.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'endpoints/batch_finalize_artifact.proto\x12\tendpoints\"\x18\n\x16\x46inalizeArtifactConfig\"\xdf\x01\n\x1c\x42\x61tchFinalizeArtifactRequest\x12`\n\x16\x63onfigs_by_artifact_id\x18\x01 \x03(\x0b\x32@.endpoints.BatchFinalizeArtifactRequest.ConfigsByArtifactIdEntry\x1a]\n\x18\x43onfigsByArtifactIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.endpoints.FinalizeArtifactConfig:\x02\x38\x01\"\x18\n\x16\x46inalizeArtifactResult\"\xe1\x01\n\x1d\x42\x61tchFinalizeArtifactResponse\x12\x61\n\x16results_by_artifact_id\x18\x01 \x03(\x0b\x32\x41.endpoints.BatchFinalizeArtifactResponse.ResultsByArtifactIdEntry\x1a]\n\x18ResultsByArtifactIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.endpoints.FinalizeArtifactResult:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'endpoints.batch_finalize_artifact_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BATCHFINALIZEARTIFACTREQUEST_CONFIGSBYARTIFACTIDENTRY._options = None
  _BATCHFINALIZEARTIFACTREQUEST_CONFIGSBYARTIFACTIDENTRY._serialized_options = b'8\001'
  _BATCHFINALIZEARTIFACTRESPONSE_RESULTSBYARTIFACTIDENTRY._options = None
  _BATCHFINALIZEARTIFACTRESPONSE_RESULTSBYARTIFACTIDENTRY._serialized_options = b'8\001'
  _FINALIZEARTIFACTCONFIG._serialized_start=54
  _FINALIZEARTIFACTCONFIG._serialized_end=78
  _BATCHFINALIZEARTIFACTREQUEST._serialized_start=81
  _BATCHFINALIZEARTIFACTREQUEST._serialized_end=304
  _BATCHFINALIZEARTIFACTREQUEST_CONFIGSBYARTIFACTIDENTRY._serialized_start=211
  _BATCHFINALIZEARTIFACTREQUEST_CONFIGSBYARTIFACTIDENTRY._serialized_end=304
  _FINALIZEARTIFACTRESULT._serialized_start=306
  _FINALIZEARTIFACTRESULT._serialized_end=330
  _BATCHFINALIZEARTIFACTRESPONSE._serialized_start=333
  _BATCHFINALIZEARTIFACTRESPONSE._serialized_end=558
  _BATCHFINALIZEARTIFACTRESPONSE_RESULTSBYARTIFACTIDENTRY._serialized_start=465
  _BATCHFINALIZEARTIFACTRESPONSE_RESULTSBYARTIFACTIDENTRY._serialized_end=558
# @@protoc_insertion_point(module_scope)
