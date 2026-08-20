# Task Management Console

## 1. PROJECT TITLE

Task Management Console

Python-based task management application allowing users to create, organize, track and manage their daily tasks effortlessly using a simple command-line interface.

---

## 2. PROBLEM STATEMENT

Managing multiple tasks can be quite challenging especially with deadlines, priority levels and status to track. It can also be stressful to keep track of all work related activities by hand. This makes it very easy to miss out on important tasks and deadlines.

The Task Management Console was built in order to manage tasks effortlessly in a single platform. It allows the user to add tasks, set priorities, due dates, search tasks, filter tasks, update tasks, mark task as complete, delete tasks, detect overdue tasks among other features.

The tasks are stored in files as a persistent storage of the task details which allows viewing editing and deleting tasks even after closing the application.

---

## 3. OBJECTIVE

The objective of this project is to develop and present a working task management application built using Python.

The project is aimed to demonstrate the practical applications of concepts such as

Functions

Lists

Dictionaries

Object-oriented programming

Conditional statements

Loops

Input validation

Error handling

Storing data in files and JSON format

Searching

Filtering

Sorting

Date functions

Testing

The project is also aimed to present a simple and reliable task management application that can help the users to effectively manage their tasks and deadlines.

---

## 4. FEATURES

### 4.1 Add Tasks

The system allows the users to add tasks to the system by providing the following information:

- Task title

- Task description

- Priority

- Due date

Each task is assigned a task ID as shown below

### 4.2 View Tasks

The system allows the users to view tasks in a table as shown below:

### 4.3 Search Tasks

This feature allows the user to search for tasks using a keyword. This is useful when trying to locate a specific task from many tasks. The search is performed against the task title and task description.

### 4.4 Filter Tasks

This feature allows the user to filter tasks based on priority and status.

The priority filter options are:

- Low

- Medium

- High

The status filter options are:

- Pending

- Completed

### 4.5 Sort Tasks

This feature allows the user to sort the tasks based on due date, title and priority.

The task priority levels are ordered as:

$$ High \rightarrow Medium \rightarrow Low $$

### 4.6 Update Tasks

This feature allows the user to update task details.

The following task fields are updatable:

- Title

- Description

- Priority

- Due date

However, the task ID is not allowed to be updated.

### 4.7 Delete Tasks

This feature allows the user to delete an existing task from the system. The user deletes a task by providing the task ID. The user also needs to enter a confirmation prompt before the task gets deleted.

### 4.8 Mark Tasks as Completed

This feature allows the user to mark a pending task as a completed task. In this case, the status field of a pending task changes from

"Pending"

to

"Completed"

### 4.9 Overdue Tasks Detection

The system is able to automatically detect tasks that are due but have not been completed. Completed tasks are excluded from the overdue list.

### 4.10 Data Persistence

This feature allows the application to store task information in a file and later retrieve the information from the file as needed.

This is useful since the tasks are saved even after the application has been closed.

The tasks are stored in JSON format in a file named

'tasks.json'

### 4.11 Input Validation and Error Handling

Input validation prevents the application from accepting wrong input. The following validations have been implemented

- Empty task titles

- Invalid priority

- Invalid date format

- Invalid menu options

- Invalid task IDs

The application also implements error handling mechanisms to handle errors that may arise while reading from/writing to files or JSON encoding/decoding errors.

---

## 5. TECHNOLOGIES

| TECHNOLOGY | USAGE |

| --- | --- |

| Python 3 | Development language |

| JSON | Persistent storage |

| Datetime | Date validation and overdue task detection |

| Unittest | Testing |

| VS Code | Development environment |

### Python modules used

The following Python modules were used in the development of the application:

- json

- os

- datetime

- unittest

However, no third-party Python modules were used.

---

## 6. INSTALLATION / SETUP INSTRUCTIONS

### Requirements

Ensure that you have Python 3 installed in your system. To verify this, open the terminal and execute the command below:

```bash

python --version

```

You should get an output similar to

`Python 3.x.x`

### Setup

Step 1: Download or clone the project folder.

Step 2: Launch Visual Studio Code.

Step 3: Open the terminal window.

Step 4: Make sure that you are in the project directory.

Step 5: Ensure that all the files have been downloaded successfully.

The project does not require you to install any packages. However, ensure that you have Python installed on your machine.

### Project Files

The following files should be present in the project directory:

```text

Task_Management_Console/

├── main.py

├── task_manager.py

├── storage.py

├── tasks.json

├── test_task_manager.py

├── README.md

└── PROJECT_REPORT.md

```

---

## 7. HOW TO RUN THE PROJECT

### Running the application

Open a terminal window and execute the following command:

```bash

python main.py

```

The application launches and presents a menu as shown below:

```text

==================================================

TASK MANAGEMENT CONSOLE

==================================================

1. Add Task

2. View Tasks

3. Search Tasks

4. Filter Tasks

5. Sort Tasks

6. Update Task

7. Delete Task

8. Mark Task Completed

9. Show Overdue Tasks

10. Exit

==================================================

Enter your choice:

```

Enter the option you want to select.

#### Sample

For instance, to add a new task, enter

`1`

and press

`enter`

You will be prompted to enter the task details as shown below:

```text

Enter your choice: 1

Enter task title: Complete ML Project

Enter description: Finish Learn Depth Python project

Enter priority (Low/Medium/High): High

Enter due date (YYYY-MM-DD): 2026-08-20

```

The application adds the task successfully and generates a task ID as shown below:

```text

Task added successfully!

Task ID: T001

```

### Running the tests

To execute the test suite, use the command below:

```bash

python -m unittest test_task_manager.py

```

A successful test will be shown below:

```text

........

----------------------------------------------------------------------

Ran 8 tests in 0.050s

OK

```

---

## 8. PROJECT STRUCTURE

The project structure is as shown below:

```text

Task_Management_Console/

├── main.py

├── task_manager.py

├── storage.py

├── tasks.json

├── test_task_manager.py

├── README.md

└── PROJECT_REPORT.md

```

### `main.py`

This file stores the main application programming logic which runs the task management console. It displays the menu and prompts the user to enter their choice of menu option.

### `task_manager.py`

This file stores the TaskManager class which implements all the features of the application.

The class contains the following methods:

- Adding tasks

- Searching tasks

- Filtering tasks

- Sorting tasks

- Updating tasks

- Deleting tasks

- Completing tasks

- Detecting overdue tasks

- Input validation

### `storage.py`

This file stores methods that implement the persistent storage of tasks locally in JSON format. It provides methods that allow loading and saving the task data from/to files.

### `tasks.json`

This file stores the task information in JSON format. The information stored includes the task ID, task title, task description, task priority, task due date and status.

Sample format:

```json

{

"id": "T001",

"title": "Complete ML Project",

"description": "Finish Learn Depth Python project",

"priority": "High",

"due_date": "2026-08-20",

"status": "Pending"

}

```

### `test_task_manager.py`

This file stores automated test cases that test the most important methods and validate the expected results.

### `requirements.txt`

This file stores information about the dependent packages used by the application. However, since the project only uses Python standard packages, there are no dependent packages listed in this file.

### `README.md`

This file contains information about the project including setup instructions, how to execute the code, project description, limitations, and future improvements.

### `PROJECT_REPORT.md`

This file stores the report for the current project.

---

## 9. TESTING

The project has been tested using Python's unittest test framework.

There are 8 test cases for the most important operations.

| TEST ID | TEST CASE | EXPECTED RESULT | RESULT |

| TC01 | Add valid task | Task is created successfully | PASS |

| TC02 | Add task with empty title | Validation error is raised | PASS |

| TC03 | Add task with invalid priority | Validation error is raised | PASS |

| TC04 | Add task with invalid date | Validation error is raised | PASS |

| TC05 | Search existing task | Matching task is returned | PASS |

| TC06 | Mark task as completed | Task status changes to Completed | PASS |

| TC07 | Delete existing task | Task is deleted successfully | PASS |

| TC08 | Filter tasks by priority | Matching tasks are returned | PASS |

### Command

```bash

python -m unittest test_task_manager.py

```

### Result

```text

........

----------------------------------------------------------------------

Ran 8 tests in 0.050s

OK

```

All the 8 automated test cases passed.

In addition to the automated testing, the manual testing was also done to test the most important features of the application.

The following features were tested:

- Adding tasks

- Viewing tasks

- Searching tasks

- Filtering tasks

- Sorting tasks

- Updating tasks

- Deleting tasks

- Marking tasks as completed

- Detecting overdue tasks

- Handling invalid inputs

- Saving and loading tasks

---

## 10. LIMITATIONS

The following are the limitations associated with the current version of the Task Management Console:

1. The application is not packaged with a graphical user interface.

2. Task information is not stored in a central database.

3. The system is not designed to support multiple users.

4. The system lacks cloud synchronization.

5. The system does not provide notification or reminder services.

6. The system is not designed to support recurring tasks.

7. The application does not support storing task data in external databases.

These limitations however make the current project minimalistic and focused on the core task management features.

---

## 11. FUTURE IMPROVEMENTS

Future improvements of this project may involve:

- Developing the graphical user interface

- Allowing user registration and authentication

- Using databases to store task information

- Implementing task notification system

- Supporting recurring tasks

- Allowing user to sync tasks over the cloud

- Generating productivity reports

- Adding tags and categories for tasks

- Developing web or mobile application version of the project

These improvements will make the system much more powerful and suitable for a production environment.

