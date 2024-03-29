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
def do_something(params: bytes):
    ...
```

Both parameters, `name` and `namespace`, are optional. If the name isn't specified, it will default to the name of the function. If the namespace isn't specified, it will default to a global namespace.

```python
@register
def do_something(params: str):
    # registers with name do_something in the global namespace
    ...
```

At the moment, only functions that take 0 or 1 `bytes` arguments will work. These functions should also either return `None` or `bytes`.

#### Resource Requirements

If your function has particular resource requirements, you should specify those during registration.

For example, if your function needs 4 cpu cores to run effectively, you can pass a configuration object.

```python
from preemo.worker import register

@register(name="some_name", namespace="dev", cpu_cores=4)
def do_something(params: bytes):
    ...
```

You can specify the memory and/or storage requirments in either Mebibytes (`MiB`) or Gibibytes (`GiB`).

```python
from preemo.worker import register

@register(name="some_name", namespace="dev", memory={ "MiB": 100 }, storage={ "GiB": 10 })
def do_something(params: bytes):
    ...
```

If you need GPUs to effectively run your function, you may pass the specific model to use.

```python
from preemo.worker import register

@register(name="some_name", namespace="dev", gpu_model="nvidia-tesla-k80")
def do_something(params: bytes):
    ...
```

Along with a gpu model, you may pass a number of gpu devices needed.

```python
from preemo.worker import register

@register(name="some_name", namespace="dev", gpu_model="nvidia-tesla-k80", gpu_count=2)
def do_something(params: bytes):
    ...
```

<!-- TODO(adrian@preemo.io, 06/01/2023): Include a list of supported gpu models -->

### Execute Function

In order to execute a function that you have previously registered with Preemo workers, you can use `get_function`.

```python
from preemo.worker import get_function

do_something = get_function(name="some_name", namespace="dev")
result = do_something(b"params")
...
```

The second parameter, `namespace`, is optional. If the namespace isn't specified, it will default to a global namespace.

```python
# gets the function named do_something in the global namespace
do_something = get_function("do_something")
result = do_something(b"params")
...
```

### Parallel Function Execution

In order to execute a function with multiple parameters at the same time, you can use `parallel`.

```python
from preemo.worker import get_function, parallel

do_something = get_function(name="some_name", namespace="dev")
results = parallel(
    do_something,
    params=[
        b"params1",
        b"params2",
        ...
    ]
)
...
```

If your function doesn't take a parameter and you'd like to run multiple instances of it in parallel, you can use the `count` parameter.

```python
do_something = get_function(name="some_name", namespace="dev")
results = parallel(
    do_something,
    count=10
)
...
```

### Results

In order to view the result of an executed function, you can call `.get()`.

```python
from preemo.worker import get_function

do_something = get_function(name="some_name", namespace="dev")
result = do_something(b"params")
value = result.get()
...
```

## Contributing

[Contribution guidelines for this project](CONTRIBUTING.md)
