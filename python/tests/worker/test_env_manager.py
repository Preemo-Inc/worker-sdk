import pytest

from preemo.worker._env_manager import (
    _get_optional_bool_env,
    _get_optional_int_env,
    _get_optional_string_env,
    _get_required_bool_env,
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

        monkeypatch.setenv("TRUE_VALUE1", "true")
        monkeypatch.setenv("TRUE_VALUE2", "TRUE")
        monkeypatch.setenv("FALSE_VALUE1", "false")
        monkeypatch.setenv("FALSE_VALUE2", "FALSE")

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

        def test_fails_to_read_malformed_value(self) -> None:
            with pytest.raises(Exception, match="expected int for env variable"):
                _get_optional_int_env("STRING_VALUE")

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

        def test_fails_to_read_malformed_value(self) -> None:
            with pytest.raises(Exception, match="expected int for env variable"):
                _get_required_int_env("STRING_VALUE")

    class TestGetOptionalBoolEnv:
        def test_reads_value(self) -> None:
            value = _get_optional_bool_env("TRUE_VALUE1")
            assert value

            value = _get_optional_bool_env("TRUE_VALUE2")
            assert value

            value = _get_optional_bool_env("FALSE_VALUE1")
            assert not value

            value = _get_optional_bool_env("FALSE_VALUE2")
            assert not value

        def test_reads_empty_value(self) -> None:
            value = _get_optional_bool_env("EMPTY_VALUE")
            assert value is None

        def test_reads_unknown_value(self) -> None:
            value = _get_optional_bool_env("UNKNOWN")
            assert value is None

        def test_fails_to_read_malformed_value(self) -> None:
            with pytest.raises(Exception, match="expected bool for env variable"):
                _get_optional_bool_env("INT_VALUE")

    class TestGetRequiredBoolEnv:
        def test_reads_value(self) -> None:
            value = _get_required_bool_env("TRUE_VALUE1")
            assert value

            value = _get_required_bool_env("TRUE_VALUE2")
            assert value

            value = _get_required_bool_env("FALSE_VALUE1")
            assert not value

            value = _get_required_bool_env("FALSE_VALUE2")
            assert not value

        def test_fails_to_read_empty_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_required_bool_env("EMPTY_VALUE")

        def test_fails_to_read_unknown_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_required_bool_env("UNKNOWN")

        def test_fails_to_read_malformed_value(self) -> None:
            with pytest.raises(Exception, match="expected bool for env variable"):
                _get_required_bool_env("INT_VALUE")
