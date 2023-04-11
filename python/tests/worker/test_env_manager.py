import pytest

from preemo.worker._env_manager import (
    _get_bool_env,
    _get_int_env,
    _get_positive_int_env,
    _get_string_env,
)


class TestEnv:
    # before each
    @pytest.fixture(autouse=True)
    def setup_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("EMPTY_VALUE", "")
        monkeypatch.setenv("STRING_VALUE", "foo")

        monkeypatch.setenv("INT_VALUE", "3")
        monkeypatch.setenv("NEGATIVE_INT_VALUE", "-3")

        monkeypatch.setenv("TRUE_VALUE1", "true")
        monkeypatch.setenv("TRUE_VALUE2", "TRUE")
        monkeypatch.setenv("FALSE_VALUE1", "false")
        monkeypatch.setenv("FALSE_VALUE2", "FALSE")

    class TestGetStringEnv:
        def test_reads_value(self) -> None:
            value = _get_string_env("STRING_VALUE")
            assert value == "foo"

        def test_reads_empty_value(self) -> None:
            value = _get_string_env("EMPTY_VALUE")
            assert value is None

        def test_reads_unknown_value(self) -> None:
            value = _get_string_env("UNKNOWN")
            assert value is None

    class TestGetIntEnv:
        def test_reads_value(self) -> None:
            value = _get_int_env("INT_VALUE")
            assert value == 3

            value = _get_int_env("INT_VALUE", default=10)
            assert value == 3

        def test_reads_empty_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_int_env("EMPTY_VALUE")

            value = _get_int_env("EMPTY_VALUE", default=10)
            assert value == 10

        def test_reads_unknown_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_int_env("UNKNOWN")

            value = _get_int_env("UNKNOWN", default=10)
            assert value == 10

        def test_fails_to_read_malformed_value(self) -> None:
            with pytest.raises(Exception, match="expected int for env variable"):
                _get_int_env("STRING_VALUE")

    class TestGetPositiveIntEnv:
        def test_reads_value(self) -> None:
            value = _get_positive_int_env("INT_VALUE")
            assert value == 3

            value = _get_positive_int_env("INT_VALUE", default=10)
            assert value == 3

        def test_reads_empty_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_positive_int_env("EMPTY_VALUE")

            value = _get_positive_int_env("EMPTY_VALUE", default=10)
            assert value == 10

        def test_reads_unknown_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_positive_int_env("UNKNOWN")

            value = _get_positive_int_env("UNKNOWN", default=10)
            assert value == 10

        def test_fails_to_read_malformed_value(self) -> None:
            with pytest.raises(Exception, match="expected int for env variable"):
                _get_positive_int_env("STRING_VALUE")

            with pytest.raises(
                Exception, match="expected positive int for env variable"
            ):
                _get_positive_int_env("NEGATIVE_INT_VALUE")

    class TestGetBoolEnv:
        def test_reads_value(self) -> None:
            value = _get_bool_env("TRUE_VALUE1")
            assert value

            value = _get_bool_env("TRUE_VALUE2")
            assert value

            value = _get_bool_env("FALSE_VALUE1")
            assert not value

            value = _get_bool_env("FALSE_VALUE2")
            assert not value

        def test_ignores_default_if_present(self) -> None:
            value = _get_bool_env("TRUE_VALUE1", default=False)
            assert value

            value = _get_bool_env("TRUE_VALUE2", default=False)
            assert value

            value = _get_bool_env("FALSE_VALUE1", default=True)
            assert not value

            value = _get_bool_env("FALSE_VALUE2", default=True)
            assert not value

        def test_reads_empty_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_bool_env("EMPTY_VALUE")

            value = _get_bool_env("EMPTY_VALUE", default=True)
            assert value

        def test_reads_unknown_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                _get_bool_env("UNKNOWN")

            value = _get_bool_env("UNKNOWN", default=True)
            assert value

        def test_fails_to_read_malformed_value(self) -> None:
            with pytest.raises(Exception, match="expected bool for env variable"):
                _get_bool_env("INT_VALUE")
