'''

some methods: 
.insert(0, "string")
.pop() #will remove an object from list
.copy()

'''

books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]


# books[len(books) -1] (to get the last book) or do books[-1]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

def display_wishlist(display_name, wishes):
    items = wishes.copy()
    print(display_name + ":")
    suggested_gift = items.pop(0)
    print("=======>", suggested_gift, "<=======")
    for item in items:
        print("* " + item)
    print()

display_wishlist("Books", books)
display_wishlist("Video Games", video_games)
display_wishlist("Video Games 2", video_games)

