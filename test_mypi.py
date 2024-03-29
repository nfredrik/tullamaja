import math
from assertpy import assert_that
from mypi import (
    get_pi,
)  # Make sure to replace 'your_module' with the actual module name


def test_get_pi_returns_correct_value():
    expected_pi = math.pi
    actual_pi = get_pi()
    assert (
        actual_pi == expected_pi
    ), "get_pi() should return the value of math.pi"


def test_more_stuff():
    assert True, "This test should pass"
    assert_that(1 + 1).described_as("Error this is wrong!").is_equal_to(2)
