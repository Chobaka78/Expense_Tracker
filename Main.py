"""
# Main.py
# Usman Farooqi
# Expense_Tracker
# This is the main class
"""

# Importing Other classes
import Utils
# Methods needed in the class



class Main:
    import New_Session
    new_session = New_Session.New

    # Initialize static variable
    running = True
    # Starting the program
    while running:
        print("Welcome to Expense Tracker!")
        print("###########################")
        print("Please Enter: \n 1. For New session \t 2. To load a session \t 3. to Quit")
        ans = int(input("Input: "))

        if ans == 1:
            print("Hello there")
            print("################")
            while True:
                print("What is your name?")
                name = input("Input: ")
                print("What is your age?")
                age = input("Input: ")
                if Utils.check_str(name) and Utils.check_int(age):
                    Option1 = New_Session.New(name, age)
                    break
                else:
                    print("Invalid please enter String for name and int for age")
                    continue

        elif ans == 2:
            print("Why")

        elif ans == 3:
            print("Ok good bye")
            break




    
