"""Todo list app."""
import sys

def add_task(task):
    """Add a task to the list."""
    with open("tasks.txt", "a") as f:
        f.write(f"{task}
")

def get_tasks():
    """Get all tasks from the file."""
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    while True:
        print(get_tasks())
        user_input = input("Enter a task (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        add_task(user_input)