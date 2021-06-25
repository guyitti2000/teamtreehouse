# class game


# grid size
# card options
# columns
# locations
# methods
     # create cards
     # create grid
     # check f0r matches
     # check game won
     # run the game
#dunder main
    #create game instance
    #call start game


'''
ON THE SECOND RUN THROUGH, COMMENT THROUGH THE CODE AND ALSO TRY TO PLAY WITH THE CODE, GET A GOOD GRASP OF IT
'''









from cards import Card
import random



class Game:

    def __init__(self):
        self.size = 4
        self.card_options = ['Add', 'Boo', 'Cat', 'Dev',
                             'Egg', 'Far', 'Gum', 'Hut']
        self.columns = ['A', 'B', 'C', 'D']
        self.cards = []
        self.locations = []
        for column in self.columns:
            for num  in range(1, self.size + 1):
                self.locations.append(f'{column}{num}')
                # appends the locations into the location attribute (review this)


    def set_cards(self):
        used_locations = []
        for word in self.card_options:
            for i in range(2):
                available_locations = set(self.locations) - set(used_locations)
                random_location = random.choice(list(available_locations))
                used_locations.append(random_location)
                card = Card(word, random_location)
                self.cards.append(card)

# locations
# methods
     # create cards
     # create grid
     # check f0r matches
     # check game won
     # run the game

#dunder main
if __name__ == '__main__':
    game = Game()
    game.set_cards()
    for card in game.cards:
        print(card)
    # call start game method
