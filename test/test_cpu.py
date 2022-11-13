"""
Test definition for CPU module
"""
import pytest

from cpu import CPU


@pytest.fixture
def cpu_values():
    return {
        'name': 'I5',
        'mfr': 'Intel',
        'total': 10,
        'allocated': 5,
        'cores': 2,
        'socket': 'sTR4',
        'power_watts': 64
    }


@pytest.fixture
def cpu(cpu_values):
    return CPU(**cpu_values)


def test_cpu(cpu, cpu_values):
    for attr_names in cpu_values:
        assert getattr(cpu, attr_names) == cpu_values.get(attr_names)


@pytest.mark.parametrize(
    'cores, errors', ((10.5, TypeError), (0, ValueError), (-1, ValueError))
)
def test_cpu_error(cpu_values, cores, errors):
    with pytest.raises(errors):
        cpu_values['cores'] = cores
        CPU(**cpu_values)
