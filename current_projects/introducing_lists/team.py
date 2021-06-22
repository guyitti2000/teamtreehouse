# TODO Create an empty list to maintain the player names
roster= []


# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'

add_name = input("Would you like to add a player? (Y/N): ")
add_count = 1

while add_name.lower() == "y":
    if add_count == 4:
        print("\nSorry only 3 players allowed")
        break
    player_name = input("What is the player's name: ")
    roster.append(player_name.capitalize())
    add_name = input("\nAnother player? (Y/N): ")
    add_count += 1
print(roster)



# TODO print the number of players on the team

print("\nThere are {} players on the team.".format(len(roster)))  

# TODO Print the player number and the player name
# The player number should start at the number one
player_num = 1
for player in roster:
    print("Player {}: {}".format(player_num, player))
    player_num += 1


# TODO Select a goalkeeper from the above roster
keeper = input("\nPlease select a goalkeeper from the above roster (1-{}): ".format(len(roster)))

keeper = int(keeper)

# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("The goalkeeper will be {}".format(roster[keeper - 1]))
