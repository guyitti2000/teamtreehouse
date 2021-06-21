name = input("Please enter your name: ")

n = int(input("Please enter a number: "))

# TODO: Make sure the number is an integer


print("Hello my sweet {}!\nThe number you have chosen is {}, and...".format(name,n))

# TODO: Print out the User's name and the number entered,
# making sure the two statements are on separate lines of output.


"""
is_fizz = n % 3 == 0
is_buzz =n % 5 == 0

Was supposed to do it like this for cleaner code.


"""





if n % 3 == 0 and n % 5 == 0:
    print(str(n) + ' is a FizzBuzz Number!')
elif n % 3 == 0 and n % 5 != 0:
    print(str(n) + ' is a Fizz number :(')
elif n % 3 != 0 and n % 5 == 0:
    print(str(n) + " is a Buzz number :(")
else:
    print(str(n) + " is neither a fizzy or buzzy number...grrrr")


# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************


# TODO: Define variables for is_fizz and is_buzz that stores 
# a Boolean value of the condition. Remember that the modulo operator, %, 
# can be used to check if there is a remainder.


# Using the variables, check the condition of the value, and print the necessary
# string




















