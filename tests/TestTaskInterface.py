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


if __name__ == "__main__":
    unittest.main()