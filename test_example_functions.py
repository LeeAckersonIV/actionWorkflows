import pytest
from example_functions import my_adder, my_thermo_stat, have_digits


@pytest.mark.parametrize("a,b,c", [(5, 10, 15, 30)(3, 6, 9, 18)])
def test_my_adder(a, b, c, expected):
    assert my_adder(a, b, c) == expected


@pytest.mark.parametrize(
    "temp, desired_temp, expected", [(20, 30, "Heat")(40, 10, "AC")]
)
def test_my_thermo_stat(temp, desired_temp, expected):
    assert my_thermo_stat(temp, desired_temp) == expected


@pytest.mark.parametrize(
    "s",
    [
        ("This function should identify 1 digit in this string", 1)(
            "This string does not have numerical digits", 0
        )
    ],
)
def test_have_digits(s, expected):
    assert have_digits(s) == expected
