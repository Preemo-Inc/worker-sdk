from typing import Callable, Dict, Optional


class PreemoWorkerClient:
    _default_namespace = "global"

    def __init__(self) -> None:
        self._registered_functions_by_namespace_and_name: Dict[
            str, Dict[str, Callable]
        ] = {}

    # TODO(adrian@preemo.io, 02/03/2023): add documentation to the readme explaining how to correctly use this method
    # explain that name must be included if namespace is?
    # explain how to correctly "nest" decorators
    def register(
        self,
        function: Optional[Callable] = None,
        *,
        name: Optional[str] = None,
        namespace: Optional[str] = None,
    ) -> Callable:
        if function is None:
            # caller must have used @register(...)
            if name is None:
                raise ValueError(
                    "name must be specified when calling register explicitly"
                )

            if namespace is None:
                namespace = PreemoWorkerClient._default_namespace

            # TODO(adrian@preemo.io, 02/03/2023): consider trimming and validating string length

        else:
            # caller must have used @register
            if name is not None:
                raise Exception("expected name to be None")

            if namespace is not None:
                raise Exception("expected namespace to be None")

            name = function.__name__
            namespace = PreemoWorkerClient._default_namespace

        # TODO(adrian@preemo.io, 02/03/2023): register function here
        print(f"registering function with namespace: {namespace} and name: {name}")

        if function is None:
            return lambda x: x

        return function


client = PreemoWorkerClient()

# all public methods of PreemoWorkerClient should be added below for ease of use
register = client.register

# TODO(adrian@preemo.io, 02/03/2023): write tests including the following syntaxes
# @register
# @register()
# @register(name=blah)
# @register(namespace=blah)
# @register(name=boo, namespace=blah)
# nested decorators for all these cases
