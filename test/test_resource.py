"""
Test definitions for resource module
"""

import pytest
from resource import Resource


@pytest.fixture
def resource_values():
    return{
            'name': 'I5',
            'mfr': 'Intel',
            'total': 10,
            'allocated': 5
    }


@pytest.fixture
def resource(resource_values):
    yield Resource(**resource_values)


def test_init(resource, resource_values):
    for attr_name in resource_values:
        assert getattr(resource, attr_name) == resource_values.get(attr_name)
    assert resource.category == 'resource'


@pytest.mark.parametrize(
    'total, allocated', ((10, -2), (10, 20))
)
def test_init_value_error(resource, total, allocated):
    with pytest.raises(ValueError):
        Resource('name', 'mfr', total, allocated)


def test_claim(resource):
    n = 3
    currently_allocated = resource.allocated
    resource.claim(n)
    assert resource.allocated == currently_allocated + n


@pytest.mark.parametrize('value', [10, -2])
def test_claim_value_error(resource, value):
    with pytest.raises(ValueError):
        resource.claim(value)


def test_free_up(resource):
    n = 3
    currently_allocated = resource.allocated
    resource.free_up(n)
    assert resource.allocated == currently_allocated - n


@pytest.mark.parametrize('value', [20, -2])
def test_freeup_value_error(resource, value):
    with pytest.raises(ValueError):
        resource.claim(value)


def test_died(resource):
    n = 5
    currently_total = resource.total
    currently_allocated = resource.allocated
    resource.died(n)
    assert resource.allocated == currently_allocated - n
    assert resource.total == currently_total - n


@pytest.mark.parametrize('value', [20, -2])
def test_died_value_error(resource, value):
    with pytest.raises(ValueError):
        resource.claim(value)


def test_purchase(resource):
    n = 3
    currently_total = resource.total
    currently_allocated = resource.allocated
    resource.purchase(n)
    assert resource.total == currently_total + n
    assert resource.allocated == currently_allocated


@pytest.mark.parametrize('value', [0, -2])
def test_purchase_value_error(resource, value):
    with pytest.raises(ValueError):
        resource.claim(value)



