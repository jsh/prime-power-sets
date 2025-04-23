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

# --- Example Usage ---

# Generate a sequence of length 10
n_elements = 10
sequence = generate_bit_count_sequence(n_elements)
print(f"Generated sequence for n={n_elements}:")
print(sequence)
# Expected output for n=10 (values of k from 0 to 9):
# [0.0, 1.0, 1.0, 1.5, 1.333..., 1.666..., 2.0, 2.333..., 2.0, 2.25]

# Print formatted values for clarity
print("\nFormatted values (k: value):")
for k, val in enumerate(sequence):
    print(f"{k}: {val:.4f}")

# Example with n=0
print(f"\nGenerated sequence for n=0:")
print(generate_bit_count_sequence(0)) # Output: []

# Example with n=1
print(f"\nGenerated sequence for n=1:")
print(generate_bit_count_sequence(1)) # Output: [0.0]

# Example demonstrating error handling
try:
    generate_bit_count_sequence(-5)
except ValueError as e:
    print(f"\nError handling test: {e}")

try:
    generate_bit_count_sequence(5.5)
except ValueError as e:
    print(f"Error handling test: {e}")
