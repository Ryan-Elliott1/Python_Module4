"""
Program: basic_if-elif.py
Author: Ryan Elliott
Last date modified: 06/10/2020

This program takes the users input to subscribe them
input 1-5 for a subscription level
outputs users subscription and price
"""

if __name__ == '__main__':
    choice = input("Programmer's Toolkit Monthly Subscription Box Options: \n1. Platinum \n2. Gold \n3. Silver \n4. Bronze \n5. Free Trial\nPlease enter the "
                   "level you would like to subscribe to: ")

    if choice == "1":
        print("Platinum $60")
    elif choice == "2":
        print("Gold $50")
    elif choice == "3":
        print("Silver $40")
    elif choice == "4":
        print("Bronze $30")
    elif choice == "5":
        print("Free Trial Free!")
    else:
        print("Incorrect Input")

"""
input: 1
output: Platinum $60
input: 3
output: Silver $40
"""
