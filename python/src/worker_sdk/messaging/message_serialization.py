from src.gen.test_pb2 import TestMessage


def serialize_thing() -> None:
    tm = TestMessage()
    tm.page_number = 3
    print(tm.page_number)
    print(dir(tm))
    print(tm.SerializeToString())
    print(type(tm.SerializeToString()))
    tm2 = TestMessage()
    tm2.ParseFromString(tm.SerializeToString())

    print(tm2.page_number)


serialize_thing()
