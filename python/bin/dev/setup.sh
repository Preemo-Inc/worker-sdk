#!/bin/bash
set -x

cp bin/dev/env-template .env

poetry config virtualenvs.in-project true
poetry env use python
poetry env use 3.8.13
poetry install
