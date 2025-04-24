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
        print(
            f"Error: Invalid base 3 string '{base3_string}'. String must only contain '0', '1', or '2' and cannot be empty."
        )
        return None


# --- Examples ---
print(f"'11' base 3 is: {base3_to_decimal('11')}")  # Expected: 4
print(
    f"'1101' base 3 is: {base3_to_decimal('1101')}"
)  # Expected: 37 (1*27 + 1*9 + 0*3 + 1*1)
print(f"'201' base 3 is: {base3_to_decimal('201')}")  # Expected: 19 (2*9 + 0*3 + 1*1)
print(f"'0' base 3 is: {base3_to_decimal('0')}")  # Expected: 0
print(f"'10' base 3 is: {base3_to_decimal('10')}")  # Expected: 3
print("-" * 20)

# --- Error Handling Examples ---
print(f"Invalid input '13': {base3_to_decimal('13')}")  # Contains invalid digit '3'
print(f"Invalid input 'abc': {base3_to_decimal('abc')}")  # Contains invalid characters
print(f"Invalid input '': {base3_to_decimal('')}")  # Empty string
print(f"Invalid input 11 (int): {base3_to_decimal(11)}")  # Input is not a string
