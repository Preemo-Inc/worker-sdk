from src.gen.test_pb2 import TestMessage


def serialize_thing() -> None:
    tm = TestMessage()
    # print(tm.HasField("page_number"))
    tm.SerializeToString()
    tm.page_number = 3
    tm.query = "abc"
    print(tm.ByteSize())
    tm.SerializeToString()


serialize_thing()
