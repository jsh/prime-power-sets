# Save this code in a file, e.g., get_np.py
import argparse
import sys
import math

def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0: # Check if even (and not 2)
        return False
    # Check odd divisors up to the integer square root of num
    limit = math.isqrt(num) # Requires Python 3.8+; use int(math.sqrt(num)) for older versions
    for i in range(3, limit + 1, 2):
        if num % i == 0:
            return False
    return True

def main():
    """Parses command line arguments for a non-negative integer n and a prime p."""
    parser = argparse.ArgumentParser(
        description="Get a non-negative integer n and a prime number p from the command line.",
        epilog="Example: python get_np.py 10 7"
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
         sys.exit(1) # Exit with a non-zero status indicating failure

    # --- Custom Validation ---

    # Validate n: Must be non-negative
    if args.n < 0:
        # parser.error prints the message and exits gracefully
        parser.error(f"Argument n: Must be a non-negative integer. Received: {args.n}")

    # Validate p: Must be prime
    if not is_prime(args.p):
        parser.error(f"Argument p: Must be a prime number. {args.p} is not prime.")

    # --- Success ---
    # If we reach here, the arguments are valid
    print("Successfully received and validated arguments:")
    print(f"  n = {args.n}")
    print(f"  p = {args.p}")

    # You can now use args.n and args.p in the rest of your script
    # Example: result = args.n + args.p
    # print(f"n + p = {result}")

if __name__ == "__main__":
    main()
