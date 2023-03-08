#!/bin/bash
set -x

brew install asdf

asdf plugin add poetry
asdf plugin add python

# python must be installed first in order for poetry to be installed correctly on M1 machines
asdf install python
asdf install
