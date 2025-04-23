import itertools
import pandas as pd

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

# --- Example Usage ---

# Define the input set of integers
S = {10, 5, 12, 3, 6, 1, 8, 9}
# Binary representations for reference:
# 10: 1010
#  5: 0101  (Disjoint with 10)
# 12: 1100
#  3: 0011  (Disjoint with 12)
#  6: 0110
#  1: 0001  (Disjoint with 6, 8, 10, 12)
#  8: 1000  (Disjoint with 1, 3, 5, 6)
#  9: 1001  (Disjoint with 6)

print(f"Input Set S: {S}")

# Find all disjoint pairs in the set S
found_pairs = find_disjoint_pairs(S)

print("\nFound Disjoint Pairs:")
if not found_pairs:
  print("No disjoint pairs found in the set.")
else:
  # For better visualization, let's show binary representations too
  results_data = []
  for pair in found_pairs:
      num1, num2 = pair
      results_data.append({
          'Pair': pair,
          'Num1 Binary': f"{num1:b}", # Show binary without '0b' prefix
          'Num2 Binary': f"{num2:b}",
          'AND Result (Decimal)': num1 & num2
      })
  df_results = pd.DataFrame(results_data)
  print(df_results.to_string(index=False)) # Use to_string for better console alignment
