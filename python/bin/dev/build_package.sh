#!/bin/bash

if [[ "${0}" != *"bin/dev/build_package.sh" ]] || [[ "$(basename $(pwd))" != "python" ]]; then
  echo "script must be run from the subrepo root: worker-sdk/python"
  exit 1
fi

python3 -m build
