#!/bin/bash

if [[ "${1}" == "--ci" ]]; then
  protobuf_dir=protobuf
else
  protobuf_dir=../protobuf

  if [[ "${0}" != *"bin/dev/ensure_protos_generated.sh" ]] || [[ "$(basename $(pwd))" != "python" ]]; then
    echo "script must be run from the subrepo root: worker-sdk/python"
    exit 1
  fi
fi

temp_dir=tmp
trap "rm -rf ${temp_dir}" EXIT
mkdir "${temp_dir}"

protoc --experimental_allow_proto3_optional --proto_path="${protobuf_dir}" --python_out="${temp_dir}" --pyi_out="${temp_dir}" "${protobuf_dir}"/*.proto

# ensure all generated files match expected
for file in src/gen/*_pb2.py*
do
  filename="$(basename ${file})"
  cmp --silent "src/gen/${filename}" "${temp_dir}/${filename}"
  if [ 0 -ne $? ]; then
    echo "src/gen/${filename} does not match expected generated file"
    exit 1
  fi
done

# ensure all expected files exist
for file in "${temp_dir}"/*
do
  filename="$(basename ${file})"
  if [[ ! -f "src/gen/${filename}" ]]; then
    echo "src/gen/${filename} does not exist"
    exit 1
  fi
done
