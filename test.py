from main import *
import pytest

serializer_types = ["json", "yaml", "pickle"]
toml = ["toml"]


class TestPrimitive:

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_int(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_int)) == SimpleTypes.test_int

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_none(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_none)) == SimpleTypes.test_none

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_float(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_float)) == SimpleTypes.test_float

    @pytest.mark.parametrize('ser_type', serializer_types + toml)
    def test_list(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_list)) == SimpleTypes.test_list

    @pytest.mark.parametrize('ser_type', serializer_types + toml)
    def test_string(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_string)) == SimpleTypes.test_string

    @pytest.mark.parametrize('ser_type', serializer_types + toml)
    def test_dict(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_dict)) == SimpleTypes.test_dict

    @pytest.mark.parametrize('ser_type', serializer_types + toml)
    def test_tuple(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_tuple)) == SimpleTypes.test_tuple

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_str(self, ser_type):
        serializer = Factory.create_serializer(ser_type)
        assert serializer.loads(serializer.dumps(SimpleTypes.test_string)) == SimpleTypes.test_string


class TestFunctions:
    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_fact(self, ser_type):
        p = Factory.create_serializer(ser_type)
        temp = p.dumps(test_fact_func)
        res = p.loads(temp)
        assert res(5) == test_fact_func(5)

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_square(self, ser_type):
        p = Factory.create_serializer(ser_type)
        temp = p.dumps(test_square_func)
        res = p.loads(temp)
        assert res() == test_square_func()

class TestClass1:
    @pytest.mark.parametrize('ser_type', serializer_types + toml)
    def test_class1(self, ser_type):
        p = Factory.create_serializer(ser_type)
        temp = p.dumps(TestClass1)
        res = p.loads(temp)
        assert res.a == TestClass1.a



