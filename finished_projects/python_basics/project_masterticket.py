import sys

TICKET_PRICE = 10
tickets_remaining = 100
service_charge = 2

def calculate_price(num_tickets):
    return num_tickets * TICKET_PRICE + (service_charge)

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?: ")
    num_tickets = input("How many tickets would you like, {}? ".format(name))
    num_tickets = int(num_tickets)

    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("Only {} tickets are available, my dude.".format(tickets_remaining)) #grammar error when there is only one ticket
    except ValueError as err:
        print("Oh no, we ran into an error, please try again ({})".format(err))
    else:
        amount_due = calculate_price(num_tickets) 
        print("The total due is ${}".format(amount_due))

        should_proceed = input("Do you want to proceed? Y/N ")
        attempt_count = 1

        while should_proceed.lower() != "y":
            if attempt_count > 1:
                sys.exit("Your lost...idjit")
            should_proceed = input("Don't make a mistake, do you want the tickets?: Y/N ")
            attempt_count += 1 
        else:
            print("SOLD!")
            tickets_remaining -= num_tickets

print ("Sorry the tickets are all sold out!!! :(")


