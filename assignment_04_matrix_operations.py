# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
from typing import List, Optional

Matrix = List[List[int]]

def transpose(matrix: Matrix) -> Matrix:
    """Return the transpose of matrix (M x N -> N x M)."""
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    result: Matrix = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][i] = matrix[i][j]
    return result

def add_matrices(a: Matrix, b: Matrix) -> Optional[Matrix]:
    """Return element-wise sum of two same-sized matrices, or None if sizes differ."""
    if not a or not b:
        return None
    m, n = len(a), len(a[0])
    if len(b) != m or any(len(row) != n for row in b):
        return None
    result: Matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = a[i][j] + b[i][j]
    return result

def multiply_matrices(a: Matrix, b: Matrix) -> Optional[Matrix]:
    """Return product A x B where A is MxN and B is NxP, or None if dimensions incompatible."""
    if not a or not b:
        return None
    m, n = len(a), len(a[0])
    if any(len(row) != n for row in a):
        return None  # irregular A
    if any(len(row) != len(b[0]) for row in b):
        # still allow if b is rectangular but check inner dimension
        pass
    # inner dimension check
    if len(b) != n:
        return None
    p = len(b[0])
    result: Matrix = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            s = 0
            for k in range(n):
                s += a[i][k] * b[k][j]
            result[i][j] = s
    return result

def print_matrix(matrix: Matrix) -> None:
    """Print matrix with neat alignment."""
    if not matrix:
        print("[]")
        return
    width = max(len(str(elem)) for row in matrix for elem in row)
    for row in matrix:
        print(" ".join(f"{elem:>{width}}" for elem in row))

def read_positive_int(prompt: str) -> int:
    while True:
        try:
            v = int(input(prompt))
            if v <= 0:
                print("Please enter a positive integer.")
                continue
            return v
        except ValueError:
            print("Please enter a valid integer.")

def read_matrix(rows: int, cols: int) -> Matrix:
    """Read a rows x cols matrix from user, reprompting on invalid input."""
    matrix: Matrix = []
    for r in range(rows):
        while True:
            line = input(f"Enter row {r+1}: ").strip()
            parts = line.split()
            if len(parts) != cols:
                print(f"Error: expected {cols} values but got {len(parts)}. Try again.")
                continue
            try:
                row = [int(x) for x in parts]
            except ValueError:
                print("Error: please enter integers only.")
                continue
            matrix.append(row)
            break
    return matrix

def part_a_transpose() -> None:
    print("\n--- PART A: Transpose a Matrix ---")
    rows = read_positive_int("Enter number of rows: ")
    cols = read_positive_int("Enter number of columns: ")
    print("Enter the matrix rows:")
    a = read_matrix(rows, cols)
    print("\nOriginal Matrix:")
    print_matrix(a)
    t = transpose(a)
    print("\nTransposed Matrix:")
    print_matrix(t)
    print()

def part_b_add() -> None:
    print("\n--- PART B: Add Two Matrices ---")
    rows = read_positive_int("Enter number of rows: ")
    cols = read_positive_int("Enter number of columns: ")
    print("Enter first matrix:")
    a = read_matrix(rows, cols)
    print("Enter second matrix:")
    b = read_matrix(rows, cols)
    s = add_matrices(a, b)
    if s is None:
        print("Error: Matrices must have the same dimensions.")
        return
    print("\nMatrix A:")
    print_matrix(a)
    print("\nMatrix B:")
    print_matrix(b)
    print("\nSum (A + B):")
    print_matrix(s)
    print()

def part_c_multiply() -> None:
    print("\n--- PART C: Multiply Two Matrices ---")
    m = read_positive_int("Enter number of rows for matrix A (M): ")
    n = read_positive_int("Enter number of columns for matrix A (N): ")
    print("Enter matrix A:")
    a = read_matrix(m, n)

    # For matrix B we need rows == n
    while True:
        print(f"Matrix B must have {n} rows (to match A's columns).")
        p = read_positive_int("Enter number of columns for matrix B (P): ")
        print(f"Enter matrix B (rows = {n}, columns = {p}):")
        b = read_matrix(n, p)
        prod = multiply_matrices(a, b)
        if prod is None:
            print("Error: incompatible dimensions for multiplication. Try again.")
            continue
        print("\nMatrix A:")
        print_matrix(a)
        print("\nMatrix B:")
        print_matrix(b)
        print("\nProduct (A x B):")
        print_matrix(prod)
        print()
        break

def main() -> None:
    while True:
        print("Matrix Operations Menu:")
        print("1. Transpose a matrix (Part A)")
        print("2. Add two matrices (Part B)")
        print("3. Multiply two matrices (Part C)")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            part_a_transpose()
        elif choice == "2":
            part_b_add()
        elif choice == "3":
            part_c_multiply()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()
# =============================================================================

