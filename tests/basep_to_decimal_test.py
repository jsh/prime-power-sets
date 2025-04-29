import pytest
from identical_means import basep_to_decimal

def test_basep_to_decimal_valid_base3():
    assert basep_to_decimal("120", 3) == 15


def test_basep_to_decimal_valid_base10():
    assert basep_to_decimal("120", 10) == 120


def test_basep_to_decimal_valid_base16():
    assert basep_to_decimal("1A", 16) == 26


def test_basep_to_decimal_invalid_char():
    assert basep_to_decimal("123", 2) is None


def test_basep_to_decimal_empty_string():
    assert basep_to_decimal("", 5) is None


def test_basep_to_decimal_invalid_input_type():
    assert basep_to_decimal(123, 5) is None


def test_basep_to_decimal_zero():
    assert basep_to_decimal("0", 5) == 0


def test_basep_to_decimal_large_base():
    assert basep_to_decimal("10", 36) == 36