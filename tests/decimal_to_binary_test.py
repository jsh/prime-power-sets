from identical_means import decimal_to_binary_string


def test_decimal_to_binary_string_positive():
    assert decimal_to_binary_string(10) == "1010"
    assert decimal_to_binary_string(7) == "111"
    assert decimal_to_binary_string(1) == "1"


def test_decimal_to_binary_string_zero():
    assert decimal_to_binary_string(0) == "0"


def test_decimal_to_binary_string_negative():
    assert decimal_to_binary_string(-5) is None


def test_decimal_to_binary_string_invalid_input():
    assert decimal_to_binary_string("abc") is None
    assert decimal_to_binary_string(3.14) is None
