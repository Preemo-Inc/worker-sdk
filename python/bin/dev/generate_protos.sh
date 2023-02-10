#!/bin/bash

if [[ "${0}" != *"bin/dev/generate_protos.sh" ]] || [[ "$(basename $(pwd))" != "python" ]]; then
  echo "script must be run from the subrepo root: worker-sdk/python"
  exit 1
fi

protoc --proto_path src/gen=../protobuf --python_out=. --pyi_out=. $(find ../protobuf -iname "*.proto")