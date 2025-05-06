import pytest

from identical_means import parse_args


def test_parse_args_helpmessage(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["script_name", "--help"])
    with pytest.raises(SystemExit):
        parse_args()
    captured = capsys.readouterr()
    assert (
        "Get a non-negative integer n and a prime number p from the command line"
        in captured.out
    )
    assert "Example: python get_np.py 10 7" in captured.out
    assert "A non-negative integer." in captured.out
    assert "A prime number." in captured.out


def test_parse_args_valid_input(monkeypatch):
    monkeypatch.setattr("sys.argv", ["script_name", "10", "7"])
    n, p = parse_args()
    assert n == 10
    assert p == 7


def test_parse_args_zero_n(monkeypatch):
    monkeypatch.setattr("sys.argv", ["script_name", "0", "7"])
    n, p = parse_args()
    assert n == 0
    assert p == 7


def test_parse_args_negative_n(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["script_name", "-1", "7"])
    with pytest.raises(SystemExit):
        parse_args()
    captured = capsys.readouterr()
    assert "Argument n: Must be a non-negative integer. Received: -1" in captured.err


def test_parse_args_non_prime_p(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["script_name", "10", "4"])
    with pytest.raises(SystemExit):
        parse_args()
    captured = capsys.readouterr()
    assert "Argument p: Must be a prime number. 4 is not prime." in captured.err


def test_parse_args_invalid_number_of_arguments(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["script_name", "10"])
    with pytest.raises(SystemExit):
        parse_args()
    captured = capsys.readouterr()
    assert "error: the following arguments are required: p" in captured.err


def test_parse_args_invalid_argument_type(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["script_name", "abc", "7"])
    with pytest.raises(SystemExit):
        parse_args()
    captured = capsys.readouterr()
    assert "invalid int value: 'abc'" in captured.err
