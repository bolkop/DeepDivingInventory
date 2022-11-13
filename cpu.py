"""
This is child class of Resource for CPU object
"""
from resource import Resource
from utilities.validators import validate_str, validate_int


class CPU(Resource):
    """
    Subclass of Resource to control inventory of CPU's
    """
    def __init__(self, name: str, mfr: str, total: int, allocated: int,
                 cores: int, socket: str, power_watts: int):
        """
        Args:
        :param name: Name of CPU as string
        :param mfr: Name of manufacturer as string
        :param total: Value of CPU's in the pool as integer
        :param allocated: Value of CPU's in use as integer
        :param cores: Number of cores as integer
        :param socket: Type of CPU socket as string
        :param power_watts: CPU rated power as integer
        """

        self._cores = validate_int('cores', cores, 1)
        self._socket = socket
        self._power_watts = validate_int('power', power_watts, 1)
        super().__init__(name, mfr, total, allocated)

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts


