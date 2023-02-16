# Contribution Guidelines

## Getting Started

Make sure that you have already followed the directions for installing `poetry` and `python` from the root repo.
Then run the following script:

```shell
worker-sdk/python$ ./bin/dev/setup.sh
```

To use the poetry environment, run:

```shell
worker-sdk/python$ poetry shell
```

Inside this environment, your python installation will have access to all dependencies managed by poetry.
To stop using the poetry environment, run:

```shell
worker-sdk/python$ exit
```

### Working in VSCode

In order to get this subrepo working in VSCode, you must open a new window with `worker-sdk/python` as the root of the project.

## Code Style

We will abide by the _PEP8_ style guide for enforcing our project's style conventions.
For code formatting and linting we leverage:

- autoflake - remove unused imports and variables
- black - opinionated and deterministic code formatter
- flake8 - linter
- isort - sort imports
- mypy - static type checker

Before creating a pull request you can autoformat your code by running:

```shell
worker_sdk/python$ ./bin/dev/format.sh
```

This will ensure that _most_ of your code passes the linting stage in CI.

Once you have formatted your code you can lint your code by running:

```shell
worker_sdk/python$ ./bin/dev/lint.sh
```

## Generating Protobuf Classes

In order to generate the protobuf classes, make sure that you have already followed the directions for installing `protobuf` from the root repo.
Then run the following script:

```shell
worker_sdk/python$ ./bin/dev/generate_protos.sh
```

## Publishing to PyPi

In order to publish a new version to pypi, first update `pyproject.toml` with the new version number.
Then run the following script while inside the poetry shell:

```shell
(.venv) worker_sdk/python$ ./bin/dev/publish_package.sh
```

Please note that you must have the proper credentials to publish to PyPi.
