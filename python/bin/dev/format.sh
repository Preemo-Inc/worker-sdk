#!/bin/bash
set -x

isort src
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place --ignore-init-module-imports src
black src
