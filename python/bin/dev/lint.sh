#!/bin/bash
set -x

mypy preemo tests
black --check preemo tests
isort --check-only preemo tests
flake8 preemo tests
