import unittest
from unittest.mock import patch, call
import json
import os

from taskCLI import main


class TestInterface(unittest.TestCase):
    def test_add(self) -> None:
        """
        Test adding new tasks
        """
        file_name = "test_add_file"
        file_content = {"last_id": 0}

        f = open(file_name + ".json", "w")
        json.dump(file_content, f)
        f.close()

        cmd1 = [file_name, "add", "task_1"]
        cmd2 = [file_name, "add", "task_2"]
        cmd3 = [file_name, "add", "task_3"]
        cmd4 = [file_name, "add"]

        self.assertTrue(main(cmd1) == 0)
        self.assertTrue(main(cmd2) == 0)
        self.assertTrue(main(cmd3) == 0)
        self.assertFalse(main(cmd4) == 0)

        f = open(file_name + ".json", "r")
        content = json.load(f)
        f.close()

        os.remove(file_name + ".json")

        # Check task ids exist
        self.assertIn("1", content)
        self.assertIn("2", content)
        self.assertIn("3", content)

        self.assertTrue(content["1"]["desc"] == "task_1")
        self.assertTrue(content["2"]["desc"] == "task_2")
        self.assertTrue(content["3"]["desc"] == "task_3")

    def test_delete(self) -> None:
        """
        Test deleting exisitng tasks
        """
        file_name = "test_delete_file"
        file_content = {
            "1": {
                "desc": "task_1",
                "status": "TODO",
                "createdAt": "Wed Jan  1 08:49:30 2025",
                "updatedAt": "Wed Jan  1 08:49:30 2025",
            },
            "2": {
                "desc": "task_2",
                "status": "TODO",
                "createdAt": "Wed Jan  1 08:49:30 2025",
                "updatedAt": "Wed Jan  1 08:49:30 2025",
            },
            "3": {
                "desc": "task_3",
                "status": "TODO",
                "createdAt": "Wed Jan  1 08:49:30 2025",
                "updatedAt": "Wed Jan  1 08:49:30 2025",
            },
            "last_id": 3,
        }

        f = open(file_name + ".json", "w")
        json.dump(file_content, f)
        f.close()

        cmd1 = [file_name, "delete", 1]
        cmd2 = [file_name, "delete", 3]
        cmd3 = [file_name, "delete", 5]
        cmd4 = [file_name, "delete"]

        self.assertTrue(main(cmd1) == 0)
        self.assertTrue(main(cmd2) == 0)
        self.assertFalse(main(cmd3) == 0)
        self.assertFalse(main(cmd4) == 0)

        f = open(file_name + ".json", "r")
        content = json.load(f)
        f.close()

        os.remove(file_name + ".json")

        # Check task ids exist
        self.assertNotIn("1", content)
        self.assertIn("2", content)
        self.assertNotIn("3", content)

        self.assertTrue(content["2"]["desc"] == "task_2")

    def test_update(self) -> None:
        """
        Test updating exisitng tasks
        """
        file_name = "test_update_file"
        file_content = {
            "1": {
                "desc": "task_1",
                "status": "TODO",
                "createdAt": "Wed Jan  1 08:49:30 2025",
                "updatedAt": "Wed Jan  1 08:49:30 2025",
            },
            "2": {
                "desc": "task_2",
                "status": "TODO",
                "createdAt": "Wed Jan  1 08:49:30 2025",
                "updatedAt": "Wed Jan  1 08:49:30 2025",
            },
            "3": {
                "desc": "task_3",
                "status": "TODO",
                "createdAt": "Wed Jan  1 08:49:30 2025",
                "updatedAt": "Wed Jan  1 08:49:30 2025",
            },
            "last_id": 3,
        }

        f = open(file_name + ".json", "w")
        json.dump(file_content, f)
        f.close()

        cmd1 = [file_name, "update", 1, "updated_task_1"]
        cmd2 = [file_name, "update", 2, "updated_task_2"]
        cmd3 = [file_name, "update", 5, "updated_task_5"]
        cmd4 = [file_name, "update", 5]

        self.assertTrue(main(cmd1) == 0)
        self.assertTrue(main(cmd2) == 0)
        self.assertFalse(main(cmd3) == 0)
        self.assertFalse(main(cmd4) == 0)

        f = open(file_name + ".json", "r")
        content = json.load(f)
        f.close()

        os.remove(file_name + ".json")

        # Check task ids exist
        self.assertIn("1", content)
        self.assertIn("2", content)
        self.assertIn("3", content)

        self.assertTrue(content["1"]["desc"] == "updated_task_1")
        self.assertTrue(content["2"]["desc"] == "updated_task_2")
        self.assertTrue(content["3"]["desc"] == "task_3")

    def test_update_progress(self) -> None:
        """
        Test updating progress on exisitng tasks
        """
        file_name = "test_progress_update_file"
        file_content = {
            "1": {
                "desc": "task_1",
                "status": "TODO",
                "createdAt": "Wed Jan  1 08:49:30 2025",
                "updatedAt": "Wed Jan  1 08:49:30 2025",
            },
            "2": {
                "desc": "task_2",
                "status": "TODO",
                "createdAt": "Wed Jan  1 08:49:30 2025",
                "updatedAt": "Wed Jan  1 08:49:30 2025",
            },
            "3": {
                "desc": "task_3",
                "status": "TODO",
                "createdAt": "Wed Jan  1 08:49:30 2025",
                "updatedAt": "Wed Jan  1 08:49:30 2025",
            },
            "last_id": 3,
        }

        f = open(file_name + ".json", "w")
        json.dump(file_content, f)
        f.close()

        cmd1 = [file_name, "mark-in-progress", 1]
        cmd2 = [file_name, "mark-done", 2]
        cmd3 = [file_name, "mark-todo", 1]
        cmd4 = [file_name, "mark-in-progress", 3]

        cmd5 = [file_name, "mark-in-progress", 5]
        cmd6 = [file_name, "mark-in-progress"]
        cmd7 = [file_name, "mark-todo"]
        cmd8 = [file_name, "mark-done"]
        cmd9 = [file_name, "mark-done", "a"]
        cmd10 = [file_name]

        self.assertTrue(main(cmd1) == 0)
        self.assertTrue(main(cmd2) == 0)
        self.assertTrue(main(cmd3) == 0)
        self.assertTrue(main(cmd4) == 0)

        self.assertFalse(main(cmd5) == 0)
        self.assertFalse(main(cmd6) == 0)
        self.assertFalse(main(cmd7) == 0)
        self.assertFalse(main(cmd8) == 0)
        self.assertFalse(main(cmd9) == 0)
        self.assertFalse(main(cmd10) == 0)

        f = open(file_name + ".json", "r")
        content = json.load(f)
        f.close()

        os.remove(file_name + ".json")

        # Check task ids exist
        self.assertIn("1", content)
        self.assertIn("2", content)
        self.assertIn("3", content)

        self.assertTrue(content["1"]["status"] == "TODO")
        self.assertTrue(content["2"]["status"] == "Done")
        self.assertTrue(content["3"]["status"] == "In Progress")

    @patch("builtins.print")
    def test_listing_tasks_none_empty(self, mock_print: unittest.mock.Mock) -> None:
        """
        Test listing exisitng tasks, when task list is populated
        """
        file_name = "test_listing_file"
        file_content = {
            "1": {
                "desc": "task_1",
                "status": "TODO",
                "createdAt": "Wed Jan  1 08:49:30 2025",
                "updatedAt": "Wed Jan  1 08:49:30 2025",
            },
            "last_id": 3,
        }

        f = open(file_name + ".json", "w")
        json.dump(file_content, f)
        f.close()

        cmd = [file_name, "list"]
        self.assertTrue(main(cmd) == 0)
        self.assertEqual(
            mock_print.mock_calls,
            [
                call("""
ID: 1\n
Description: task_1\n
Status: TODO\n
Creation Time: Wed Jan  1 08:49:30 2025\n
Last Updated Time: Wed Jan  1 08:49:30 2025"""),
                call("_" * 60),
            ],
        )

        cmd = [file_name, "list", "In Progress"]
        self.assertTrue(main(cmd) == 0)
        self.assertEqual(
            mock_print.mock_calls,
            [
                call("""
ID: 1\n
Description: task_1\n
Status: TODO\n
Creation Time: Wed Jan  1 08:49:30 2025\n
Last Updated Time: Wed Jan  1 08:49:30 2025"""),
                call("_" * 60),
            ],
        )

        cmd = [file_name, "list", "TODO"]
        self.assertTrue(main(cmd) == 0)
        self.assertEqual(
            mock_print.mock_calls,
            [
                call("""
ID: 1\n
Description: task_1\n
Status: TODO\n
Creation Time: Wed Jan  1 08:49:30 2025\n
Last Updated Time: Wed Jan  1 08:49:30 2025"""),
                call("_" * 60),
                call("""
ID: 1\n
Description: task_1\n
Status: TODO\n
Creation Time: Wed Jan  1 08:49:30 2025\n
Last Updated Time: Wed Jan  1 08:49:30 2025"""),
                call("_" * 60),
            ],
        )

        os.remove(file_name + ".json")


if __name__ == "__main__":
    unittest.main()
