from lib.parsers import toml_parser, yaml_parser, json_parser, pickle_parser

serializers = {
    "json": json_parser.JsonParser,
    "yaml": yaml_parser.YamlParser,
    "toml": toml_parser.TomlParser,
    "pickle": pickle_parser.PickleParser
}


class Factory(object):
    @staticmethod
    def create_serializer(file_format: str):
        serializer = serializers.get(file_format.lower(), None)
        return serializer
