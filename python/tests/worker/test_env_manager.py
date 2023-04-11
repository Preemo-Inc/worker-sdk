import pytest

from preemo.worker._env_manager import (
    _get_optional_int_env,
    _get_optional_string_env,
    _get_required_int_env,
    _get_required_string_env,
)


class TestEnv:
    # before each
    @pytest.fixture(autouse=True)
    def setup_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("STRING_VALUE", "foo")
        monkeypatch.setenv("INT_VALUE", "3")
        monkeypatch.setenv("EMPTY_VALUE", "")

    class TestGetOptionalStringEnv:
        def test_reads_value(self) -> None:
            value = _get_optional_string_env("STRING_VALUE")
            assert value == "foo"

        def test_reads_empty_value(self) -> None:
            value = _get_optional_string_env("EMPTY_VALUE")
            assert value is None

        def test_reads_unknown_value(self) -> None:
            value = _get_optional_string_env("UNKNOWN")
            assert value is None

    class TestGetRequiredStringEnv:
        def test_reads_value(self) -> None:
            value = _get_required_string_env("STRING_VALUE")
            assert value == "foo"

        def test_fails_to_read_empty_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_required_string_env("EMPTY_VALUE")

        def test_fails_to_read_unknown_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_required_string_env("UNKNOWN")

    class TestGetOptionalIntEnv:
        def test_reads_value(self) -> None:
            value = _get_optional_int_env("INT_VALUE")
            assert value == 3

        def test_reads_empty_value(self) -> None:
            value = _get_optional_int_env("EMPTY_VALUE")
            assert value is None

        def test_reads_unknown_value(self) -> None:
            value = _get_optional_int_env("UNKNOWN")
            assert value is None

    class TestGetRequiredIntEnv:
        def test_reads_value(self) -> None:
            value = _get_required_int_env("INT_VALUE")
            assert value == 3

        def test_fails_to_read_empty_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_required_int_env("EMPTY_VALUE")

        def test_fails_to_read_unknown_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_required_int_env("UNKNOWN")
