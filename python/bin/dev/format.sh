#!/bin/bash
set -x

isort preemo tests
black preemo tests
autoflake preemo tests
