#!/usr/bin/python




first_name = input("What is your first name?: ")
gender = input("What is your preferred gender?: ")


print("Hello, World and", first_name.capitalize())
if "G" in first_name and gender.lower() == "male":
    print(first_name.capitalize(), "is learning Python")
elif gender.lower() == "female":
    question = input("Are boys better than girls?: ")
    if question.lower() == "yes":
        print("You're not wrong...")
    elif question.lower() == "no":
        print("Are you sure...")
    else:
        print("What?")
else:
    print("You should totes learn some Pyth, {}!".format(first_name.capitalize()))
print("Have a great day {}!".format(first_name.capitalize()))
