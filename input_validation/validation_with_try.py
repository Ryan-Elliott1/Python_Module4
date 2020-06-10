"""
Program: validation_with_try.py
Author: Ryan Elliott
Last date modified: 06/10/2020

This program takes information about the user and 3 test scores and outputs the average of their scores
input first and last name, age and 3 test scores
outputs users information and the average of their scores
"""


def average(score1, score2, score3):
    try:
        if score1 < 0:
            raise ValueError
        NUMBER_TESTS = 3
        return float((score1 + score2 + score3)/NUMBER_TESTS)
    except ValueError:
        raise ValueError
    print("no negative numbers")


if __name__ == '__main__':
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first name: ")
    age = input("Enter your age: ")
    s1 = input("Enter score 1: ")
    s2 = input("Enter score 2: ")
    s3 = input("Enter score 3: ")
    average_scores = average(int(s1), int(s2), int(s3))
    print(f'{last_name}, {first_name} age: {age} average grade: {average_scores:.2f}')

"""
test run 
Enter your last name: Sam
Enter your first name: Darnold
Enter your age: 25
Enter score 1: 98
Enter score 2: 88
Enter score 3: 91
Sam, Darnold age: 25 average grade: 92.33
"""
