import pytest
from identical_means import are_disjoint, find_disjoint_pairs


def test_find_disjoint_pairs_empty_set():
    assert find_disjoint_pairs(set()) == []


def test_find_disjoint_pairs_no_disjoint_pairs():
    s = {1, 3, 5}
    assert find_disjoint_pairs(s) == []


def test_find_disjoint_pairs_one_disjoint_pair():
    s = {1, 2, 3}
    assert find_disjoint_pairs(s) == [(1, 2)]


def test_find_disjoint_pairs_multiple_disjoint_pairs():
    s = {1, 2, 4, 7}
    expected_pairs = [(1, 2), (1, 4), (2, 4)]
    assert set(find_disjoint_pairs(s)) == set(expected_pairs)


def test_find_disjoint_pairs_with_zero():
    s = {0, 1, 2, 3}
    expected_pairs = [(0, 1), (0, 2), (0, 3), (1, 2)]
    assert set(find_disjoint_pairs(s)) == set(expected_pairs)