from preemo.worker._bytes import convert_byte_dict_to_bytes


class TestConvertByteDictToBytes:
    def test_works_for_mebibytes(self) -> None:
        assert convert_byte_dict_to_bytes({"MiB": 4}) == 4194304

    def test_works_for_gibibytes(self) -> None:
        assert convert_byte_dict_to_bytes({"GiB": 4}) == 4294967296
