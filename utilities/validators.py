"""
Definition of different validators for the application
"""


def validate_int(value_name: str, value: int, min_value: int = None, max_value: int = None) -> int:
    """
    Function to verify that value is an integer and within provided range min and max (inclusive),
    if they are provided

    :param value_name: the name of the provided value
    :param value: to be validated
    :param max_value: specified maximum value
    :param min_value: specified minimum value
    :return: value if no exception raised

    raises: TypeError if value is not an integer
    raises: ValueError if value is not within specified range min and max
    """

    if not isinstance(value, int):
        raise TypeError(f'{value_name} {value} value must be integer')
    if min_value is not None and min_value > value:
        raise ValueError(f'{value_name} {value} value must be more than {min_value}')
    if max_value is not None and max_value < value:
        raise ValueError(f'{value_name} {value} value must be less or equal to {max_value}')
    return value


def validate_str(value: str) -> str:
    """
    Validate if the value is a string type
    :param value: arg to be verified
    :return: value as tring

    raises: TypeError if argument is not a string
    raises: ValueError if argument is None or without chars
    """

    if value is None:
        raise TypeError(f"Argument cannot be None.")
    if not isinstance(value, str):
        raise TypeError(f"{value} must be string.")
    if value is None or len(str(value).strip()) == 0:
        raise ValueError(f"{value} cannot be empty.")
    else:
        return str(value).strip().capitalize()


def validate_hdd_size(size: float) -> float:
    """
    Validate if size of HDD has correct value
    :param size: size of HDD
    :return: size if value is correct
    :raises ValueError if size value is not correct
    """
    sizes = ('2.5', '3.5')
    if str(size) in sizes:
        return size
    else:
        raise ValueError("HDD size should be 2.5 or 3.5 inches")


def validate_hdd_rpm(rpm: int) -> int:
    """
    Validate if rpm speed of HDD has correct value
    :param rpm: RPM of HDD
    :return: rpm if value is correct
    :raises: ValueError if rpm value is not correct
    """
    rpm_s = ('5400', '7200')
    if str(rpm) in rpm_s:
        return rpm
    else:
        raise ValueError("HDD speed should be 5400 or 7200 rpm")


