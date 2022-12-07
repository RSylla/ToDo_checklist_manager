import unittest
from func import ToDoManager

class TestToDoManager(unittest.TestCase):
    def setUp(self):
        self.obj=ToDoManager("test.json")

    def test_create(self):
        self.obj.create(task="Drink water", deadline=1)
        self.assertTrue(self.obj.get_json_arr()[-1]["Task"] == "Drink water")
        self.assertFalse(self.obj.get_json_arr()[-1]["Task"] == "aidnoanfon")

    def test_markAsDone(self):
        self.obj.markAsDone(2)
        for item in self.obj.get_json_arr():
            if item["ID"] == 2:
                self.assertFalse(item["Status"] == "Undone")
                self.assertTrue(item["Status"] == "Done")

    def test_markAsUndone(self):
        self.obj.markAsUndone(3)
        for item in self.obj.get_json_arr():
            if item["ID"] == 3:
                self.assertFalse(item["Status"] == "Done")
                self.assertTrue(item["Status"] == "Undone")

    def test_delete(self):
        respons = "No task with ID: 6!"
        self.obj.delete(6)
        self.assertTrue(self.obj.read(6) == respons)
