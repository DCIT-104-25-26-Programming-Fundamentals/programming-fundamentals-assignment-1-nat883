# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
#!/usr/bin/env python3
from typing import Optional, Tuple


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b


def modulus(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a % b


def exponent(a: float, b: float) -> float:
    return a ** b


def read_number(prompt: str) -> Optional[float]:
    """Read a number from input; return None if invalid."""
    try:
        return float(input(prompt).strip())
    except ValueError:
        print("Error: Please enter a valid number.")
        return None


def read_two_numbers() -> Optional[Tuple[float, float]]:
    """Prompt for two numbers and return them as a tuple, or None on invalid input."""
    a = read_number("Enter first number : ")
    if a is None:
        return None
    b = read_number("Enter second number: ")
    if b is None:
        return None
    return a, b


def fmt_num(x: float, force_decimals: Optional[int] = None) -> str:
    """Format numbers:
       - If force_decimals is provided, use that many decimals.
       - Otherwise, show as integer if whole number, else trim trailing zeros.
    """
    if force_decimals is not None:
        return f"{x:.{force_decimals}f}"
    if float(x).is_integer():
        return str(int(x))
    # Trim unnecessary trailing zeros but keep a few decimals if needed
    s = f"{x:.6f}".rstrip("0").rstrip(".")
    return s


def show_menu() -> None:
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main() -> None:
    while True:
        show_menu()
        choice = input("Select an operation (1-7): ").strip()
        if choice == "1":
            nums = read_two_numbers()
            if not nums:
                continue
            a, b = nums
            res = add(a, b)
            print(f"Result: {fmt_num(a)} + {fmt_num(b)} = {fmt_num(res)}")
        elif choice == "2":
            nums = read_two_numbers()
            if not nums:
                continue
            a, b = nums
            res = subtract(a, b)
            print(f"Result: {fmt_num(a)} - {fmt_num(b)} = {fmt_num(res)}")
        elif choice == "3":
            nums = read_two_numbers()
            if not nums:
                continue
            a, b = nums
            res = multiply(a, b)
            print(f"Result: {fmt_num(a)} * {fmt_num(b)} = {fmt_num(res)}")
        elif choice == "4":
            nums = read_two_numbers()
            if not nums:
                continue
            a, b = nums
            res = divide(a, b)
            if res is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {fmt_num(a)} / {fmt_num(b)} = {fmt_num(res, force_decimals=2)}")
        elif choice == "5":
            nums = read_two_numbers()
            if not nums:
                continue
            a, b = nums
            res = modulus(a, b)
            if res is None:
                print("Error: Cannot perform modulus by zero.")
            else:
                print(f"Result: {fmt_num(a)} % {fmt_num(b)} = {fmt_num(res)}")
        elif choice == "6":
            nums = read_two_numbers()
            if not nums:
                continue
            a, b = nums
            try:
                res = exponent(a, b)
            except OverflowError:
                print("Error: Result is too large.")
                continue
            print(f"Result: {fmt_num(a)} ** {fmt_num(b)} = {fmt_num(res)}")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
# =============================================================================

