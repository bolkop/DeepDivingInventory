"""
Test definitions for storage module
"""

import pytest
from storage import Storage, HDD, SSD


@pytest.fixture
def storage_values():
    return {
        'name': 'I5',
        'mfr': 'Intel',
        'total': 10,
        'allocated': 5,
        'capacity_GB': 120
    }


@pytest.fixture
def hdd_values():
    return {
        'name': 'I5',
        'mfr': 'Intel',
        'total': 10,
        'allocated': 5,
        'capacity_GB': 120,
        'size': 3.5,
        'rpm': 7200
    }


@pytest.fixture
def ssd_values():
    return {
        'name': 'I5',
        'mfr': 'Intel',
        'total': 10,
        'allocated': 5,
        'capacity_GB': 120,
        'interface': 'SATA'
    }

@pytest.fixture
def storage(storage_values):
    yield Storage(**storage_values)


def test_init_storage(storage, storage_values):
    assert storage.capacity_GB == storage_values['capacity_GB']


def test_init_hdd(storage, hdd_values):
    hdd = HDD(**hdd_values)
    for atr_name in hdd_values:
        assert getattr(hdd, atr_name) == hdd_values.get(atr_name)


def test_init_ssd(storage, ssd_values):
    sdd = SSD(**ssd_values)
    for atr_name in ssd_values:
        assert getattr(sdd, atr_name) == ssd_values.get(atr_name)
