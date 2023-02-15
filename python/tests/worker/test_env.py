import pytest

from preemo.worker._env import get_optional_env, get_required_env


class TestEnv:
    # before each
    @pytest.fixture(autouse=True)
    def setup_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("VALUE", "foo")
        monkeypatch.setenv("EMPTY_VALUE", "")

    class TestGetOptionalEnv:
        def test_reads_value(self) -> None:
            value = get_optional_env("VALUE")
            assert value == "foo"

        def test_reads_empty_value(self) -> None:
            value = get_optional_env("EMPTY_VALUE")
            assert value is None

        def test_reads_unknown_value(self) -> None:
            value = get_optional_env("UNKNOWN")
            assert value is None

    class TestGetRequiredEnv:
        def test_reads_value(self) -> None:
            value = get_optional_env("VALUE")
            assert value == "foo"

        def test_fails_to_read_empty_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                get_required_env("EMPTY_VALUE")

        def test_fails_to_read_unknown_value(self) -> None:
            with pytest.raises(Exception, match="missing required env variable"):
                get_required_env("UNKNOWN")
