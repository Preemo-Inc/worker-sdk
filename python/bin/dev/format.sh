#!/bin/bash
set -x

isort preemo tests
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place --ignore-init-module-imports preemo tests
black preemo tests
