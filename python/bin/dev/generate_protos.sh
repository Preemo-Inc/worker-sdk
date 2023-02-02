#!/bin/bash

if [[ "${0}" != *"bin/dev/generate_protos.sh" ]] || [[ "$(basename $(pwd))" != "python" ]]; then
  echo "script must be run from the subrepo root: worker-sdk/python"
  exit 1
fi

protoc --proto_path=../protobuf --python_out=src/gen --pyi_out=src/gen ../protobuf/*.proto
# TODO(adrian@preemo.io, 02/01/2023): add build step that ensure that the generated files match what is expected?
