#!/bin/bash
set -e

if [[ "${0}" != *"bin/dev/publish_package.sh" ]] || [[ "$(basename $(pwd))" != "python" ]]; then
  echo "script must be run from the subrepo root: worker-sdk/python"
  exit 1
fi

pytest tests
rm -rf dist
python3 -m build

# must have valid ~/.pypirc file to upload
python3 -m twine upload \
  --non-interactive \
  dist/*
