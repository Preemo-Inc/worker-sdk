#!/bin/bash
set -x

brew install asdf

asdf plugin add poetry
asdf plugin add protoc https://github.com/paxosglobal/asdf-protoc.git
asdf plugin add python

asdf install
