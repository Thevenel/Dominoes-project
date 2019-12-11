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
            
    def get_phase1(self):
        return self.phase1
    
    def get_phase2(self):
        return self.phase2
        
class Players:
    def __init__(self, name):
        self.name = name
        self.pile = []
        self.passes = 0
        self.points = 0

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

    def get_passes(self):
        return self.passes
    
    

class Robot(Players):
    def player_turn(self, chain):
        print("It's " + self.name + "'s turn !\nThe tiles are:")
        for i in range(len(self.pile)): # print all tiles
            print(str(i+1) + ") " + str(self.pile[i]))

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
    
    def get_points(self):
        return self.points