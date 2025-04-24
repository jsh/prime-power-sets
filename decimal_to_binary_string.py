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

# --- Examples ---
print(f"2 -> {decimal_to_binary_string(2)}")      # Expected: 10
print(f"7 -> {decimal_to_binary_string(7)}")      # Expected: 111
print(f"13 -> {decimal_to_binary_string(13)}")     # Expected: 1101
print(f"0 -> {decimal_to_binary_string(0)}")      # Expected: 0
print(f"1 -> {decimal_to_binary_string(1)}")      # Expected: 1
print(f"16 -> {decimal_to_binary_string(16)}")    # Expected: 10000
print(f"35 -> {decimal_to_binary_string(35)}")    # Expected: 100011

print("-" * 20)

# --- Error Handling Examples ---
print(f"-5 -> {decimal_to_binary_string(-5)}")     # Test negative input
print(f"10.5 -> {decimal_to_binary_string(10.5)}") # Test non-integer input
print(f"'abc' -> {decimal_to_binary_string('abc')}")# Test non-numeric input
