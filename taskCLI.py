import sys

from TaskInterface.TaskInterface import TaskInterface


def main(args: list) -> int:
    if len(args) < 2:
        return 1

    file_name = args[0]
    task_interface = TaskInterface(file_name)
    args = args[1:]
    command = args[0]

    try:
        res = None
        if command == "add":
            if len(args) != 2:
                return 1

            task_interface.add_task(args[1])

        elif command == "update":
            if len(args) != 3:
                return 1

            res = task_interface.update_task(int(args[1]), args[2])

        elif command == "delete":
            if len(args) != 2:
                return 1

            res = task_interface.delete_task(int(args[1]))

        elif command == "mark-in-progress":
            if len(args) != 2:
                return 1

            res = task_interface.update_task_progress(int(args[1]), "In Progress")

        elif command == "mark-done":
            if len(args) != 2:
                return 1

            res = task_interface.update_task_progress(int(args[1]), "Done")

        elif command == "mark-todo":
            if len(args) != 2:
                return 1

            res = task_interface.update_task_progress(int(args[1]), "TODO")

        elif command == "list":
            subcommnad = None
            if len(args) != 1:
                subcommnad = args[1]

            task_interface.list_tasks(subcommnad)

        if res is not None:
            if not res:
                return 1

        return 0

    except ValueError:
        return 1


if __name__ == "__main__":
    ret_val = main(sys.argv[1:])
    sys.exit(ret_val)
