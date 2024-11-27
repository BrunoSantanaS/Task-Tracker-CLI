/*
# Python Task Tracker CLI

[Task Tracker CLI](https://roadmap.sh/projects/task-tracker)

## Context

Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## Requirements

The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

## Constraints
Here are some constraints to guide the implementation:

You can use any programming language to build this project.
Use positional arguments in command line to accept user inputs.
Use a JSON file to store the tasks in the current directory.
The JSON file should be created if it does not exist.
Use the native file system module of your programming language to interact with the JSON file.
Do not use any external libraries or frameworks to build this project.
Ensure to handle errors and edge cases gracefully.

## Installing

To get started with the Task Tracker CLI, follow these steps:

### Clone the Repository

First, clone the repository to your local machine using the following command:

```powershell
git clone https://github.com/BrunoSantanaS/Task-Tracker-CLI.git
cd .\Task-Tracker-CLI
```

### Set Up the Virtual Environment

Create a virtual environment to manage dependencies. This helps to keep your project dependencies isolated from your global Python environment.

```powershell
python3 -m venv .venv
```

### Activate the Virtual Environment

Activate the virtual environment to start using it.

#### On Linux:

```bash
source ./.venv/bin/activate
```

#### On Windows:

```powershell
.\.venv\Scripts\activate
```

### Install Dependencies

Install the required dependencies listed in the `requirements.txt` file.

```powershell
pip install -r requirements.txt
```

### Verify Installation

To verify that the installation was successful, you can run the following command to see the help message for the CLI:

```bash
python . --help
```

This should display a list of available commands and their usage.

Now you are ready to use the Task Tracker CLI to manage your tasks!
```
Usage: . [OPTIONS] COMMAND [ARGS]...

  Welcome to the Python Task Tracker CLI application

  This application allow you to manage your tasks using CRUD operations.

  Creator: Bruno de Santana Santos https://github.com/BrunoSantanaS

Options:
  --help  Show this message and exit.

Commands:
  add               Adds a new task with the given description.
  delete            Deletes a task by its ID.
  list              Lists tasks based on the provided filter.
  mark-done         Marks a task as 'done' based on the provided task ID.
  mark-in-progress  Mark a task as 'in-progress' based on its ID.
  mark-to-do        Marks a task as 'todo' based on the provided task ID.
  update            Update the description of a task by its ID.
```

### Update a Task
To update an existing task, use the `update` command followed by the task ID and the new description.
```bash
python . update <task_id> "<your_new_task_description>"
```

### Delete a Task
To delete a task, use the `delete` command followed by the task ID.
```bash
python . delete <task_id>
```

### Mark a Task as In Progress
To mark a task as in progress, use the `in-progress` command followed by the task ID.
```bash
python . in-progress <task_id>
```

### Mark a Task as Done
To mark a task as done, use the `mark-done` command followed by the task ID.
```bash
python . mark-done <task_id>
```

### Mark a Task as ToDo
To mark a task as todo, use the `mark-to-do` command followed by the task ID.
```bash
python . mark-to-do <task_id>
```

### List All Tasks
To list all tasks, use the `list` command.
```bash
python . list
```

### List Done Tasks
To list all tasks that are done, use the command `list` followed by the `done` argument.
```bash
python . list done
```

### List To Do Tasks
To list all tasks that are to do, use the `list` followed by the `todo` argument.
```bash
python . list todo
```

### List In Progress Tasks
To list all tasks that are in progress, use the `list` followed by the `in-progress` argument.
```bash
python . list in-progress
```

Make sure to replace all variables, such as`<task_id>` with the actual ID or description of the task you want to update, delete, or change the status of.