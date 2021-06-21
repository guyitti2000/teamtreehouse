import math


def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / number_of_people)

try: # possibly problematic code in the try block
    total_due = float(input("What is the total? "))
    number_of_people = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_people)

except ValueError as err: # there are different types of errors, you have to identify it one by one. This body is what will happen should the error happen.
    print("Oh no! That's not a valid value. Try again!")
    print("({})".format(err))

else: # want these in the body to run....only if there was a ValueError
    print("Each person owes ${}".format(amount_due))





# Well I deleted all my work by accident, so if y0u wanna check how to do ValueError stuff.. go to Python Basics: Functions and Loops in Team Treehouse
