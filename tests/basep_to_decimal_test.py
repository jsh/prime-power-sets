from identical_means import basep_to_decimal
import pytest


def test_basep_to_decimal_valid_base3():
    assert basep_to_decimal("120", 3) == 15


def test_basep_to_decimal_valid_base10():
    assert basep_to_decimal("120", 10) == 120


def test_basep_to_decimal_valid_base16():
    assert basep_to_decimal("1A", 16) == 26


def test_basep_to_decimal_invalid_char():
    with pytest.raises(ValueError, match=r"^Invalid base 2 string '123'. Must contain only digits 0-1.$"):
        basep_to_decimal("123", 2)


def test_basep_to_decimal_empty_string():
    with pytest.raises(ValueError, match=r"^Invalid base 5 string ''. Must contain only digits 0-4.$"):
        basep_to_decimal("", 5)


def test_basep_to_decimal_invalid_input_type():
    with pytest.raises(TypeError, match=r"^Input must be a string.$"):
        basep_to_decimal(123, 5)

def test_basep_to_decimal_zero():
    assert basep_to_decimal("0", 5) == 0


def test_basep_to_decimal_large_base():
    assert basep_to_decimal("10", 36) == 36
