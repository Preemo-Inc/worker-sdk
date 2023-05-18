from preemo.worker._bytes import convert_byte_dict_to_bytes


class TestConvertByteDictToBytes:
    def test_with_mebibytes(self) -> None:
        result = convert_byte_dict_to_bytes({"MiB": 4})
        assert result == 4194304

    def test_with_gibibytes(self) -> None:
        result = convert_byte_dict_to_bytes({"GiB": 4})
        assert result == 4294967296
