#!/bin/bash

if [[ "${0}" != *"bin/dev/generate_protos.sh" ]] || [[ "$(basename $(pwd))" != "python" ]]; then
  echo "script must be run from the subrepo root: worker-sdk/python"
  exit 1
fi

protobufDir="../protobuf"
genDir="preemo/gen"

protoc \
  --proto_path "${protobufDir}" \
  --python_out "${genDir}" \
  --pyi_out "${genDir}" \
  $(find "${protobufDir}" -name "*.proto")
