import json_parser
serializers = {
    "json": json_parser.JsonParser,
    #"yaml": YamlParser,
    #"toml": TomlParser,
    #"pickle": PickleParser
}


class Factory(object):
    @staticmethod
    def create_serializer(file_format: str):
        serializer = serializers.get(file_format.lower(), None)
        return serializer
