from lib.parsers.json_serializer import *
from lib.parsers.parser_sk import Parser


class JsonParser(Parser):

    @staticmethod
    def dumps(obj, indent=None):
        if isinstance(indent, int) and indent > 0:
            step = " " * indent
            res = serialize_json(obj, step)
            if indent < 1:
                res = res.replace("\n", "")
        else:
            res = serialize_json(obj).replace("\n", "")
        return res

    @staticmethod
    def dump(obj, fp, indent=None):
        string = JsonParser.dumps(obj, indent)
        try:
            with open(fp, "w") as file:
                file.write(string)
        except FileNotFoundError:
            raise FileNotFoundError("file doesn't exist")

    @staticmethod
    def loads(obj: str):
        idx = 0
        try:
            while obj[idx] == " " or obj[idx] == "\n":
                idx += 1
        except IndexError:
            pass
        obj, idx = deserialize_json(obj, idx)


        return obj

    @staticmethod
    def load(file):
        try:
            with open(file, "r") as file:
                data = file.read()
        except FileNotFoundError:
            raise FileNotFoundError("file doesn't exist")
        return JsonParser.loads(data)


