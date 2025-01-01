import unittest
import json
import os

from TaskInterface.TaskInterface import TaskInterface

class TestInterface(unittest.TestCase):
    def test_add(self):
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

        # Check task ids exit
        self.assertIn("1", content)
        self.assertIn("2", content)
        self.assertIn("3", content)
    
        self.assertTrue(content["1"]["desc"] == "task_1")
        self.assertTrue(content["2"]["desc"] == "task_2")
        self.assertTrue(content["3"]["desc"] == "task_3")

    def test_delete(self):
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

        # Add 3 tasks
        test_delete_interface.delete_task(1)
        test_delete_interface.delete_task(3)
        
        f = open(file_name + ".json", "r")
        content = json.load(f)
        f.close()

        os.remove(file_name + ".json")

        # Check task ids exit
        self.assertNotIn("1", content)
        self.assertIn("2", content)
        self.assertNotIn("3", content)
    
        self.assertTrue(content["2"]["desc"] == "task_2")

    def test_update(self):
        """
        Test updating exisitng tasks
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

        test_update_interface = TaskInterface(file_name)

        # Add 3 tasks
        test_update_interface.update_task(1, "updated_task_1")
        test_update_interface.update_task(2, "updated_task_2")
        
        f = open(file_name + ".json", "r")
        content = json.load(f)
        f.close()

        os.remove(file_name + ".json")

        # Check task ids exit
        self.assertIn("1", content)
        self.assertIn("2", content)
        self.assertIn("3", content)
    
        self.assertTrue(content["1"]["desc"] == "updated_task_1")
        self.assertTrue(content["2"]["desc"] == "updated_task_2")
        self.assertTrue(content["3"]["desc"] == "task_3")


if __name__ == "__main__":
    unittest.main()