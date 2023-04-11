import os
from typing import Final, Optional


def _get_optional_string_env(name: str) -> Optional[str]:
    value = os.getenv(key=name)
    if value is None or len(value) == 0:
        return None

    return value


def _get_optional_int_env(name: str) -> Optional[int]:
    value = _get_optional_string_env(name)
    if value is None:
        return None

    try:
        return int(value)
    except ValueError:
        raise Exception(f"expected int for env variable: {name}")


def _get_optional_bool_env(name: str) -> Optional[bool]:
    value = _get_optional_string_env(name)
    if value is None:
        return None

    lower_value = value.lower()
    if lower_value == "true":
        return True

    if lower_value == "false":
        return False

    raise Exception(f"expected bool for env variable: {name}")


def _get_required_string_env(name: str) -> str:
    value = _get_optional_string_env(name)
    if value is None:
        raise Exception(f"missing required env variable: {name}")

    return value


def _get_required_int_env(name: str) -> int:
    value = _get_optional_int_env(name)
    if value is None:
        raise Exception(f"missing required env variable: {name}")

    return value


def _get_required_bool_env(name: str) -> bool:
    value = _get_optional_bool_env(name)
    if value is None:
        raise Exception(f"missing required env variable: {name}")

    return value


class EnvManager:
    is_development: Final = _get_optional_bool_env("PREEMO_IS_DEVELOPMENT")
    max_download_threads: Final = _get_optional_int_env("PREEMO_MAX_DOWNLOAD_THREADS")
    max_upload_threads: Final = _get_optional_int_env("PREEMO_MAX_UPLOAD_THREADS")
    sdk_server_host: Final = _get_optional_string_env("PREEMO_SDK_SERVER_HOST")
    worker_server_url: Final = _get_optional_string_env("PREEMO_WORKER_SERVER_URL")
