from main import SimpleTypes, Factory, func
import pytest

serializer_types = ["json"]


class TestPrimitives:

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_int(self, ser_type):
        serializerTest = Factory.create_serializer(ser_type)
        assert serializerTest.loads(serializerTest.dumps(SimpleTypes.test_int)) == SimpleTypes.test_int

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_none(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_none)) == SimpleTypes.test_none

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_float(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_float)) == SimpleTypes.test_float

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_list(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_list)) == SimpleTypes.test_list

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_string(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_string)) == SimpleTypes.test_string

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_dict(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_dict)) == SimpleTypes.test_dict

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_tuple(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_tuple)) == SimpleTypes.test_tuple

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_str(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_string)) == SimpleTypes.test_string

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_fib(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        result = serializer.loads(serializer.dumps(func))
        assert result(5) == func(5)
