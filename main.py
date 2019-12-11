import random # To use later for a random shuffle
# import the classes for classes.py
from classes import Dominoes
from classes import Players
from classes import Robot
        
def start_game():
    chain = [] # tiles of the chain
    completed_pile = [] # all the tiles
    extra_tiles = [] # reserved piles
    
    for n in range(7): # add the tiles to completed_pile
        for i in range(0, n+1):
            completed_pile.append(Dominoes(n, i))
    random.shuffle(completed_pile)

# create the players
    c4 = Robot("Bot4")
    c1 = Robot("Bot1")
    c2 = Robot("Bot2")
    c3 = Robot("Bot3")
    
    # deal the game 
    input("Enter to start the game")
    player_list = [c1, c2, c3, c4]
    for player in player_list: #give each player 7 tiles to start the game
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
        # print('this =>', chain)

    #Games Over phase
    #There is two ways the domino can close 
    # When a pile is empty and when everyone is passed
    #The winner by emptying pile
        if len(game_train[player_number].get_pile()) == 0: 
            total_dots = 168
            points = 0
            for tile in chain:
                c = (str(tile))
                d = eval(c.replace("|", "+"))
                points  += d
                result = total_dots - points
            print(game_train[player_number].get_name() + " played their final domino! \n" + \
            game_train[player_number].name + " wins! with " + str(result) + " points")
            break

        #Win by block
        number_of_passes = 0
        for player in game_train:
            if player.get_passes()>= 1:
                number_of_passes += 1
        
        if number_of_passes == 4:
            print("No one has playable dominoes. The last player to play a domino was " +\
            (game_train[player_number].get_name() + "."))
            # print(number_of_points)
            total_dots = 168
            points = 0
            for tile in chain:
                c = (str(tile))
                d = eval(c.replace("|", "+"))
                points  += d
                result = total_dots - points
            print(game_train[player_number].get_name() + " wins! with " + str(result) + " points")
            break

        player_number = (player_number + 1) % 4
        

        
start_game()











