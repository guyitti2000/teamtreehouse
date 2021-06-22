shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter "DONE" to stop adding items.
Enter "HELP" for this help.
Enter "SHOW" to see items in list.
""")


def add_to_list(item):
    shopping_list.append(item)
    print("{} was added.".format(item) + " There are {} items on the list currently".format(len(shopping_list)))


def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


show_help()
while True:
    new_item = input("> ")
    if new_item.lower() == "done":
        break
    elif new_item.lower() == "help":
        show_help()
        continue
    elif new_item.lower() == "show":
        show_list()
        continue 
    add_to_list(new_item.capitalize())

print("\nWe done!")
show_list()
