from typing import Callable, Optional


def register(
    function: Optional[Callable] = None, *, name: Optional[str] = None
) -> Callable:
    # TODO(adrian@preemo.io, 02/01/2023): handle namespace as well
    if function is None:
        if name is None:
            raise ValueError("name must be specified")

        function_name = name
    else:
        if name is not None:
            # TODO(adrian@preemo.io, 02/01/2023): clean error messaging
            raise ValueError("did not expect name")

        function_name = function.__name__

    # TODO(adrian@preemo.io, 02/01/2023): do the registering here
    print(f"registering func_name: {function_name}")

    # def decorator_register(func: Callable) -> Callable:
    #     @functools.wraps(func)
    #     # TODO(adrian@preemo.io, 02/01/2023): can i clean up these types?
    #     def wrapper_decorator(*args: Any, **kwargs: Any) -> Any:
    #         # Do something before
    #         value = func(*args, **kwargs)
    #         # Do something after
    #         return value

    #     return wrapper_decorator

    if function is None:
        return lambda x: x
    else:
        return function


@register
def say_whee() -> None:
    print("Whee!")


@register(name="blah")
def say_whee2() -> None:
    print("Whee!")


say_whee()
say_whee2()
