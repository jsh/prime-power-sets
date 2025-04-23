# Save this code as, for example, get_integer_simple.py
import sys

def main():
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
        k = int(argument_str)
        print(f"Successfully received the integer: {k}")
        print(f"The type is: {type(k)}")

        # --- Use the integer 'k' ---
        result = k * 2
        print(f"{k} multiplied by 2 is: {result}")

    except ValueError:
        # Handle the case where the argument is not a valid integer
        print(f"Error: Argument '{argument_str}' is not a valid integer.", file=sys.stderr)
        sys.exit(1) # Exit with an error code
    except Exception as e:
        # Catch other potential unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()