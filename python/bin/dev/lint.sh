#!/bin/bash
set -x

# TODO(adrian@preemo.io, 02/13/2023): check if these work as intended
mypy preemo src tests
black --check preemo src tests
isort --check-only preemo src tests
flake8 preemo src tests
