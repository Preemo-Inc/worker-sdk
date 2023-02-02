import os


def get_required_env(name: str) -> str:
    value = os.getenv(key=name)
    if value is None or len(value) == 0:
        raise Exception(f"Missing {name} env variable")

    return value
