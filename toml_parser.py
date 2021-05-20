import toml
from parser_sk import Parser


class TomlParser(Parser):
    @staticmethod
    def dumps(obj) -> str:
        return toml.dumps(obj)

    @staticmethod
    def dump(obj, file):
        file.write(TomlParser.dumps(obj))

    @staticmethod
    def loads(obj: str):
        return toml.loads(obj)

    @staticmethod
    def load(file):
        return TomlParser.loads(file.read())
