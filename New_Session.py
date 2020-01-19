# New_Session.py
import Utils

class New:
    Category = ["Personal", "Travel", "Food", "Other"]
    def selection(self):
        category = self.Category
        print("Please Choose the category of the Expense")
        for str in category:
            print(str)
        val = (input("Type: "))
        if val in category:
            print("Hi")


    def start(self, name):
        running = True
        while running:
            print("Hello " + name + " what would you like to do today? \n 1. Add Expense \t 2.Go back")
            val = input("Input: ")
            if int(val) == 1 and Utils.check_int(val):
                self.selection()
            elif int(val) == 2 and Utils.check_int(val):
                break
            else:
                print("Invalid please Enter in a number")
                continue

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.start(name)


    def print_details(self):
        print("Well then your name is " + self.name + " and your age is " + str(self.age))


