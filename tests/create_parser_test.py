import argparse
import sys

from identical_means import create_parser
import pytest


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
    """Test that the parser correctly handles both prime and size arguments."""
    parser = create_parser()
    args = parser.parse_args(["-p", "5", "-n", "10"])
    assert args.prime == 5
    assert args.exponent_limit == 10


def test_parser_prime_argument():
    """Test that the parser correctly parses the prime argument by itself."""
    parser = create_parser()
    args = parser.parse_args(["-p", "7"])
    assert args.prime == 7
    assert args.exponent_limit == 0



def test_parser_size_argument():
    """Test that the parser correctly parses the size argument by itself."""
    parser = create_parser()
    args = parser.parse_args(["-n", "15"])
    assert args.exponent_limit == 15
    
def test_parser_description():
    """Test that the parser has the correct description."""
    parser = create_parser()
    assert parser.description is not None
    assert isinstance(parser.description, str)
    assert parser.description == "Get a non-negative exponent-limit, 'n'  and a prime number 'p' from the command line."


def test_parser_epilog():
    """Test that the parser has the correct epilog."""
    parser = create_parser()
    assert parser.epilog is not None
    assert isinstance(parser.epilog, str)
    assert parser.epilog == f"Example: python {sys.argv[0]} -n 10 -p 7"


def test_parser_help_message():
    """Test that the parser provides a help message."""
    parser = create_parser()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parser.parse_args(["-h"])
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_prime_help_message():
    """Test that the prime argument has a help message."""
    parser = create_parser()
    help_text = parser.format_help()
    assert "-p PRIME" in help_text

def test_exponent_limit_help_message():
    """Test that the exponent_limit argument has a help message."""
    parser = create_parser()
    help_text = parser.format_help()
    assert "-n EXPONENT_LIMIT" in help_text
