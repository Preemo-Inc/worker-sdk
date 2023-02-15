import pytest

from preemo.worker._env import get_optional_env, get_required_env


class TestGetOptionalEnv:
    # before each
    @pytest.fixture(autouse=True)
    def setup_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("MOCK_VAR", "anything")

    def test_retrieves_correct_value(self) -> None:
        value = get_optional_env("MOCK_VAR")
        assert value == "anything"

    def test_returns_none_when_missing(self) -> None:
        value = get_optional_env("unknown")
        assert value is None


class TestGetRequiredEnv:
    # before each
    @pytest.fixture(autouse=True)
    def setup_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("MOCK_VAR", "anything")

    def test_retrieves_correct_value(self) -> None:
        value = get_required_env("MOCK_VAR")
        assert value == "anything"

    def test_raises_exception_when_missing(self) -> None:
        with pytest.raises(Exception, match="missing required env variable"):
            get_required_env("unknown")
