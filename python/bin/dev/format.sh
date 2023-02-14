#!/bin/bash
set -x

# TODO(adrian@preemo.io, 02/13/2023): test if these commands work
isort preemo src tests
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place --ignore-init-module-imports preemo src tests
black preemo src tests
