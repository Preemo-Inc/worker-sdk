# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: endpoints/batch_create_artifact.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%endpoints/batch_create_artifact.proto\x12\tendpoints\"K\n\x14\x43reateArtifactConfig\x12*\n\x04type\x18\x01 \x01(\x0e\x32\x17.endpoints.ArtifactTypeH\x00\x88\x01\x01\x42\x07\n\x05_type\"\xc9\x01\n\x1a\x42\x61tchCreateArtifactRequest\x12S\n\x10\x63onfigs_by_index\x18\x01 \x03(\x0b\x32\x39.endpoints.BatchCreateArtifactRequest.ConfigsByIndexEntry\x1aV\n\x13\x43onfigsByIndexEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.endpoints.CreateArtifactConfig:\x02\x38\x01\"z\n\x14\x43reateArtifactResult\x12\x18\n\x0b\x61rtifact_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\x13part_size_threshold\x18\x02 \x01(\x04H\x01\x88\x01\x01\x42\x0e\n\x0c_artifact_idB\x16\n\x14_part_size_threshold\"\xcb\x01\n\x1b\x42\x61tchCreateArtifactResponse\x12T\n\x10results_by_index\x18\x01 \x03(\x0b\x32:.endpoints.BatchCreateArtifactResponse.ResultsByIndexEntry\x1aV\n\x13ResultsByIndexEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.endpoints.CreateArtifactResult:\x02\x38\x01*a\n\x0c\x41rtifactType\x12\x1d\n\x19\x41RTIFACT_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x41RTIFACT_TYPE_PARAMS\x10\x01\x12\x18\n\x14\x41RTIFACT_TYPE_RESULT\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'endpoints.batch_create_artifact_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BATCHCREATEARTIFACTREQUEST_CONFIGSBYINDEXENTRY._options = None
  _BATCHCREATEARTIFACTREQUEST_CONFIGSBYINDEXENTRY._serialized_options = b'8\001'
  _BATCHCREATEARTIFACTRESPONSE_RESULTSBYINDEXENTRY._options = None
  _BATCHCREATEARTIFACTRESPONSE_RESULTSBYINDEXENTRY._serialized_options = b'8\001'
  _ARTIFACTTYPE._serialized_start=663
  _ARTIFACTTYPE._serialized_end=760
  _CREATEARTIFACTCONFIG._serialized_start=52
  _CREATEARTIFACTCONFIG._serialized_end=127
  _BATCHCREATEARTIFACTREQUEST._serialized_start=130
  _BATCHCREATEARTIFACTREQUEST._serialized_end=331
  _BATCHCREATEARTIFACTREQUEST_CONFIGSBYINDEXENTRY._serialized_start=245
  _BATCHCREATEARTIFACTREQUEST_CONFIGSBYINDEXENTRY._serialized_end=331
  _CREATEARTIFACTRESULT._serialized_start=333
  _CREATEARTIFACTRESULT._serialized_end=455
  _BATCHCREATEARTIFACTRESPONSE._serialized_start=458
  _BATCHCREATEARTIFACTRESPONSE._serialized_end=661
  _BATCHCREATEARTIFACTRESPONSE_RESULTSBYINDEXENTRY._serialized_start=575
  _BATCHCREATEARTIFACTRESPONSE_RESULTSBYINDEXENTRY._serialized_end=661
# @@protoc_insertion_point(module_scope)
