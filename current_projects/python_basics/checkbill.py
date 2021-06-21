import math


def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)

total_due = float(input("What is the total? "))
number_of_people = int(input("How many people?  "))
amount_due = split_check(total_due, number_of_people)






print("Each person owes ${}".format(amount_due))


# Well I deleted all my work by accident, so if y0u wanna check how to do ValueError stuff.. go to Python Basics: Functions and Loops in Team Treehouse
