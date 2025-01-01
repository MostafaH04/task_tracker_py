# CLI Task Tracker
[![codecov](https://codecov.io/gh/MostafaH04/task_tracker_py/graph/badge.svg?token=Z1Y0KH7JDC)](https://codecov.io/gh/MostafaH04/task_tracker_py)
![Pipeline](https://github.com/MostafaH04/task_tracker_py/actions/workflows/ci.yaml/badge.svg)

Simple CLI task tracker. I was bored, so I decided to do this for fun :P

It follows the problem description [here](https://roadmap.sh/projects/task-tracker).

The main purpose of this project was to set up automated tests (using unittests & coverage module) that run using GitHub Actions. There are also some static analysis jobs using `ruff` and `mypy`.

# Cloning
To clone the repo run the following commands
```
git clone https://github.com/MostafaH04/task_tracker_py.git
cd task_tracker_py
```

# Usage
The task tracker CLI follows the expected interface provided in the problem description. To call it one must call `py taskCLI.py`.

```
# Adding a new task
py taskCLI.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
py taskCLI.py update 1 "Buy groceries and cook dinner"
py taskCLI.py delete 1

# Marking a task as in progress, done or todo
py taskCLI.py mark-in-progress 1
py taskCLI.py mark-done 1
py taskCLI.py mark-todo 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list "Done"
task-cli list "TODO"
task-cli list "In Progress"
```

This is built on a task tracker class interface under `/TaskInterface`. Docstrings are provided to guide users regarding their usage.
