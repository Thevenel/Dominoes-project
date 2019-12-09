import random # To use later for a random shuffle
class Dominoes:

    def __init__(self, phase1, phase2):
        self.phase1 = phase1
        self.phase2 = phase2
    
    def __str__(self):
        return "{}|{}".format(self.phase1, self.phase2)
    
    def matchL(self, o):
        return self.phase1 == o.phase1 or self.phase2 == o.phase1

    def matchR(self, o):
        return self.phase1 == o.phase2 or self.phase2 == o.phase2

    def __eq__(self, o):
        if self.phase1 == o.phase1 and self.phase2 == o.phase2:
            return True
        elif self.phase1 == o.phase2 and self.phase2 == o.phase1:
            return True
        else:
            return False
        
class Players:
    def __init__(self, name):
        self.name = name
        self.pile = []
        self.passes = 0

    def __str__(self):
        string = self.name
        for tile in self.pile:
            string += tile
            string += '\n'
        return string

# Initialize the chain with add_left and add_right methods
    def add_left(self, chain, tile):
        if tile.phase2 == chain[0].phase1:
            chain.insert(0, tile)
            self.pile.remove(tile)
        elif tile.phase1 == chain[0].phase1:
            a = tile.phase1
            b = tile.phase2
            tile.phase1 = b
            tile.phase2 = a
            chain.insert(0, tile)
            self.pile.remove(tile)
        return chain
    
    def add_right(self, chain, tile):
        if tile.phase1 == chain[len(chain)-1].phase2:
            chain.append(tile)
            self.pile.remove(tile)
        elif tile.phase2 == chain[len(chain)-1].phase2:
            a = tile.phase1
            b = tile.phase2
            tile.phase1 = b
            tile.phase2 = a
            chain.append(tile)
            self.pile.remove(tile)
        return chain

    def player_turn(self, chain):
        for i in range(len(self.pile)): # print all tiles
                print(str(i + 1) + ") " + str(self.pile[i]))
    
        canPlay = False
        for tile in self.pile:
            if tile.matchL(chain[0]) or tile.matchR(chain[len(chain)-1]):
                canPlay = True
        if canPlay == False:
            self.passes += 1
            return chain
        
        elif canPlay == True:
                self.passes = 0
                for tile in self.pile:
                    if tile.matchL(chain[0]):
                        print(tile)
                        chain = self.add_left(chain, tile)
                        input("press enter to continue")
                        return chain
                    elif tile.matchR(chain[len(chain)-1]):
                        print(tile)
                        chain = self.add_right(chain, tile)
                        input("press input to continue") 
                        return chain
    
    def get_name(self):
        return self.name

    def get_pile(self):
        return self.pile

    def get_passess(self):
        return self.passes


class Robot(Players):
    def player_turn(self, chain):

        canPlay = False
        for tile in self.pile:
            if tile.matchL(chain[0]) or tile.matchR(chain[len(chain)-1]):
                canPlay = True
        if canPlay == False:
            print(self.name + ' has no playable dominoes.')
            self.passes +=1
            input("press enter to continue")
            return chain

        elif canPlay == True:
            self.passes = 0
            for tile in self.pile:
                if tile.matchL(chain[0]):
                    print(tile)
                    chain = self.add_left(chain, tile)
                    input("press enter to continue")
                    return chain
                elif tile.matchR(chain[len(chain)-1]):
                    print(tile)
                    chain = self.add_right(chain, tile)
                    input("press enter to continue")
                    return chain
    
def start_game():
    chain = [] # tiles of the chain
    completed_pile = [] # all the tiles
    # extra_tiles = [] # reserved piles
    
    for n in range(7): # add the tiles to completed_pile
        for i in range(0, n+1):
            completed_pile.append(Dominoes(n, i))
    random.shuffle(completed_pile)

# create the players
    
    c1 = Robot("Bot1")
    c2 = Robot("Bot2")
    c3 = Robot("Bot3")
    c4 = Robot("Bot4")

    # deal the game 
    input("Enter to start the game")
    player_list = [c1, c2, c3, c4]
    for player in player_list:
        for i in range(7):
            player.pile.append(completed_pile.pop())


    #Find the player with the 6-6 to start the game
    game_train = []
    for player in player_list:
        for tile in player.pile:
            if Dominoes(6,6) == tile:
                game_train.append(player) # This player starts the game
                chain.append(Dominoes(6,6))
                player.pile.remove(Dominoes(6,6))
                player_list.remove(player)
                print(player.name + ' has 6|6 and plays it to start the game')
    random.shuffle(player_list)
    for player in player_list:
        game_train.append(player)

    game_oder = "The game order is: "
    for player in game_train:
        game_oder += player.name
        game_oder += " "
    print(game_oder)
    input("Press enter to continue")

    player_number = 1

    # Take game into loop
    while True:
        print("\nThe current train is: ")
        for tile in chain:
            print(str(tile) + " ", end="")
        print('\n')


        chain = game_train[player_number].player_turn(chain)
        player_number = (player_number + 1) % 4

        # print(current_player)

start_game()