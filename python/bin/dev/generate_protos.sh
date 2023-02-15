#!/bin/bash

if [[ "${0}" != *"bin/dev/generate_protos.sh" ]] || [[ "$(basename $(pwd))" != "python" ]]; then
  echo "script must be run from the subrepo root: worker-sdk/python"
  exit 1
fi

INIT_FILE_CONTENTS="import os
import sys

# protoc does not and will not generate relative imports for python.
# This workaround was copied from https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-429735834:
sys.path.append(os.path.dirname(__file__))"

function generateInitFiles {
  local dir="${1}"

  echo "${INIT_FILE_CONTENTS}" > "${dir}/__init__.py"

  for file in "${dir}"/*; do
    if [ -d "${file}" ]; then
      generateInitFiles "${file}"
    fi
  done
}

protobufDir="../protobuf"
genDir="preemo/gen"

rm -rf "${genDir}"
mkdir "${genDir}"

protoc \
  --proto_path "${protobufDir}" \
  --python_out "${genDir}" \
  --pyi_out "${genDir}" \
  $(find "${protobufDir}" -name "*.proto")

generateInitFiles "${genDir}"
