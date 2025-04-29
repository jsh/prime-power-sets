from identical_means import are_disjoint

def test_are_disjoint_disjoint():
    assert are_disjoint(5, 2) == True  # 101 and 010

def test_are_disjoint_not_disjoint():
    assert are_disjoint(5, 3) == False  # 101 and 011

def test_are_disjoint_one_zero():
    assert are_disjoint(5, 0) == True

def test_are_disjoint_both_zero():
    assert are_disjoint(0, 0) == True

def test_are_disjoint_large_numbers_disjoint():
    assert are_disjoint(170, 75) == False  # 10101010 and 01001011

def test_are_disjoint_large_numbers_not_disjoint():
    assert are_disjoint(170, 85) == True # 10101010 and 01010101