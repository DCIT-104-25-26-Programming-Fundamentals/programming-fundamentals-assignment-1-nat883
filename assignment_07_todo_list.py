# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
#!/usr/bin/env python3
from typing import List

def add_task(tasks: List[str]) -> None:
    """Prompt the user and add a task to the list."""
    task = input("Enter task: ").strip()
    if not task:
        print("Error: Task cannot be empty.")
        return
    tasks.append(task)
    print(f'Task added: "{task}"')

def view_tasks(tasks: List[str]) -> None:
    """Display all tasks numbered from 1, or a friendly message if empty."""
    if not tasks:
        print("Your task list is empty.")
        return
    print("Your Tasks:")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")

def delete_task(tasks: List[str]) -> None:
    """Show tasks, ask which one to remove, and delete it if valid."""
    if not tasks:
        print("There are no tasks to delete.")
        return
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: ").strip())
    except ValueError:
        print("Error: Please enter a valid task number.")
        return
    if 1 <= choice <= len(tasks):
        removed = tasks.pop(choice - 1)
        print(f'Task "{removed}" has been removed.')
    else:
        print("Error: Invalid task number.")

def show_menu() -> None:
    """Print the to-do list menu."""
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

def main() -> None:
    tasks: List[str] = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
# =============================================================================

