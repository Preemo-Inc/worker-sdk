# Preemo Worker SDK

[![PyPi Version](https://img.shields.io/pypi/v/preemo-worker-sdk)](https://pypi.org/project/preemo-worker-sdk/)
[![License](https://img.shields.io/github/license/Preemo-Inc/worker-sdk)](https://github.com/Preemo-Inc/worker-sdk/blob/master/python/LICENSE)

This subrepo contains the python implementation of the Preemo Worker SDK.

## Installation

```
pip install preemo-worker-sdk
```

## Usage

### Register Function

In order to register a function with Preemo workers, you can use `register` to decorate your functions.

```python
from preemo.worker import register

@register(name="some_name", namespace="dev")
def do_something(params: str):
    ...
```

Both parameters, `name` and `namespace`, are optional. If the name isn't specified, it will default to the name of the function. If the namespace isn't specified, it will default to a global namespace.

```python
@register
def do_something(params: str):
    # registers with name do_something in the global namespace
    ...
```

At the moment, only functions that take 0 or 1 string arguments will work. These functions should also either return `None` or a string.

### Execute Function

In order to execute a function that you have previously registered with Preemo workers, you can use `get_function`.

```python
from preemo.worker import get_function

do_something = get_function(name="some_name", namespace="dev")
result = do_something("params")
...
```

The second parameter, `namespace`, is optional. If the namespace isn't specified, it will default to a global namespace.

```python
# gets the function named do_something in the global namespace
do_something = get_function("do_something")
result = do_something("params")
...
```

### Parallelize Function Execution

In order to execute a function with multiple parameters in parallel, you can use `parallelize`.

```python
from preemo.worker import parallelize

do_something = get_function(name="some_name", namespace="dev")
results = parallelize(
    do_something,
    params=[
        "params1",
        "params2",
        ...
    ]
)
...
```

If your function doesn't take a parameter and you'd like to run multiple instances of it in parallel, you can use the `count` parameter.

```python
do_something = get_function(name="some_name", namespace="dev")
results = parallelize(
    do_something,
    count=10
)
...
```

<!-- TODO(adrian@preemo.io, 03/20/23): include an explanation of the result objects. They should be objects that give you access to the artifacts. -->

## Contributing

[Contribution guidelines for this project](CONTRIBUTING.md)
