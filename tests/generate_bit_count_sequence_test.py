import pytest
from identical_means import generate_bit_count_sequence

def test_generate_bit_count_sequence_valid_input():
    result = generate_bit_count_sequence(5, 2)
    assert isinstance(result, list)
    assert len(result) == 5


def test_generate_bit_count_sequence_n_is_zero():
    result = generate_bit_count_sequence(0, 3)
    assert result == []


def test_generate_bit_count_sequence_small_values():
    result = generate_bit_count_sequence(3, 2)
    assert len(result) == 3
    # Expected values depend on basep_analogue and bit_count.  Hard to check without mocking.
    # Just check types and basic properties.
    assert all(isinstance(x, float) for x in result)


def test_generate_bit_count_sequence_invalid_n():
    with pytest.raises(ValueError):
        generate_bit_count_sequence(-1, 5)


def test_generate_bit_count_sequence_large_n():
    result = generate_bit_count_sequence(10, 2)
    assert len(result) == 10


# def test_generate_bit_count_sequence_p_equals_one():
#     result = generate_bit_count_sequence(5, 1)
#     assert len(result) == 5