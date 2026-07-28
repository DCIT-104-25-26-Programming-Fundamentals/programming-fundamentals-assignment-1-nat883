# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
#!/usr/bin/env python3
from typing import List

def generate_fibonacci(n: int) -> List[int]:
    """Return a list with the first n Fibonacci numbers (n >= 1). Uses a loop."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fibs = [0, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def part_a_print_terms() -> None:
    """Ask user for N and print the first N Fibonacci numbers on one line."""
    try:
        n = int(input("How many terms? ").strip())
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    seq = generate_fibonacci(n)
    print("Fibonacci sequence:", " ".join(str(x) for x in seq))

def is_fibonacci_number(x: int) -> bool:
    """Return True if x is a Fibonacci number. Generates Fibonacci numbers with a loop."""
    if x < 0:
        return False
    a, b = 0, 1
    while a < x:
        a, b = b, a + b
    return a == x

def part_b_check_number() -> None:
    """Ask user for a number and report whether it is a Fibonacci number."""
    try:
        num = int(input("Enter a number to check: ").strip())
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if is_fibonacci_number(num):
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")

def main() -> None:
    """Simple menu to run Part A or Part B (or both)."""
    while True:
        print("\nFibonacci Tasks:")
        print("1. Print the first N terms (Part A)")
        print("2. Check if a number is in the sequence (Part B)")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            part_a_print_terms()
        elif choice == "2":
            part_b_check_number()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
# =============================================================================

