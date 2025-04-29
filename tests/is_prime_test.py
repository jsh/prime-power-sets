import pytest
from identical_means import is_prime

def test_is_prime_basic():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True

def test_is_prime_non_prime():
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(12) == False

def test_is_prime_edge_cases():
    assert is_prime(0) == False
    assert is_prime(1) == False

def test_is_prime_large_prime():
    assert is_prime(104729) == True  # A known large prime

def test_is_prime_large_non_prime():
    assert is_prime(104730) == False # A known large non-prime