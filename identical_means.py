import argparse
import itertools
import sys
from collections import defaultdict
from functools import lru_cache
from typing import List, Set, Tuple

from sympy import isprime


def decimal_to_binary_string(decimal_num: int) -> str:
    """Converts a non-negative integer to its base 2 (binary) string representation.

    Args:
      decimal_num: A non-negative integer.

    Returns:
      A string containing the binary representation (e.g., "101", "1110").

      Raises:
        ValueError: If input is not a non-negative integer.
    """
    if not isinstance(decimal_num, int):
        raise ValueError("Input must be an integer.")
    if decimal_num < 0:
        raise ValueError("Input must be a non-negative integer.")
    if decimal_num == 0:
        return "0"  # Explicitly handle 0 case
    # bin() returns a string like "0b1101". We slice off the first two characters ("0b").
    return bin(decimal_num)[2:]


def basep_to_decimal(basep_string: str, p: int) -> int:
    """Converts a string representation of a base p number to its decimal (base 10) equivalent.

    Args:
      base3_string: A string containing the base p number (must only contain
                    digits '0', '1', '2', ..., 'p-1').

    Returns:
      The integer decimal equivalent of the base p string.

    Raises:
        ValueError: If input is invalid or empty.
        TypeError: If input is not a string.
    """
    if not isinstance(basep_string, str):
        raise TypeError("Input must be a string.")
    try:
        # The int() function can take a base argument.
        # int(string, base) converts the string representation in the given base
        # to a base 10 integer.
        return int(basep_string, p)
    except ValueError:
        # This error occurs if the string contains characters
        # other than '0', '1', '2', ..., 'p-1'
        # or if the string is empty.
        raise ValueError(
            f"Invalid base {p} string '{basep_string}'. Must contain only digits 0-{p - 1}."
        )


@lru_cache(maxsize=1024)
def basep_analogue(k: int, p: int) -> int:
    """
    Computes a value based on the binary representation of k, interpreted as a base-p number.
    For example, if k is 5 (binary 101) and p is 3, it interprets "101" as a base-3 number.
    """
    if p < 2:
        raise ValueError("Base 'p' must be at least 2.")
    if not isinstance(p, int):
        raise ValueError("Base 'p' must be an integer.")
    bit_string = decimal_to_binary_string(k)
    decimal_value = basep_to_decimal(bit_string, p)
    return decimal_value


def generate_bit_count_sequence(n: int, p: int) -> List[float]:
    """
    Generates a list of n floats using k / k.bit_count() via list comprehension.

    Handles k=0 as 0.0. Raises ValueError for invalid n.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")
    if not isinstance(p, int) or p < 0:
        raise ValueError("Input 'p' must be a non-negative integer.")
    # Use a conditional expression within the list comprehension for k=0
    return [0.0 if k == 0 else basep_analogue(k, p) / k.bit_count() for k in range(n)]


def find_exact_float_duplicates_with_indices(
    seq: List[float],
) -> List[Tuple[float, List[int]]]:
    """
    Finds EXACT duplicate float elements in a list and returns them with indices.
    Works correctly if duplicates have identical float representations.

    Args:
      seq: The input list, containing only float numbers.

    Returns:
      A list of tuples: (duplicate_float_value, [list_of_indices]).
    """
    if not isinstance(seq, list):
        raise TypeError("Input must be a list.")
    index_map = defaultdict(list)
    for index, value in enumerate(seq):
        if not isinstance(value, float):
            raise TypeError(
                f"All values must be float. Found {type(value)} at index {index}"
            )
        index_map[value].append(index)

    return [
        (value, indices) for value, indices in index_map.items() if len(indices) > 1
    ]


def are_disjoint(num1: int, num2: int) -> bool:
    """
    Checks if the binary representations of two integers are disjoint
    (share no '1' bits). Returns True if disjoint, False otherwise.
    """
    return (num1 & num2) == 0


def find_disjoint_pairs(s: Set[int]) -> List[Tuple[int, int]]:
    """
    Finds all pairs of disjoint integers within a given set.

    Args:
      s: A set of integers.

    Returns:
      A list of tuples, where each tuple contains a pair of
      disjoint integers from the set.
    """
    disjoint_pairs = []
    # Generate all unique pairs of size 2 from the set
    for pair in itertools.combinations(s, 2):
        num1, num2 = pair
        # Check if the pair is disjoint using the bitwise AND operator
        if are_disjoint(num1, num2):
            disjoint_pairs.append(pair)
    return disjoint_pairs


def create_parser() -> argparse.ArgumentParser:
    """Creates a parser for a non-negative size s and a prime p."""
    parser = argparse.ArgumentParser(
        description="Get a non-negative exponent-limit, 'n'  and a prime number 'p' from the command line.",
        epilog=f"Example: python {sys.argv[0]} -n 10 -p 7",
    )

    # Define the positional arguments
    # argparse handles the basic conversion to int and errors if it fails
    parser.add_argument("-p", "--prime", type=int, help="A prime number.", default=2)
    parser.add_argument(
        "-n", "--exponent-limit", type=int, help="A non-negative integer.", default=0
    )
    return parser


def get_and_validate_args() -> Tuple[int, int]:
    """Parses command line arguments and validats them.
    Returns:
      A tuple (exponent-limit, prime) where size is a non-negative integer and prime is a prime number.
    Raises:
      SystemExit: If the arguments are invalid or if help is requested.
    """
    # Create the argument parser
    parser = create_parser()
    # Parse the arguments from the command line
    args = parser.parse_args()
    # --- Custom Validation ---
    # Validate exponent-limit: Must be non-negative
    if args.exponent_limit < 0:
        parser.error(f"Exponent-limit must be a non-negative integer. Received: {args.exponent_limit}")
    # Validate p: Must be prime
    if not isprime(args.prime):
        parser.error(f"Prime must be a prime number. Received: {args.prime}")
    # --- Success ---
    return args.exponent_limit, args.prime


def main():
    lim, prime = get_and_validate_args()
    size = prime**lim
    seq = generate_bit_count_sequence(size, prime)
    dups = find_exact_float_duplicates_with_indices(seq)
    for dup in dups:
        if find_disjoint_pairs(set(dup[1])):
            print(dup)


if __name__ == "__main__":  # pragma: no cover
    main()
