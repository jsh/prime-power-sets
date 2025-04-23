def count_set_bits_native(n):
  """Counts set bits using the native int.bit_count() method (Python 3.10+)."""
  if not isinstance(n, int):
	  raise TypeError("Input must be an integer.")
  # This is the most efficient method in Python 3.10+
  return n.bit_count()

# Example Usage
num = 29 # Binary: 11101
print(f"Number: {num} (Binary: {bin(num)})")
print(f"Set bits (native): {count_set_bits_native(num)}") # Output: 3

num = 42 # Binary: 101010
print(f"\nNumber: {num} (Binary: {bin(num)})")
print(f"Set bits (native): {count_set_bits_native(num)}") # Output: 3

num = -5 # Two's complement depends on width, but bit_count handles it infinitely
print(f"\nNumber: {num} (Binary: {bin(num)})")
# For negative numbers, it counts bits in the (infinite) two's complement representation.
# Think of it like ...111111111011 for -5. Since it's infinite 1s, this isn't
# practically useful unless you're working within fixed-width contexts implicitly.
# However, the *method itself* is defined and works.
# Python doesn't have fixed-width integers by default, so the two's complement
# notion for negatives is slightly different than in C/Java.
# print(f"Set bits (native): {count_set_bits_native(num)}") # Output: (inf) - usually not what's desired without context

# For non-negative integers, it's perfectly defined:
num = 0
print(f"\nNumber: {num} (Binary: {bin(num)})")
print(f"Set bits (native): {count_set_bits_native(num)}") # Output: 0

num = (1 << 1000) - 1 # A large number (1000 ones)
# print(f"\nNumber: Large number with 1000 bits") # Avoid printing large number
# print(f"Set bits (native): {count_set_bits_native(num)}") # Output: 1000
