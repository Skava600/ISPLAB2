from factory_create import Factory


def test_fib(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    return test_fib(num - 1) + test_fib(num - 2)


def func(a):
    return a * a * a


class SimpleTypes:
    test_none = None
    test_bool = False
    test_int = 4325
    test_float = 0.3443
    test_string = 'Some String'
    test_tuple = (1, 2, 3)

    test_list = ['Some String', 12, None, (None, 14.34, 'true')]
    test_set = {1, 2, 3, 4, 5}

    test_dict = {'3': [1, 2, 3],
                 '0.23': 32,
                 'key': (5, 'info', 8)}



if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]

    class b():
        x = 10

    serializer = Factory.create_serializer("json")

    rList = [1, 2, 3, 4, 5]

    arr = bytes(rList)
    y = True
    serializer = Factory.create_serializer("json")
    res = serializer.dumps(SimpleTypes.test_tuple)
    deserealised = serializer.loads(res)
    f = open("func.json", "w")
    resfile = serializer.dump(func, f)
    res4 = serializer.dumps(arr)
    c = 4

