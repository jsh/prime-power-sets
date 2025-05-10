from identical_means import decimal_to_binary_string

import pytest


def test_decimal_to_binary_string_positive():
    assert decimal_to_binary_string(10) == "1010"
    assert decimal_to_binary_string(7) == "111"
    assert decimal_to_binary_string(1) == "1"


def test_decimal_to_binary_string_zero():
    assert decimal_to_binary_string(0) == "0"


def test_decimal_to_binary_string_negative():
    with pytest.raises(ValueError, match=r"^Input must be a non-negative integer.$"):
        decimal_to_binary_string(-5)
        
        
def test_decimal_to_binary_string_invalid_input():
    with pytest.raises(ValueError, match=r"^Input must be an integer.$"):
        decimal_to_binary_string("abc")
    with pytest.raises(ValueError, match=r"^Input must be an integer.$"):
        decimal_to_binary_string(3.14)
