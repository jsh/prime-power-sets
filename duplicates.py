
from collections import defaultdict

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

# Example with exact duplicates
my_float_list_exact = [1.5, 2.0, 3.75, 1.5, -0.5, 2.0, 1.5]
result_exact = find_exact_float_duplicates_with_indices(my_float_list_exact)
print(f"Input list (exact floats): {my_float_list_exact}")
print(f"Exact Duplicates: {result_exact}")
# Expected Output: [(1.5, [0, 3, 6]), (2.0, [1, 5])]
