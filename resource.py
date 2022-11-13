"""
An inventory application for a budding tech guy who has a video channel featuring computer builds.
"""

from utilities.validators import validate_int, validate_str


class Resource:
    """
    The base class and provide functionality common to all the actual resources:
    (CPU, GPU, Memory, HDD, SSD)
    """

    def __init__(self, name: str, mfr: str, total: int, allocated: int):

        self._name = validate_str(name)
        self._mfr = validate_str(mfr)

        self._total = validate_int('total', total, min_value=1)
        self._allocated = validate_int('allocated', allocated, min_value=0, max_value=self._total)

        self._available = self._total - self._allocated

    @property
    def name(self) -> str:
        """

        :return: name of resource
        """
        return self._name

    @property
    def mfr(self) -> str:
        """

        :return: manufacturer name of resource
        """
        return self._mfr

    @property
    def total(self) -> int:
        """

        :return: total number of resources
        """
        return self._total

    @property
    def allocated(self) -> int:
        """

        :return: number of allocated resources
        """
        return self._allocated

    @property
    def category(self) -> str:
        """

        :return: category name of resource
        """
        return type(self).__name__.lower()

    @property
    def available(self) -> int:
        """

        :return: number of resources ready for use
        """
        return self.total - self.allocated

    @staticmethod
    def _validate_str(value: str):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f"{value} cannot be empty.")
        else:
            return str(value).strip()

    @staticmethod
    def _validate_int(value: int):
        if isinstance(value, int) and value >= 0:
            return value
        else:
            raise ValueError(f'{value} must be positive int value.')

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(name: {self._name}, mfr: {self._mfr})'

    def __str__(self):
        return f'({self._mfr}:{self._name}, {self._total}/{self._allocated})'

    def claim(self, value: int) -> None:
        """
        Claim a resource for use if available

        :param value: number of resources to be used
        :return: None
        """
        validate_int('Claim', value, min_value=1, max_value=self.available)
        self._allocated += value

    def free_up(self, value) -> None:
        """
        Release an used resource and add to an inventory

        :param value: number of released resources
        :return: None
        """
        validate_int('Free-up', value, min_value=1, max_value=self.allocated)
        self._allocated -= value

    def died(self, value) -> None:
        """
        Remove a faulty resource from an inventory

        :param value: number of died resources
        :return: None
        """
        validate_int('Died', value, min_value=1, max_value=self.allocated)
        self.free_up(value)
        self._total -= value

    def purchase(self, value) -> None:
        """
        Add new resources to the inventory
        :param value: number of new resources to be added
        :return: None
        """
        self._total += validate_int('Purchase', value, min_value=1)

