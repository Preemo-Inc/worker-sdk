#!/bin/bash
set -x

# asdf v0.10.0 was unable to install nodejs, so we are manually pinning the version to v0.8.1
# TODO(adrian@preemo.io, 2/01/2023): check asdf version and only uninstall if not v0.8.1
#brew uninstall asdf
#brew install --formula --build-from-source ./bin/dev/asdf.rb
brew install asdf

asdf plugin add poetry
asdf plugin add python

# asdf v0.8.1 has some bug that where `asdf install` won't install python
# adding `asdf install python` seems to fix the issue
#asdf install python
#asdf install

