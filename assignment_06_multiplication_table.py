# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
#!/usr/bin/env python3
from typing import Optional

def print_table(number: int) -> None:
    """Print the multiplication table for `number` from 1 to 12."""
    print(f"Multiplication Table for {number}:")
    # Choose widths so columns align nicely for typical small numbers
    left_w = len(str(number))
    mult_w = 2  # width for multiplier (1..12)
    res_w = max(len(str(number * 12)), 2)
    for i in range(1, 13):
        # Format: "<num>  x  <i>  =  <result>" with aligned columns
        print(f"{str(number).rjust(left_w)}  x  {str(i).rjust(mult_w)}  =  {str(number * i).rjust(res_w)}")
    print()

def print_tables_up_to(n: int) -> None:
    """Print multiplication tables for every number from 1 to n (inclusive).
    If n is not a positive integer, print an error message and stop (return)."""
    if n <= 0:
        print("Error: N must be a positive integer.")
        return
    for num in range(1, n + 1):
        print_table(num)
        if num != n:
            print("-" * 27)  # separator line between tables

def read_positive_int(prompt: str) -> Optional[int]:
    """Read an integer from input; return None on invalid integer input."""
    try:
        value = int(input(prompt).strip())
    except ValueError:
        return None
    return value

def part_a_single_table() -> None:
    """Interactively run Part A: single multiplication table."""
    val = read_positive_int("Enter a number: ")
    if val is None:
        print("Error: Please enter a valid integer.")
        return
    # Accept any integer for part A (including 0 or negatives); sample shows positives.
    print_table(val)

def part_b_tables_to_n() -> None:
    """Interactively run Part B: tables from 1 to N. N must be positive."""
    val = read_positive_int("Enter a number N: ")
    if val is None:
        print("Error: Please enter a valid integer.")
        return
    if val <= 0:
        print("Error: N must be a positive integer.")
        return
    print_tables_up_to(val)

def main() -> None:
    """Simple menu to run Part A or Part B."""
    while True:
        print("Multiplication Table Generator:")
        print("1. Single table (Part A)")
        print("2. Tables from 1 to N (Part B)")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            part_a_single_table()
        elif choice == "2":
            part_b_tables_to_n()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
# =============================================================================

