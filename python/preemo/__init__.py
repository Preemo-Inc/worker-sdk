from importlib import metadata as _metadata

# TODO(adrian@preemo.io, 02/15/2023): revert this back
__version__ = _metadata.version("preemo_worker_sdk3")
