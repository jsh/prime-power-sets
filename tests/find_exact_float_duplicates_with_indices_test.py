import pytest

from identical_means import find_exact_float_duplicates_with_indices


def test_find_exact_float_duplicates_with_indices_empty_list():
    assert find_exact_float_duplicates_with_indices([]) == []


def test_find_exact_float_duplicates_with_indices_no_duplicates():
    assert find_exact_float_duplicates_with_indices([1.0, 2.0, 3.0]) == []


def test_find_exact_float_duplicates_with_indices_one_duplicate():
    result = find_exact_float_duplicates_with_indices([1.0, 2.0, 1.0])
    assert len(result) == 1
    assert result[0][0] == 1.0
    assert result[0][1] == [0, 2]


def test_find_exact_float_duplicates_with_indices_multiple_duplicates():
    result = find_exact_float_duplicates_with_indices([1.0, 2.0, 1.0, 2.0, 3.0, 1.0])
    assert len(result) == 2
    assert (1.0, [0, 2, 5]) in result
    assert (2.0, [1, 3]) in result


def test_find_exact_float_duplicates_with_indices_all_same():
    result = find_exact_float_duplicates_with_indices([1.0, 1.0, 1.0, 1.0])
    assert len(result) == 1
    assert result[0][0] == 1.0
    assert result[0][1] == [0, 1, 2, 3]


def test_find_exact_float_duplicates_with_indices_mixed_types():
    # This test is expected to raise a TypeError because of the presence of non-float values
    # in the input list.
    # The error message should indicate the first non-float value encountered.
    with pytest.raises(
        TypeError, match=r"^All values must be float. Found <class 'int'> at index 1$"
    ):
        find_exact_float_duplicates_with_indices([1.0, 2, 1.0, "test", 3.0, 1.0])


def test_find_exact_float_duplicates_with_indices_large_floats():
    result = find_exact_float_duplicates_with_indices([1e10, 2e10, 1e10])
    assert len(result) == 1
    assert result[0][0] == 1e10
    assert result[0][1] == [0, 2]


def test_find_exact_float_duplicates_with_indices_negative_floats():
    result = find_exact_float_duplicates_with_indices([-1.0, -2.0, -1.0])
    assert len(result) == 1
    assert result[0][0] == -1.0
    assert result[0][1] == [0, 2]


def test_find_exact_float_duplicates_with_indices_zero_float():
    result = find_exact_float_duplicates_with_indices([0.0, 1.0, 0.0])
    assert len(result) == 1
    assert result[0][0] == 0.0
    assert result[0][1] == [0, 2]


def test_find_exact_float_duplicates_with_indices_nan():
    nan = float("nan")
    result = find_exact_float_duplicates_with_indices([nan, 1.0, nan])
    assert len(result) == 1
    assert result[0][0] != result[0][0]  # nan != nan
    assert result[0][1] == [0, 2]


def test_find_exact_float_duplicates_with_indices_inf():
    inf = float("inf")
    result = find_exact_float_duplicates_with_indices([inf, 1.0, inf])
    assert len(result) == 1
    assert result[0][0] == inf
    assert result[0][1] == [0, 2]


def test_find_exact_float_duplicates_with_indices_type_error():
    with pytest.raises(TypeError, match=r"^Input must be a list.$"):
        find_exact_float_duplicates_with_indices("not a list")
