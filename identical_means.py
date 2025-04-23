from collections import defaultdict
import math


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

# --- Example Usage ---

# Generate a sequence of length 10
n_elements = 100
sequence = generate_bit_count_sequence(n_elements)
result_exact = find_exact_float_duplicates_with_indices(sequence)
print(f"Exact Duplicates: {result_exact}")
