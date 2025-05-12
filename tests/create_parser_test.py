import argparse

from identical_means import create_parser


def test_create_parser_returns_argparse_parser():
    """Test that create_parser() returns an argparse.ArgumentParser object."""
    parser = create_parser()
    assert isinstance(parser, argparse.ArgumentParser)


def test_parser_default_values():
    """Test that the parser has the correct default values for prime and size."""
    parser = create_parser()
    args = parser.parse_args([])  # Pass an empty list to get default values
    assert args.prime == 2
    assert args.exponent_limit == 0


def test_parser_accepts_prime_and_size():
    """Test that the parser correctly parses prime and size arguments."""
    parser = create_parser()
    args = parser.parse_args(["-p", "5", "-n", "10"])
    assert args.prime == 5
    assert args.exponent_limit == 10


def test_parser_prime_argument():
    """Test that the parser correctly parses the prime argument."""
    parser = create_parser()
    args = parser.parse_args(["-p", "7"])
    assert args.prime == 7


def test_parser_size_argument():
    """Test that the parser correctly parses the size argument."""
    parser = create_parser()
    args = parser.parse_args(["-n", "15"])
    assert args.exponent_limit == 15
