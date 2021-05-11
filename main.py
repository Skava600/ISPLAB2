from factory_create import Factory


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    test_tuple = (1, 2, 3)
    test_list = ['Some String', 12, None, (None, 14.34, 'true')]
    test_set = {1, 2, 3, 4, 5}
    test_none = None
    test_bool = False
    test_int = 4325
    test_float = 0.3443
    test_string = 'Some String'
    serializer = Factory.create_serializer("json")
    res = serializer.dumps(test_float)
    desres = serializer.loads(res)



