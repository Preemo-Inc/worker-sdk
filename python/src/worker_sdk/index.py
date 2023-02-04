from typing import Callable, Dict


class PreemoWorkerClient:
    def __init__(self) -> None:
        self._registered_functions_by_namespace_and_name: Dict[
            str, Dict[str, Callable]
        ] = {}
