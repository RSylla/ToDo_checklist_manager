from func import ToDoManager

"""
Siia tuleb kirjutada Mainloop.
Programm peab jooksma While loopis, kuniks kasutaja
otsustab selle sulgeda valikvastuse abil.

Esimese ringi valikud on:
    - C: Create new task
    - R: Read all tasks
    - S: Sort tasks (küsib, kas by 1: creation or 2: deadline date)
    - F: Filter tasks (küsib, kas by done või undone)
    - E: Exit program
"""

def main():


    print(" _____                         _    _____         _      _____                   \n"
          "|  _  |___ ___ ___ ___ ___ ___| |  |_   _|___ ___| |_   |     |___ ___ ___ ___ ___ ___ \n"
          "|   __| -_|  _|_ -| . |   | .'| |    | | | .'|_ -| '_|  | | | | .'|   | .'| . | -_|  _|\n"
          "|__|  |___|_| |___|___|_|_|__,|_|    |_| |__,|___|_,_|  |_|_|_|__,|_|_|__,|_  |___|_|  \n"
          "                                                                          |___|         \n")



    manager = ToDoManager(db_file="database.json")
    while True:
        choice = input("\nC: Create new task\n"
                       "R: Read all tasks\n"
                       "E: Exit program\n\n"
                       "What would you like to do? >> ").lower()


        if choice == "m":
            print("ToDoManager - an interface to create and sort your tasks ")


            if choice == "me":
                continue




        if choice == "c":
            task = input("Please enter your new task. >> ")
            deadline = int(input("Enter a deadline in number of days.\n (0 if no deadline) >> "))
            manager.create(task, deadline)

        elif choice == "r":
            print("")
            manager.showAll()
            choice = input("\nC: Choose a specific task\n"
                           "S: Sort tasks by date of creation or deadline\n"
                           "F: Filter tasks by 'Done' or 'Undone'\n"
                           "B: Back to main menu\n\n"
                           "What would you like to do next? >> ").lower()

            if choice == "c":
                id = int(input("\nEnter #ID of selected task. >> "))
                manager.read(id)

                choice = input("\nE: Edit a task\n"
                               "D: Delete a task\n"
                               "MD: Mark task as Done\n"
                               "MU: Mark task as Undone\n"
                               "B: Back to main menu\n\n"
                               "What would you like to do next? >> ").lower()
                if choice == "e":
                    manager.update(id)
                    manager.read(id)


                elif choice == "d":
                    manager.delete(id)
                    manager.showAll()

                elif choice == "md":
                    manager.markAsDone(id)
                    manager.read(id)

                elif choice == "mu":
                    manager.markAsUndone(id)
                    manager.read(id)

                elif choice == "B":
                    continue

            elif choice == "s":
                manager.sort()

            elif choice == "f":
                manager.filter()

            elif choice == "b":
                continue




        elif choice == "e":
            print("Closing program...")
            break


if __name__ == "__main__":
        try:
            main()
        except:
            print("\nOops, something went wrong...\n"
                  "Closing program...")