# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime Number Checker
#
# Write a Python program that checks whether a given number is prime.
#
# A prime number is a whole number greater than 1 that has no divisors
# other than 1 and itself (e.g., 2, 3, 5, 7, 11, 13 ...).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter a number: 7
#   7 is a prime number.
#
#   Enter a number: 10
#   10 is NOT a prime number.
#
#   Enter a number: 1
#   1 is NOT a prime number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement the logic inside a function (see scaffold below).
# - Numbers less than 2 are NOT prime — handle this inside the function.
# - The main block must call the function and print the result.
#

# =============================================================================
def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is NOT a prime number.")
# =============================================================================

