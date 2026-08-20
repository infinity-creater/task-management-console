from datetime import datetime
from storage import load_tasks, save_tasks


class TaskManager:
    """Manages all task-related operations."""

    VALID_PRIORITIES = ["Low", "Medium", "High"]
    VALID_STATUSES = ["Pending", "Completed"]

    def __init__(self):
        self.tasks = load_tasks()

    # --------------------------------------------------
    # Validation Functions
    # --------------------------------------------------

    def validate_date(self, date_string):
        """Validate date format YYYY-MM-DD."""
        try:
            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def validate_priority(self, priority):
        """Validate task priority."""
        return priority.capitalize() in self.VALID_PRIORITIES

    # --------------------------------------------------
    # ID Generation
    # --------------------------------------------------

    def generate_task_id(self):
        """Generate a unique task ID."""
        if not self.tasks:
            return "T001"

        numbers = []

        for task in self.tasks:
            task_id = task.get("id", "")

            if task_id.startswith("T"):
                try:
                    numbers.append(int(task_id[1:]))
                except ValueError:
                    pass

        next_number = max(numbers, default=0) + 1

        return f"T{next_number:03d}"

    # --------------------------------------------------
    # Add Task
    # --------------------------------------------------

    def add_task(self, title, description, priority, due_date):
        """Add a new task."""

        title = title.strip()
        description = description.strip()
        priority = priority.strip().capitalize()
        due_date = due_date.strip()

        if not title:
            raise ValueError("Task title cannot be empty.")

        if not self.validate_priority(priority):
            raise ValueError(
                "Invalid priority. Choose Low, Medium or High."
            )

        if not self.validate_date(due_date):
            raise ValueError(
                "Invalid date. Use YYYY-MM-DD format."
            )

        task = {
            "id": self.generate_task_id(),
            "title": title,
            "description": description,
            "priority": priority,
            "due_date": due_date,
            "status": "Pending"
        }

        self.tasks.append(task)
        save_tasks(self.tasks)

        return task

    # --------------------------------------------------
    # View Tasks
    # --------------------------------------------------

    def get_all_tasks(self):
        """Return all tasks."""
        return self.tasks

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search_tasks(self, keyword):
        """Search tasks by title or description."""

        keyword = keyword.strip().lower()

        if not keyword:
            return []

        results = []

        for task in self.tasks:
            title = task.get("title", "").lower()
            description = task.get("description", "").lower()

            if keyword in title or keyword in description:
                results.append(task)

        return results

    # --------------------------------------------------
    # Filter
    # --------------------------------------------------

    def filter_by_priority(self, priority):
        """Filter tasks by priority."""

        priority = priority.strip().capitalize()

        if not self.validate_priority(priority):
            raise ValueError(
                "Invalid priority. Choose Low, Medium or High."
            )

        return [
            task for task in self.tasks
            if task.get("priority") == priority
        ]

    def filter_by_status(self, status):
        """Filter tasks by status."""

        status = status.strip().capitalize()

        if status not in self.VALID_STATUSES:
            raise ValueError(
                "Invalid status. Choose Pending or Completed."
            )

        return [
            task for task in self.tasks
            if task.get("status") == status
        ]

    # --------------------------------------------------
    # Sorting
    # --------------------------------------------------

    def sort_by_due_date(self):
        """Return tasks sorted by due date."""
        return sorted(
            self.tasks,
            key=lambda task: task.get("due_date", "")
        )

    def sort_by_title(self):
        """Return tasks sorted alphabetically by title."""
        return sorted(
            self.tasks,
            key=lambda task: task.get("title", "").lower()
        )

    def sort_by_priority(self):
        """Return tasks sorted by priority."""

        priority_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3
        }

        return sorted(
            self.tasks,
            key=lambda task: priority_order.get(
                task.get("priority"), 4
            )
        )

    # --------------------------------------------------
    # Find Task
    # --------------------------------------------------

    def find_task(self, task_id):
        """Find a task using its ID."""

        task_id = task_id.strip().upper()

        for task in self.tasks:
            if task.get("id") == task_id:
                return task

        return None

    # --------------------------------------------------
    # Update Task
    # --------------------------------------------------

    def update_task(
        self,
        task_id,
        title=None,
        description=None,
        priority=None,
        due_date=None
    ):
        """Update an existing task."""

        task = self.find_task(task_id)

        if task is None:
            return False

        if title is not None:
            title = title.strip()

            if not title:
                raise ValueError("Task title cannot be empty.")

            task["title"] = title

        if description is not None:
            task["description"] = description.strip()

        if priority is not None:
            priority = priority.strip().capitalize()

            if not self.validate_priority(priority):
                raise ValueError(
                    "Invalid priority. Choose Low, Medium or High."
                )

            task["priority"] = priority

        if due_date is not None:
            due_date = due_date.strip()

            if not self.validate_date(due_date):
                raise ValueError(
                    "Invalid date. Use YYYY-MM-DD format."
                )

            task["due_date"] = due_date

        save_tasks(self.tasks)

        return True

    # --------------------------------------------------
    # Delete Task
    # --------------------------------------------------

    def delete_task(self, task_id):
        """Delete a task."""

        task = self.find_task(task_id)

        if task is None:
            return False

        self.tasks.remove(task)
        save_tasks(self.tasks)

        return True

    # --------------------------------------------------
    # Complete Task
    # --------------------------------------------------

    def complete_task(self, task_id):
        """Mark a task as completed."""

        task = self.find_task(task_id)

        if task is None:
            return False

        task["status"] = "Completed"

        save_tasks(self.tasks)

        return True

    # --------------------------------------------------
    # Overdue Tasks
    # --------------------------------------------------

    def get_overdue_tasks(self):
        """Return pending tasks whose due date has passed."""

        today = datetime.now().date()
        overdue_tasks = []

        for task in self.tasks:
            if task.get("status") == "Completed":
                continue

            try:
                due_date = datetime.strptime(
                    task.get("due_date"),
                    "%Y-%m-%d"
                ).date()

                if due_date < today:
                    overdue_tasks.append(task)

            except (ValueError, TypeError):
                continue

        return overdue_tasks