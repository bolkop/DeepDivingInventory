"""
This is child class of Resource for memory objects
"""

from resource import Resource
from utilities.validators import validate_int, validate_hdd_size, validate_hdd_rpm, validate_str


class Storage(Resource):
    def __init__(self, name: str, mfr: str, total: int, allocated: int, capacity_GB: int):
        self._capacity_GB = validate_int('Storage capacity', capacity_GB)
        super().__init__(name, mfr, total, allocated)

    @property
    def capacity_GB(self):
        return self._capacity_GB

    def __str__(self):
        return f'{type(self).__name__}, capacity[GB]: {self.capacity_GB}'

    def __repr__(self):
        return f'{type(self).__name__}, capacity[GB]: {self.capacity_GB}, {self.total}/{self.allocated}'


class HDD(Storage):
    def __init__(
            self, name: str,
            mfr: str,
            total: int,
            allocated: int,
            capacity_GB: int,
            size: float,
            rpm: int):
        super().__init__(name, mfr, total, allocated, capacity_GB)

        self._size = validate_hdd_size(size)
        self._rpm = validate_hdd_rpm(rpm)

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm


class SSD(Storage):
    def __init__(
            self, name: str,
            mfr: str,
            total: int,
            allocated: int,
            capacity_GB: int,
            interface: str):
        super().__init__(name, mfr, total, allocated, capacity_GB)

        self._interface = validate_str(interface).upper()

    @property
    def interface(self):
        return self._interface






