from .. import HW2


def test_calculate_tax():
    assert HW2.calculate_tax(5.50) == 1, HW2.calculate_tax(5.50) + " should be 1"
