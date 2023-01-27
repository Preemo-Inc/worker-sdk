#!/bin/bash
set -x

mypy src
black --check src
isort --check-only src
flake8 src
