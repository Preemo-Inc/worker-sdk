#!/bin/bash

if [[ "${0}" != *"bin/dev/build_package.sh" ]] || [[ "$(basename $(pwd))" != "python" ]]; then
  echo "script must be run from the subrepo root: worker-sdk/python"
  exit 1
fi

rm -rf dist
python3 -m build
# TODO(adrian@preemo.io, 02/10/2023): figure out how to not have to enter username and password interactively
python3 -m twine upload --repository testpypi dist/*
