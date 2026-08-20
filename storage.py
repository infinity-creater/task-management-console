import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except json.JSONDecodeError:
        print("Warning: tasks.json contains invalid data.")
        return []

    except OSError as error:
        print(f"Error reading task file: {error}")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)

        return True

    except OSError as error:
        print(f"Error saving tasks: {error}")
        return False