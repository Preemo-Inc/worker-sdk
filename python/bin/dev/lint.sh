#!/bin/bash
set -x

mypy preemo tests
isort --check-only preemo tests
black --check preemo tests
flake8 preemo tests
