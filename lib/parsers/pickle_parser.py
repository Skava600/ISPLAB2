import pickle
from lib.parsers.parser_sk import Parser


class PickleParser(Parser):
    @staticmethod
    def dumps(obj):
        return pickle.dumps(obj)

    @staticmethod
    def dump(obj, file="testpicke.pickle"):
        with open(file, 'wb') as f:
            pickle.dump(obj, f)

    @staticmethod
    def loads(temp_str):
        return pickle.loads(temp_str)

    @staticmethod
    def load(file="testpickle.pickle"):
        with open(file, 'rb') as f:
            result = pickle.load(f)
            return result
