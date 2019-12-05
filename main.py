import random # To use later for a random shuffle


class Dominoes:

    def __init__(self, phase1, phase2):
        self.phase1 = phase1
        self.phase2 = phase2
    
    def structure(self, bones):
        self.bones = []
        return self.bones.append(self.phase1 + '-' + self.phase2)
    
    def matchL(self, o):
        return self.phase1 == o.phase1 or self.phase2 == o.phase1

    def matchR(self, o):
        return self.phase1 == o.phase2 or self.phase2 == o.phase1

    def __eq__(self, o):
        if self.phase1 == o.phase1 or self.phase2 == o.phase2:
            return True
        elif self.phase1 == o.phase2 or self.phase2 == o.phase1:
            return True
        else:
            return False
        
class Players:
    def __init__(self, player1):
        self.player1 = player1
        self.pile = []
        self.passes = 0



# Initialize the chain with add_left and add_right methods

    def add_left(self, chain, tile):
        if tile.phase2 == chain[0].phase1:
            chain.insert(0, phase1)
            pile.remove(phase1)
        elif tile.phase1 == chain[0].phase1:
            a = phase1
            b = phase2
            tile.phase2 = a
            tile.phase1 = b
            chain.append(0, tile)
            pile.remove(tile)
        else:
            return chain
    
    def add_right(self, chain, tile):
        if tile.phase1 == chain[len(chain)-1].phase2:
            chain.append(tile)
            pile.remove(tile)
        elif tile.phase2 == chain[len(chain)-1].phase2:
            a = phase1
            b = phase2
            tile.phase2 = a
            tile.phase1 = b
            chain.append(tile)
            pile.remove(tile)
        else:
            return chain

class Robot(Players):
    pass




def start_game():
    chain = []
    shuffles = []
    extra_tiles = []
    
    for n in range(7):
        for i in range(0, n+1):
            shuffles.append(Dominoes(n, i))
    random.shuffle(shuffles)

# create the two players

player = Players(player1)
computer = Robot("computer")

# deal the game for 2 players

player_list = [player, computer]
    for player in player_list:
        for i in range(7):
            player.pile.append(shuffles.pop())


#Find the player with the 6-6 to start the game
game_train = []
for player in player_list:
    if


print(start_game())