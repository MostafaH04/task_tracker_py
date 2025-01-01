import json
import datetime
from typing import Union


class TaskInterface:
    """
    Task Planner Interface Class.

    This class handles updating, storing and retrieving tasks,
    for the task tracker using a JSON file.

    Attributes:
        task_file_name (str): JSON File storing tasks
        content (dict): Content of the JSON File (tasks)
    """

    def __init__(self, fileName: str = "task_file") -> None:
        """
        Initializes the task interface.

        This loads up the stored tasks in the JSON file, and
        manipulates the file based on the function calls.

        Parameters:
            fileName (str): Name of the JSON file (.json omitted).
                Defaults to `task_file`.
        """
        self.task_file_name = fileName + ".json"
        self.content = self._load_file_()

    def add_task(self, task_desc: str) -> None:
        """
        Adds a new task to the list.

        Parameters:
            task_desc (str): Description (or name) of the new task.
        """
        task_id = self._get_last_id_()
        curr_time = datetime.datetime.now()
        time_formated = curr_time.strftime("%c")

        new_task = {
            task_id: {
                "desc": task_desc,
                "status": "TODO",
                "createdAt": time_formated,
                "updatedAt": time_formated,
            }
        }

        self._add_content_(new_task)

    def delete_task(self, task_id: int) -> bool:
        """
        Removes a pre-existing task.

        Fails to remove task if it doesn't exist.

        Parameters:
            task_id (int): ID corresponding to the task.

        Returns:
            bool: A boolean representing if the task has been deleted successfully.
        """
        return self._remove_content_(task_id)

    def update_task(self, task_id: int, new_desc: str) -> bool:
        """
        Updates a pre-existing task.

        Fails to update task if it doesn't exist.

        Parameters:
            task_id (int): ID corresponding to the task.
            new_desc (str): New description for the task.

        Returns:
            bool: A boolean representing if the task has been updated successfully.
        """
        return self._update_content_(task_id, new_desc)

    def update_task_progress(self, task_id: int, progress: str) -> bool:
        """
        Updates the progress on a pre-existing task.

        Fails to update task if it doesn't exist, or
        if the new status is invalid.

        Parameters:
            task_id (int): ID corresponding to the task.

        Returns:
            bool: A boolean representing if the task has been updated successfully.
        """
        if progress != "TODO" and progress != "In Progress" and progress != "Done":
            return False

        return self._update_content_progress_(task_id, progress)

    def list_tasks(self, filter: Union[str, None] = None) -> None:
        for key in self.content.keys():
            if key == "last_id":
                continue

            task_id = int(key)
            task_status = self.content[key]["status"]

            if filter is not None and task_status != filter:
                continue

            print(self._format_task_(task_id, self.content[key]))
            print("_" * 60)

    def _format_task_(self, task_id: int, task_content: dict) -> str:
        formatted_text = f"""
ID: {task_id}\n
Description: {task_content["desc"]}\n
Status: {task_content["status"]}\n
Creation Time: {task_content["createdAt"]}\n
Last Updated Time: {task_content["updatedAt"]}"""

        return formatted_text

    def _add_content_(self, new_entry: dict) -> None:
        self.content.update(new_entry)
        self._update_file_()

    def _update_content_(self, id: int, new_desc: str) -> bool:
        if str(id) not in self.content:
            return False

        current_entry = self.content[str(id)]

        current_entry["desc"] = new_desc
        current_entry["updatedAt"] = datetime.datetime.now().strftime("%c")

        self.content[str(id)] = current_entry
        self._update_file_()

        return True

    def _update_content_progress_(self, id: int, new_progress: str) -> bool:
        if str(id) not in self.content:
            return False

        current_entry = self.content[str(id)]

        current_entry["status"] = new_progress
        current_entry["updatedAt"] = datetime.datetime.now().strftime("%c")

        self.content[str(id)] = current_entry
        self._update_file_()

        return True

    def _remove_content_(self, id: int) -> bool:
        if str(id) not in self.content:
            return False

        self.content.pop(str(id))
        self._update_file_()

        return True

    def _get_last_id_(self) -> int:
        last_id = int(self.content["last_id"]) + 1
        self.content["last_id"] = last_id

        return last_id

    def _load_file_(self) -> dict:
        file = open(self.task_file_name, "r+")
        content = json.load(file)
        file.close()

        return content

    def _update_file_(self) -> None:
        file = open(self.task_file_name, "w+")
        json.dump(self.content, file)
        file.close()
