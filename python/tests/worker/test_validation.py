import pytest

from preemo.worker._validation import ensure_keys_match


class TestEnsureKeysMatch:
    def test_does_not_raise_when_keys_match(self) -> None:
        try:
            ensure_keys_match(expected={}, actual={})
            ensure_keys_match(expected={"a": 1}, actual={"a": 2})
            ensure_keys_match(expected={"a": 1, True: 1}, actual={"a": 2, True: 2})
            ensure_keys_match(
                expected={"a": 1, True: 1, 1: 1}, actual={"a": 2, True: 2, 1: 2}
            )
        except Exception as e:
            assert False, f"raised an exception unexpectedly: {e}"

    def test_raises_exception_when_keys_do_not_match(self) -> None:
        with pytest.raises(Exception, match="unexpected keys"):
            ensure_keys_match(expected={"a": 1}, actual={"a": 2, "b": 2})

        with pytest.raises(Exception, match="missing expected keys"):
            ensure_keys_match(expected={"a": 1, "b": 1}, actual={"a": 2})

        expected = {"a": 1, "b": 1}
        actual = {"a": 2, "c": 2}
        with pytest.raises(Exception, match="unexpected keys"):
            ensure_keys_match(expected=expected, actual=actual)
        with pytest.raises(Exception, match="missing expected keys"):
            ensure_keys_match(expected=expected, actual=actual)
