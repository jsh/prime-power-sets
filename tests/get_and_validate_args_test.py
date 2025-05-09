import pytest

from identical_means import get_and_validate_args


def test_get_and_validate_args_valid_input(monkeypatch):
    """Test that get_and_validate_args returns correct values for valid input."""
    monkeypatch.setattr("sys.argv", ["script_name.py", "-s", "10", "-p", "7"])
    s, p = get_and_validate_args()
    assert s == 10
    assert p == 7


def test_get_and_validate_args_default_values(monkeypatch):
    """Test that get_and_validate_args returns default values when no arguments are provided."""
    monkeypatch.setattr("sys.argv", ["script_name.py"])
    s, p = get_and_validate_args()
    assert s == 0
    assert p == 2


def test_get_and_validate_args_invalid_size(monkeypatch):
    """Test that get_and_validate_args raises SystemExit for negative size."""
    monkeypatch.setattr("sys.argv", ["script_name.py", "-s", "-1", "-p", "5"])
    with pytest.raises(SystemExit):
        get_and_validate_args()


def test_get_and_validate_args_invalid_prime(monkeypatch):
    """Test that get_and_validate_args raises SystemExit for non-prime prime."""
    monkeypatch.setattr("sys.argv", ["script_name.py", "-s", "10", "-p", "4"])
    with pytest.raises(SystemExit):
        get_and_validate_args()


def test_get_and_validate_args_size_as_string(monkeypatch):
    """Test that get_and_validate_args handles size given as string."""
    monkeypatch.setattr("sys.argv", ["script_name.py", "-s", "20", "-p", "5"])
    s, p = get_and_validate_args()
    assert s == 20
    assert p == 5


def test_get_and_validate_args_prime_as_string(monkeypatch):
    """Test that get_and_validate_args handles prime given as string."""
    monkeypatch.setattr("sys.argv", ["script_name.py", "-s", "10", "-p", "11"])
    s, p = get_and_validate_args()
    assert s == 10
    assert p == 11
