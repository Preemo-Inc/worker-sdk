from typing import Callable, Optional

def register(
    outer_function: Optional[Callable] = ...,
    *,
    name: Optional[str] = ...,
    namespace: Optional[str] = ...,
) -> Callable: ...

# TODO(adrian@preemo.io, 04/06/2023): add other functions and types
