"""
Test definitions for validators module
"""

import pytest
from utilities.validators import validate_int, validate_str


class TestValidatorInt:
    def test_valid(self):
        validate_int('total', 10, min_value=1, max_value=10)

    def test_type_error(self):
        with pytest.raises(TypeError) as ex:
            validate_int('total', 10.0, min_value=1, max_value=10)
        assert 'total' in str(ex.value)
        assert '10.0' in str(ex.value)

    def test_value_min_error(self):
        with pytest.raises(ValueError):
            validate_int('total', -10, min_value=1, max_value=10)

    def test_value_max_error(self):
        with pytest.raises(ValueError):
            validate_int('total', 20, min_value=1, max_value=10)


class TestValidatorStr:
    def test_valid(self):
        res = validate_str('intel')
        assert res == 'Intel'

    @pytest.mark.parametrize(
        'argument', (None, 23)
    )
    def test_type_error(self, argument):
        with pytest.raises(TypeError) as er:
            validate_str(argument)

    def test_value_error(self):
        with pytest.raises(ValueError):
            validate_str('')


