from parser_sk import Parser
from yaml import dump as dumps, full_load as loads


class YamlParser(Parser):
    @staticmethod
    def dumps(obj) -> str:
        return dumps(obj)

    @staticmethod
    def dump(obj, file):
        file.write(YamlParser.dumps(obj))

    @staticmethod
    def loads(obj: str):
        return loads(obj)

    @staticmethod
    def load(file):
        return YamlParser.loads(file.read())