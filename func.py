import json
from datetime import datetime, timedelta
from os import path
import pprint


class ToDoManager:

    def __init__(self):
        self.date = datetime.now().replace(second=0, microsecond=0)
        self.__json_arr = []
        if path.isfile("database.json"):
          self.__json_arr = json.load(open("database.json"))

    def create(self, task, deadline):
        data = {}
        id_counter = 1 if len(self.__json_arr) == 0 else self.__json_arr[-1]["ID"] + 1
        data["ID"] = id_counter
        data["Created"] = str(self.date)
        data["Task"] = task
        data["Status"] = "Undone"
        data["Deadline"] = str(self.date + timedelta(days=deadline))
        self.__json_arr.append(data)

        with open("database.json", "w+", encoding="utf-8") as file:
            file.write(json.dumps(self.__json_arr, indent=4))

    def read(self, id):
        for item in self.__json_arr:
            if item["ID"] == id:
                return item
        return f"No task with ID: {id}!"

    def update(self, id):
        choice = input("What do you want to update?\n1: Task\n2: Deadline\nEnter your choice>> ")
        if choice.lower() == "1":
            new_task = input("Enter edited task>> ")
            for item in self.__json_arr:
                if item["ID"] == id:
                    item["Task"] = new_task
        else:
            print("Deadline has to be given in number of days, starting from now.")
            new_deadline = int("Enter new deadline>> ")
            for item in self.__json_arr:
                if item["ID"] == id:
                    item["Deadline"] = self.date + timedelta(days=new_deadline)

        with open("database.json", "w+", encoding="utf-8") as file:
            file.write(json.dumps(self.__json_arr, indent=4))

    def markAsDone(self, id):
        for item in self.__json_arr:
            if item["ID"] == id:
                item["Status"] = "Done"
        with open("database.json", "w+", encoding="utf-8") as file:
            file.write(json.dumps(self.__json_arr, indent=4))

    def markAsUndone(self, id):
        for item in self.__json_arr:
            if item["ID"] == id:
                item["Status"] = "Undone"
        with open("database.json", "w+", encoding="utf-8") as file:
            file.write(json.dumps(self.__json_arr, indent=4))

    def delete(self, id):
        for item in self.__json_arr:
            if item["ID"] == id:
                self.__json_arr.remove(item)
        with open("database.json", "w+", encoding="utf-8") as file:
            file.write(json.dumps(self.__json_arr, indent=4))

    def sort(self):
        choice = input("Do you want to sort by:\n1: Date created\n2: Deadline\nEnter your choice>> ")
        if choice == "1":
            sortedlist = sorted(self.__json_arr, key=lambda d: d["Created"])
        else:
            sortedlist = sorted(self.__json_arr, key=lambda d: d["Deadline"])
        for item in sortedlist:
            for k, v in item.items():
                print(f"{k}: {v}")
            print("")

    def filter(self):
        choice = input("Do you want to filter by:\n1: Done\n2: Undone\nEnter your choice>> ")
        if choice == "1":
            filteredlist = [task for task in self.__json_arr if task["Status"] == "Done"]
        else:
            filteredlist = [task for task in self.__json_arr if task["Status"] == "Undone"]
        if len(filteredlist) == 0:
            print("No tasks with such status!")
        for item in filteredlist:
            for k, v in item.items():
                print(f"{k}: {v}")
            print("")

    def showAll(self):
        for item in self.__json_arr:
            for k, v in item.items():
                print(f"{k}: {v}")
            print("")

manage = ToDoManager()

manage.showAll()

