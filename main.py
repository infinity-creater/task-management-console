from task_manager import TaskManager


def display_tasks(tasks):
    """Display tasks in a formatted table."""

    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n" + "-" * 90)
    print(
        f"{'ID':<8}"
        f"{'TITLE':<25}"
        f"{'PRIORITY':<12}"
        f"{'DUE DATE':<15}"
        f"{'STATUS':<15}"
    )
    print("-" * 90)

    for task in tasks:
        print(
            f"{task['id']:<8}"
            f"{task['title'][:23]:<25}"
            f"{task['priority']:<12}"
            f"{task['due_date']:<15}"
            f"{task['status']:<15}"
        )

    print("-" * 90)


def add_task(manager):
    print("\n========== ADD TASK ==========")

    title = input("Enter task title: ")
    description = input("Enter description: ")
    priority = input("Enter priority (Low/Medium/High): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    try:
        task = manager.add_task(
            title,
            description,
            priority,
            due_date
        )

        print("\nTask added successfully!")
        print(f"Task ID: {task['id']}")

    except ValueError as error:
        print(f"\nError: {error}")


def search_tasks(manager):
    print("\n========== SEARCH TASKS ==========")

    keyword = input("Enter search keyword: ")

    results = manager.search_tasks(keyword)

    display_tasks(results)


def filter_tasks(manager):
    print("\n========== FILTER TASKS ==========")
    print("1. Filter by Priority")
    print("2. Filter by Status")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            priority = input(
                "Enter priority (Low/Medium/High): "
            )

            results = manager.filter_by_priority(priority)
            display_tasks(results)

        elif choice == "2":
            status = input(
                "Enter status (Pending/Completed): "
            )

            results = manager.filter_by_status(status)
            display_tasks(results)

        else:
            print("Invalid choice.")

    except ValueError as error:
        print(f"Error: {error}")


def sort_tasks(manager):
    print("\n========== SORT TASKS ==========")
    print("1. Sort by Due Date")
    print("2. Sort by Title")
    print("3. Sort by Priority")

    choice = input("Enter choice: ")

    if choice == "1":
        results = manager.sort_by_due_date()

    elif choice == "2":
        results = manager.sort_by_title()

    elif choice == "3":
        results = manager.sort_by_priority()

    else:
        print("Invalid choice.")
        return

    display_tasks(results)


def update_task(manager):
    print("\n========== UPDATE TASK ==========")

    task_id = input("Enter Task ID: ").strip().upper()

    task = manager.find_task(task_id)

    if task is None:
        print("Task not found.")
        return

    print("\nPress Enter to keep the existing value.")

    title = input(
        f"Title [{task['title']}]: "
    )

    description = input(
        f"Description [{task['description']}]: "
    )

    priority = input(
        f"Priority [{task['priority']}]: "
    )

    due_date = input(
        f"Due Date [{task['due_date']}]: "
    )

    try:
        manager.update_task(
            task_id,
            title if title else None,
            description if description else None,
            priority if priority else None,
            due_date if due_date else None
        )

        print("\nTask updated successfully!")

    except ValueError as error:
        print(f"Error: {error}")


def delete_task(manager):
    print("\n========== DELETE TASK ==========")

    task_id = input("Enter Task ID: ").strip().upper()

    task = manager.find_task(task_id)

    if task is None:
        print("Task not found.")
        return

    print(f"Task: {task['title']}")

    confirmation = input(
        "Are you sure you want to delete it? (y/n): "
    ).lower()

    if confirmation == "y":
        if manager.delete_task(task_id):
            print("Task deleted successfully.")
        else:
            print("Unable to delete task.")

    else:
        print("Deletion cancelled.")


def complete_task(manager):
    print("\n========== COMPLETE TASK ==========")

    task_id = input("Enter Task ID: ").strip().upper()

    if manager.complete_task(task_id):
        print("Task marked as Completed.")

    else:
        print("Task not found.")


def show_overdue_tasks(manager):
    print("\n========== OVERDUE TASKS ==========")

    overdue_tasks = manager.get_overdue_tasks()

    if not overdue_tasks:
        print("No overdue tasks.")
        return

    display_tasks(overdue_tasks)


def main():
    manager = TaskManager()

    while True:
        print("\n")
        print("=" * 50)
        print("       TASK MANAGEMENT CONSOLE")
        print("=" * 50)

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Search Tasks")
        print("4. Filter Tasks")
        print("5. Sort Tasks")
        print("6. Update Task")
        print("7. Delete Task")
        print("8. Mark Task Completed")
        print("9. Show Overdue Tasks")
        print("10. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(manager)

        elif choice == "2":
            print("\n========== ALL TASKS ==========")
            display_tasks(manager.get_all_tasks())

        elif choice == "3":
            search_tasks(manager)

        elif choice == "4":
            filter_tasks(manager)

        elif choice == "5":
            sort_tasks(manager)

        elif choice == "6":
            update_task(manager)

        elif choice == "7":
            delete_task(manager)

        elif choice == "8":
            complete_task(manager)

        elif choice == "9":
            show_overdue_tasks(manager)

        elif choice == "10":
            print("\nThank you for using Task Management Console!")
            break

        else:
            print("\nInvalid choice. Please enter 1-10.")


if __name__ == "__main__":
    main()