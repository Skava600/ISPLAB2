from lib.factory.factory_create import Factory
class TestClass1:
    a = 2

    def __init__(self):
        self.b = 10


def test_square_func():
    return TestClass1.a * TestClass1.a


def test_fact_func(n: int):
    if n == 0:
        return 1
    else:
        return n * test_fact_func(n - 1)


class SimpleTypes:
    test_none = None
    test_bool = False
    test_int = 4325
    test_float = 0.3443
    test_string = 'Some String'
    test_tuple = (1, 2, 3)

    test_list = ['Some String'[:], 12, None, (None, 14.34, 'true'[:])]
    test_set = {1, 2, 3, 4, 5}
    test_dict = {"a": 1, "b": 2.2, "c": False, "d": True, "f1": [1, 2, 3]}

serializer = Factory.create_serializer("yaml")
serializer.dump(SimpleTypes.test_list, "yamltest.yaml")