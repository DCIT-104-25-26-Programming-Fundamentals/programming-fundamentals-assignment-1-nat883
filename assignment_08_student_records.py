# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================

# =============================================================================

#!/usr/bin/env python3
from typing import List, Dict, Optional

Student = Dict[str, object]

def add_student(students: List[Student]) -> None:
    """Add a student record (name, unique id, scores)."""
    name = input("Student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    # Read and validate unique integer ID
    id_str = input("Student ID: ").strip()
    try:
        sid = int(id_str)
    except ValueError:
        print("Error: ID must be an integer.")
        return
    if any(s["id"] == sid for s in students):
        print(f"Error: A student with ID {sid} already exists.")
        return

    # Read number of scores (must be >= 1)
    try:
        n_scores = int(input("How many scores? ").strip())
    except ValueError:
        print("Error: Please enter a valid integer for number of scores.")
        return
    if n_scores < 1:
        print("Error: Please enter at least 1 score.")
        return

    scores: List[float] = []
    for i in range(1, n_scores + 1):
        while True:
            try:
                score_input = input(f"Enter score {i}: ").strip()
                score = float(score_input)
                scores.append(score)
                break
            except ValueError:
                print("Error: Please enter a valid number for the score.")

    student = {"name": name, "id": sid, "scores": scores}
    students.append(student)
    print(f'Student "{name}" added successfully.')

def display_all_students(students: List[Student]) -> None:
    """Display all students with Name, ID, Scores, and Average (rounded to 2 decimals)."""
    if not students:
        print("No student records found.")
        return

    # Determine column widths
    name_w = max(4, max(len(s["name"]) for s in students))
    id_w = max(2, max(len(str(s["id"])) for s in students))
    scores_w = max(6, max(len(", ".join(format_score_list(s["scores"]))) for s in students))
    avg_w = 7

    sep = "-" * (name_w + id_w + scores_w + avg_w + 9)
    print(sep)
    print(f"{'Name':<{name_w}}   {'ID':<{id_w}}   {'Scores':<{scores_w}}   {'Average':>{avg_w}}")
    print(sep)
    for s in students:
        name = s["name"]
        sid = s["id"]
        scores_list = s["scores"]
        scores_str = ", ".join(format_score_list(scores_list))
        avg = calculate_average(scores_list)
        print(f"{name:<{name_w}}   {sid:<{id_w}}   {scores_str:<{scores_w}}   {avg:>{avg_w}.2f}")
    print(sep)

def format_score_list(scores: List[float]) -> List[str]:
    """Format each score to remove unnecessary decimal when integer-like."""
    formatted = []
    for sc in scores:
        if sc == int(sc):
            formatted.append(str(int(sc)))
        else:
            formatted.append(f"{sc:.2f}".rstrip('0').rstrip('.'))
    return formatted

def calculate_average(scores: List[float]) -> float:
    """Return the average of scores (assumes at least one score)."""
    return sum(scores) / len(scores)

def calculate_average_for_student(students: List[Student]) -> None:
    """Ask for student ID, find the student, and print their average (rounded to 2 decimals)."""
    id_str = input("Enter student ID: ").strip()
    try:
        sid = int(id_str)
    except ValueError:
        print("Error: ID must be an integer.")
        return
    found = next((s for s in students if s["id"] == sid), None)
    if found is None:
        print(f"Error: No student found with ID {sid}.")
        return
    avg = calculate_average(found["scores"])
    print(f"{found['name']}'s average score: {avg:.2f}")

def show_menu() -> None:
    """Print the main menu."""
    print("\n===============================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("===============================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

def main() -> None:
    students: List[Student] = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_average_for_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()