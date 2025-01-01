import unittest
from unittest.mock import patch, call
import json
import os

from TaskInterface.TaskInterface import TaskInterface

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

        test_add_interface = TaskInterface(file_name)

        # Add 3 tasks
        test_add_interface.add_task("task_1")
        test_add_interface.add_task("task_2")
        test_add_interface.add_task("task_3")
        
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
            "1":{"desc": "task_1", "status": "TODO", "createdAt": "Wed Jan  1 08:49:30 2025", "updatedAt": "Wed Jan  1 08:49:30 2025"}, 
            "2": {"desc": "task_2", "status": "TODO", "createdAt": "Wed Jan  1 08:49:30 2025", "updatedAt": "Wed Jan  1 08:49:30 2025"},
            "3": {"desc": "task_3", "status": "TODO", "createdAt": "Wed Jan  1 08:49:30 2025", "updatedAt": "Wed Jan  1 08:49:30 2025"},
            "last_id": 3
            }

        f = open(file_name + ".json", "w")
        json.dump(file_content, f)
        f.close()        

        test_delete_interface = TaskInterface(file_name)

        # Delete tasks 1 and 3
        self.assertTrue(test_delete_interface.delete_task(1))
        self.assertTrue(test_delete_interface.delete_task(3))

        self.assertFalse(test_delete_interface.delete_task(5))
        
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
            "1":{"desc": "task_1", "status": "TODO", "createdAt": "Wed Jan  1 08:49:30 2025", "updatedAt": "Wed Jan  1 08:49:30 2025"}, 
            "2": {"desc": "task_2", "status": "TODO", "createdAt": "Wed Jan  1 08:49:30 2025", "updatedAt": "Wed Jan  1 08:49:30 2025"},
            "3": {"desc": "task_3", "status": "TODO", "createdAt": "Wed Jan  1 08:49:30 2025", "updatedAt": "Wed Jan  1 08:49:30 2025"},
            "last_id": 3
            }

        f = open(file_name + ".json", "w")
        json.dump(file_content, f)
        f.close()        

        test_update_interface = TaskInterface(file_name)

        # Update tasks 1 and 2
        self.assertTrue(test_update_interface.update_task(1, "updated_task_1"))
        self.assertTrue(test_update_interface.update_task(2, "updated_task_2"))

        self.assertFalse(test_update_interface.update_task(5, "updated_task_5"))
        
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
            "1":{"desc": "task_1", "status": "TODO", "createdAt": "Wed Jan  1 08:49:30 2025", "updatedAt": "Wed Jan  1 08:49:30 2025"}, 
            "2": {"desc": "task_2", "status": "TODO", "createdAt": "Wed Jan  1 08:49:30 2025", "updatedAt": "Wed Jan  1 08:49:30 2025"},
            "3": {"desc": "task_3", "status": "TODO", "createdAt": "Wed Jan  1 08:49:30 2025", "updatedAt": "Wed Jan  1 08:49:30 2025"},
            "last_id": 3
            }

        f = open(file_name + ".json", "w")
        json.dump(file_content, f)
        f.close()        

        test_progress_interface = TaskInterface(file_name)

        # Update tasks 1, 2 and 3
        self.assertTrue(test_progress_interface.update_task_progress(1, "In Progress"))
        self.assertTrue(test_progress_interface.update_task_progress(2, "Done"))
        self.assertTrue(test_progress_interface.update_task_progress(1, "TODO"))
        self.assertTrue(test_progress_interface.update_task_progress(3, "In Progress"))
        
        self.assertFalse(test_progress_interface.update_task_progress(1, "in prog"))
        self.assertFalse(test_progress_interface.update_task_progress(5, "Done"))
        
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

    @patch('builtins.print')
    def test_listing_tasks_none_empty(self, mock_print: unittest.mock.Mock) -> None:
        """
        Test listing exisitng tasks, when task list is populated
        """
        file_name = "test_listing_file"
        file_content = {
            "1":{"desc": "task_1", "status": "TODO", "createdAt": "Wed Jan  1 08:49:30 2025", "updatedAt": "Wed Jan  1 08:49:30 2025"}, 
            "last_id": 3
            }

        f = open(file_name + ".json", "w")
        json.dump(file_content, f)
        f.close()        

        test_list_interface = TaskInterface(file_name)

        test_list_interface.list_tasks()
        self.assertEqual(mock_print.mock_calls, [
            call('''
ID: 1\n
Description: task_1\n
Status: TODO\n
Creation Time: Wed Jan  1 08:49:30 2025\n
Last Updated Time: Wed Jan  1 08:49:30 2025'''),
            call("_" * 60)])     

        test_list_interface.list_tasks("In Progress")
        self.assertEqual(mock_print.mock_calls, [
            call('''
ID: 1\n
Description: task_1\n
Status: TODO\n
Creation Time: Wed Jan  1 08:49:30 2025\n
Last Updated Time: Wed Jan  1 08:49:30 2025'''),
            call("_" * 60)])   

        test_list_interface.list_tasks("TODO")
        self.assertEqual(mock_print.mock_calls, [
            call('''
ID: 1\n
Description: task_1\n
Status: TODO\n
Creation Time: Wed Jan  1 08:49:30 2025\n
Last Updated Time: Wed Jan  1 08:49:30 2025'''),
            call("_" * 60),
            call('''
ID: 1\n
Description: task_1\n
Status: TODO\n
Creation Time: Wed Jan  1 08:49:30 2025\n
Last Updated Time: Wed Jan  1 08:49:30 2025'''),
            call("_" * 60)])  

        os.remove(file_name + ".json")   

if __name__ == "__main__":
    unittest.main()