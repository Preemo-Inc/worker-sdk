import pytest

from preemo.worker.environment.manager import get_required_env


class TestGetRequiredEnv:
    # before each
    @pytest.fixture(autouse=True)
    def setup_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("MOCK_VAR", "anything")

    def test_retrieves_correct_value(self) -> None:
        value = get_required_env("MOCK_VAR")
        assert value == "anything"

    def test_raises_exception_when_missing(self) -> None:
        with pytest.raises(Exception):
            get_required_env("unknown")
