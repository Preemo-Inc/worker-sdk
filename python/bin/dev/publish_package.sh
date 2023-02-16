#!/bin/bash
set -e

if [[ "${0}" != *"bin/dev/publish_package.sh" ]] || [[ "$(basename $(pwd))" != "python" ]]; then
  echo "script must be run from the subrepo root: worker-sdk/python"
  exit 1
fi

# TODO(adrian@preemo.io, 02/15/2023): consider adding link to pypi env file
if [ -f pypi.env ]; then
  source pypi.env
fi

if [ -z "${PYPI_USERNAME}" ] || [ -z "${PYPI_PASSWORD}" ]; then
  echo "missing at least one required env variable: PYPI_USERNAME, PYPI_PASSWORD"
  exit 1
fi

pytest tests
rm -rf dist
python3 -m build

# TODO(adrian@preemo.io, 02/15/2023): remove the repository line
python3 -m twine upload \
  --username "${PYPI_USERNAME}" \
  --password "${PYPI_PASSWORD}" \
  --repository testpypi \
  dist/*
