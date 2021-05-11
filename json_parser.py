from parser_sk import Parser
from json_serializer import *
from serializer import Serializer


class JsonParser(Parser):
    @staticmethod
    def dumps(obj) -> str:
        obj = Serializer.serialize_object(obj)
        return serialize_json(obj).replace("\n", "\\n")

    @staticmethod
    def dump(obj, file):
        file.write(JsonParser.dumps(obj))

    @staticmethod
    def loads(obj: str):
        obj = deserialize_json(obj.replace("\\n", "\n"))
        return Serializer.deserialize_object(obj)

    @staticmethod
    def load(file):
        return JsonParser.loads(file.read())

