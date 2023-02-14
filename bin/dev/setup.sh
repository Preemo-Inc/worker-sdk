#!/bin/bash
set -x

if [[ "${0}" != *"bin/dev/setup.sh"  ]]; then
  echo "script must be run from the repo root"
  exit 1
fi

brew install asdf

asdf plugin add poetry
asdf plugin add python
./bin/dev/add_protoc_plugin.sh

asdf install
