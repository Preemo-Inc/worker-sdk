# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: endpoints/batch_allocate_artifact_part.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,endpoints/batch_allocate_artifact_part.proto\x12\tendpoints\"$\n\"AllocateArtifactPartConfigMetadata\"\xed\x01\n\x1a\x41llocateArtifactPartConfig\x12\x62\n\x18metadatas_by_part_number\x18\x01 \x03(\x0b\x32@.endpoints.AllocateArtifactPartConfig.MetadatasByPartNumberEntry\x1ak\n\x1aMetadatasByPartNumberEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.endpoints.AllocateArtifactPartConfigMetadata:\x02\x38\x01\"\xeb\x01\n BatchAllocateArtifactPartRequest\x12\x64\n\x16\x63onfigs_by_artifact_id\x18\x01 \x03(\x0b\x32\x44.endpoints.BatchAllocateArtifactPartRequest.ConfigsByArtifactIdEntry\x1a\x61\n\x18\x43onfigsByArtifactIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.endpoints.AllocateArtifactPartConfig:\x02\x38\x01\"$\n\"AllocateArtifactPartResultMetadata\"\xed\x01\n\x1a\x41llocateArtifactPartResult\x12\x62\n\x18metadatas_by_part_number\x18\x01 \x03(\x0b\x32@.endpoints.AllocateArtifactPartResult.MetadatasByPartNumberEntry\x1ak\n\x1aMetadatasByPartNumberEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.endpoints.AllocateArtifactPartResultMetadata:\x02\x38\x01\"\xed\x01\n!BatchAllocateArtifactPartResponse\x12\x65\n\x16results_by_artifact_id\x18\x01 \x03(\x0b\x32\x45.endpoints.BatchAllocateArtifactPartResponse.ResultsByArtifactIdEntry\x1a\x61\n\x18ResultsByArtifactIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.endpoints.AllocateArtifactPartResult:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'endpoints.batch_allocate_artifact_part_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ALLOCATEARTIFACTPARTCONFIG_METADATASBYPARTNUMBERENTRY._options = None
  _ALLOCATEARTIFACTPARTCONFIG_METADATASBYPARTNUMBERENTRY._serialized_options = b'8\001'
  _BATCHALLOCATEARTIFACTPARTREQUEST_CONFIGSBYARTIFACTIDENTRY._options = None
  _BATCHALLOCATEARTIFACTPARTREQUEST_CONFIGSBYARTIFACTIDENTRY._serialized_options = b'8\001'
  _ALLOCATEARTIFACTPARTRESULT_METADATASBYPARTNUMBERENTRY._options = None
  _ALLOCATEARTIFACTPARTRESULT_METADATASBYPARTNUMBERENTRY._serialized_options = b'8\001'
  _BATCHALLOCATEARTIFACTPARTRESPONSE_RESULTSBYARTIFACTIDENTRY._options = None
  _BATCHALLOCATEARTIFACTPARTRESPONSE_RESULTSBYARTIFACTIDENTRY._serialized_options = b'8\001'
  _ALLOCATEARTIFACTPARTCONFIGMETADATA._serialized_start=59
  _ALLOCATEARTIFACTPARTCONFIGMETADATA._serialized_end=95
  _ALLOCATEARTIFACTPARTCONFIG._serialized_start=98
  _ALLOCATEARTIFACTPARTCONFIG._serialized_end=335
  _ALLOCATEARTIFACTPARTCONFIG_METADATASBYPARTNUMBERENTRY._serialized_start=228
  _ALLOCATEARTIFACTPARTCONFIG_METADATASBYPARTNUMBERENTRY._serialized_end=335
  _BATCHALLOCATEARTIFACTPARTREQUEST._serialized_start=338
  _BATCHALLOCATEARTIFACTPARTREQUEST._serialized_end=573
  _BATCHALLOCATEARTIFACTPARTREQUEST_CONFIGSBYARTIFACTIDENTRY._serialized_start=476
  _BATCHALLOCATEARTIFACTPARTREQUEST_CONFIGSBYARTIFACTIDENTRY._serialized_end=573
  _ALLOCATEARTIFACTPARTRESULTMETADATA._serialized_start=575
  _ALLOCATEARTIFACTPARTRESULTMETADATA._serialized_end=611
  _ALLOCATEARTIFACTPARTRESULT._serialized_start=614
  _ALLOCATEARTIFACTPARTRESULT._serialized_end=851
  _ALLOCATEARTIFACTPARTRESULT_METADATASBYPARTNUMBERENTRY._serialized_start=744
  _ALLOCATEARTIFACTPARTRESULT_METADATASBYPARTNUMBERENTRY._serialized_end=851
  _BATCHALLOCATEARTIFACTPARTRESPONSE._serialized_start=854
  _BATCHALLOCATEARTIFACTPARTRESPONSE._serialized_end=1091
  _BATCHALLOCATEARTIFACTPARTRESPONSE_RESULTSBYARTIFACTIDENTRY._serialized_start=994
  _BATCHALLOCATEARTIFACTPARTRESPONSE_RESULTSBYARTIFACTIDENTRY._serialized_end=1091
# @@protoc_insertion_point(module_scope)