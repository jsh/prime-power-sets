from identical_means import basep_analogue

def test_basep_analogue_basic():
    assert basep_analogue(5, 3) == 10


def test_basep_analogue_zero():
    assert basep_analogue(0, 5) == 0


def test_basep_analogue_large_p():
    assert basep_analogue(7, 10) == 111


def test_basep_analogue_another():
    assert basep_analogue(10, 3) == 30