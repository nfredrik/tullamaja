import math
from mypi import (
    get_pi,
)  # Make sure to replace 'your_module' with the actual module name


def test_get_pi_returns_correct_value():
    expected_pi = math.pi
    actual_pi = get_pi()
    assert (
        actual_pi == expected_pi
    ), "get_pi() should return the value of math.pi"
