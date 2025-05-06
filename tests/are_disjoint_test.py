from identical_means import are_disjoint


def test_are_disjoint_disjoint():
    assert are_disjoint(5, 2)  # 101 and 010


def test_are_disjoint_not_disjoint():
    assert not are_disjoint(5, 3)  # 101 and 011


def test_are_disjoint_one_zero():
    assert are_disjoint(5, 0)  # 101 and 000


def test_are_disjoint_both_zero():
    assert are_disjoint(0, 0)  # 000 and 000


def test_are_disjoint_large_numbers_disjoint():
    assert not are_disjoint(170, 75)  # 10101010 and 01001011


def test_are_disjoint_large_numbers_not_disjoint():
    assert are_disjoint(170, 85)  # 10101010 and 01010101
