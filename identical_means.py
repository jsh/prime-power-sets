import argparse
import itertools
import math
import sys
from collections import defaultdict

from sympy import isprime


def decimal_to_binary_string(decimal_num):
    """Converts a non-negative integer to its base 2 (binary) string representation.

    Args:
      decimal_num: A non-negative integer.

    Returns:
      A string containing the binary representation (e.g., "101", "1110").
      Returns None and prints an error message if the input is not a non-negative
      integer.
    """
    if not isinstance(decimal_num, int):
        print(f"Error: Input must be an integer.")
        return None

    if decimal_num < 0:
        print("Error: Input must be a non-negative integer.")
        return None

    if decimal_num == 0:
        return "0"  # Explicitly handle 0 case

    # bin() returns a string like "0b1101". We slice off the first two characters ("0b").
    binary_representation = bin(decimal_num)[2:]
    return binary_representation


def basep_to_decimal(basep_string, p):
    """Converts a string representation of a base p number to its decimal (base 10) equivalent.

    Args:
      base3_string: A string containing the base p number (must only contain
                    digits '0', '1', '2', ..., 'p-1').

    Returns:
      The integer decimal equivalent of the base p string.
      Returns None and prints an error message if the input string is not a
      valid base p number or not a string.
    """
    if not isinstance(basep_string, str):
        print(f"Error: Input must be a string.")
        return None
    try:
        # The int() function can take a base argument.
        # int(string, base) converts the string representation in the given base
        # to a base 10 integer.
        decimal_value = int(basep_string, p)
        return decimal_value
    except ValueError:
        # This error occurs if the string contains characters
        # other than '0', '1', '2', ..., 'p-1'
        # or if the string is empty.
        print(
            f"Error: Invalid base p string '{basep_string}'. String must only contain '0', '1', '2', ...', 'p-1', and cannot be empty."
        )
        return None


def basep_analogue(k, p):
    if p < 2:
        raise ValueError("Base p must be at least 2.")
    if not isinstance(p, int):
        raise ValueError("Base p must be an integer.")
    bit_string = decimal_to_binary_string(k)
    return basep_to_decimal(bit_string, p)


def generate_bit_count_sequence(n, p):
    """
    Generates a list of n floats using k / k.bit_count() via list comprehension.

    Handles k=0 as 0.0. Raises ValueError for invalid n.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")

    # Use a conditional expression within the list comprehension for k=0
    return [0.0 if k == 0 else basep_analogue(k, p) / k.bit_count() for k in range(n)]


def find_exact_float_duplicates_with_indices(seq):
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
    # Basic check if elements are floats (can be enhanced)
    # if not all(isinstance(item, float) for item in seq):
    #   raise ValueError("List must contain only floats for this scenario.")

    index_map = defaultdict(list)
    for index, value in enumerate(seq):
        # Check if value is float before using - crucial if list might be mixed despite assumption
        if isinstance(value, float):
            index_map[value].append(index)
        else:
            # Handle non-float case if the assumption might be violated
            print(
                f"Warning: Non-float value {value} encountered at index {index}. Skipping."
            )
            # Or raise ValueError("List contains non-float elements.")

    duplicates_result = [
        (value, indices) for value, indices in index_map.items() if len(indices) > 1
    ]
    return duplicates_result


def are_disjoint(num1: int, num2: int) -> bool:
    """
    Checks if the binary representations of two integers are disjoint
    (share no '1' bits). Returns True if disjoint, False otherwise.
    """
    return (num1 & num2) == 0


def find_disjoint_pairs(s: set[int]) -> list[tuple[int, int]]:
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


# def is_prime(num):
#     """Checks if a number is prime."""
#     if num < 2:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:  # Check if even (and not 2)
#         return False
#     # Check odd divisors up to the integer square root of num
#     limit = math.isqrt(
#         num
#     )  # Requires Python 3.8+; use int(math.sqrt(num)) for older versions
#     for i in range(3, limit + 1, 2):
#         if num % i == 0:
#             return False
#     return True


def parse_args():
    """Parses command line arguments for a non-negative integer n and a prime p."""
    parser = argparse.ArgumentParser(
        description="Get a non-negative integer n and a prime number p from the command line.",
        epilog="Example: python get_np.py 10 7",
    )

    # Define the positional arguments
    # argparse handles the basic conversion to int and errors if it fails
    parser.add_argument("n", type=int, help="A non-negative integer.")
    parser.add_argument("p", type=int, help="A prime number.")

    # Parse the arguments from the command line
    try:
        args = parser.parse_args()
    except SystemExit:
        # argparse handles printing help/errors if parsing itself fails (e.g., wrong number of args)
        sys.exit(1)  # Exit with a non-zero status indicating failure

    # --- Custom Validation ---

    # Validate n: Must be non-negative
    if args.n < 0:
        # parser.error prints the message and exits gracefully
        parser.error(f"Argument n: Must be a non-negative integer. Received: {args.n}")

    # Validate p: Must be prime
    if not isprime(args.p):
        parser.error(f"Argument p: Must be a prime number. {args.p} is not prime.")

    # --- Success ---
    # If we reach here, the arguments are valid
    return (args.n, args.p)


def main():
    n, p = parse_args()
    seq = generate_bit_count_sequence(n, p)
    dups = find_exact_float_duplicates_with_indices(seq)
    for dup in dups:
        if find_disjoint_pairs(dup[1]):
            print(dup)


if __name__ == "__main__":
    main()
