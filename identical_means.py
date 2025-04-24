from collections import defaultdict
import math
import sys
import itertools

import pandas as pd


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
    print(f"Error: Input must be an integer. Received type: {type(decimal_num)}")
    return None

  if decimal_num < 0:
    print("Error: Input must be a non-negative integer.")
    return None

  if decimal_num == 0:
    return "0" # Explicitly handle 0 case

  # bin() returns a string like "0b1101". We slice off the first two characters ("0b").
  binary_representation = bin(decimal_num)[2:]
  return binary_representation


def base3_to_decimal(base3_string):
  """Converts a string representation of a base 3 number to its decimal (base 10) equivalent.

  Args:
    base3_string: A string containing the base 3 number (must only contain
                  digits '0', '1', or '2').

  Returns:
    The integer decimal equivalent of the base 3 string.
    Returns None and prints an error message if the input string is not a
    valid base 3 number or not a string.
  """
  if not isinstance(base3_string, str):
      print(f"Error: Input must be a string, but received type {type(base3_string)}.")
      return None
  try:
    # The int() function can take a base argument.
    # int(string, base) converts the string representation in the given base
    # to a base 10 integer.
    decimal_value = int(base3_string, 3)
    return decimal_value
  except ValueError:
    # This error occurs if the string contains characters other than '0', '1', '2'
    # or if the string is empty.
    print(f"Error: Invalid base 3 string '{base3_string}'. String must only contain '0', '1', or '2' and cannot be empty.")
    return None


def generate_bit_count_sequence(n):
  """
  Generates a list of n floats using k / k.bit_count() via list comprehension.

  Handles k=0 as 0.0. Raises ValueError for invalid n.
  """
  if not isinstance(n, int) or n < 0:
    raise ValueError("Input 'n' must be a non-negative integer.")

  # Use a conditional expression within the list comprehension for k=0
  return [0.0 if k == 0 else k / k.bit_count() for k in range(n)]

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
          print(f"Warning: Non-float value {value} encountered at index {index}. Skipping.")
          # Or raise ValueError("List contains non-float elements.")


  duplicates_result = [(value, indices) for value, indices in index_map.items() if len(indices) > 1]
  return duplicates_result


def get_integer_simple():
    # sys.argv[0] is the script name
    # sys.argv[1] is the first argument, sys.argv[2] the second, etc.

    # Check if the expected number of arguments is provided
    if len(sys.argv) != 2: # Script name + 1 argument = 2 items
        print(f"Usage: python {sys.argv[0]} <integer>", file=sys.stderr)
        sys.exit(1) # Exit with an error code

    # Get the argument string
    argument_str = sys.argv[1]

    # Try to convert the string to an integer
    try:
        return int(argument_str)
    except ValueError:
        # Handle the case where the argument is not a valid integer
        print(f"Error: Argument '{argument_str}' is not a valid integer.", file=sys.stderr)
        sys.exit(1) # Exit with an error code
    except Exception as e:
        # Catch other potential unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

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


def main():
    n = get_integer_simple()
    seq = generate_bit_count_sequence(n)
    dups = find_exact_float_duplicates_with_indices(seq)
    for dup in dups:
      if find_disjoint_pairs(dup[1]):
        print(dup)

if __name__ == "__main__":
    main()
