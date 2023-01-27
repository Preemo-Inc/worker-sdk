# python worker-sdk

This subrepo contains the python implementation of the Preemo Worker SDK.

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
