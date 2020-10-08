import random

#classes/objects
class Player:
    def __init__(self,name,tile=0):
        self.name = name
        self.tile = tile

    def printtile(self):
        print(self.name + ": tile:" +str(self.tile))

class Snake:
    def __init__(self,head,tail):
        self.head = head
        self.tail = tail

class Snakegrp:
    def __init__(self,snakes = []):
        self.snakes = snakes
        snakes.append(Snake(31,4))
        snakes.append(Snake(16,8))
        snakes.append(Snake(47,25))
        snakes.append(Snake(66,52))
        snakes.append(Snake(63,60))
        snakes.append(Snake(97,75))

    def snakecheck(self,player):
        for x in self.snakes:
            if(player.tile == x.head):
                print("oops you landed on a snake! you are on tile: " + str(x.tail))
                player.tile = x.tail

class Ladder:
    def __init__(self,top,bottom):
        self.top = top
        self.bottom = bottom

class Laddergrp:
    def __init__(self,ladder = []):
        self.ladder = ladder
        ladder.append(Ladder(39,3))
        ladder.append(Ladder(12,10))
        ladder.append(Ladder(53,27))
        ladder.append(Ladder(84,56))
        ladder.append(Ladder(99,61))
        ladder.append(Ladder(90,72))

    def laddercheck(self,player):
        for x in self.ladder:
            if(player.tile == x.bottom):
                print("Wow you landed on a Ladder! you are on tile: " + str(x.top))
                player.tile = x.top


class Dice:
    def __init__(self,no):
        self.no = no

    def roll(self):
        dice_value = random.randint(1, self.no*6)
        print("Its a " + str(dice_value))
        return dice_value

class Board:
    def __init__(self,tiles,playerlist=[]):
        self.tiles = tiles
        self.playerlist = playerlist

    def playerscheck(self):
        snakes = Snakegrp()
        ladder = Laddergrp()
        i=1
        while i:
            for x in playerlist:
                input(x.name + ": Press enter to roll the dice: you are on tile: "+ str(x.tile))
                diecount = dice.roll()
                if(diecount == 6):
                    input(x.name + ": Press enter to roll the dice: you are on tile: "+ str(x.tile))
                    diecount += dice.roll()
                    if(diecount == 6):
                        input(x.name + ": Press enter to roll the dice: you are on tile: "+ str(x.tile))
                        diecount += dice.roll()
                        if(diecount == 6):
                            print(x.name + ": Opps 3 times 6 drowned your chance")
                            diecount = 0
                if(x.tile + diecount > boardsize):
                    print("you need "+ str(boardsize - x.tile) +" to win.")
                elif(x.tile + diecount == boardsize):
                    print(x.name+" : you win!!!")
                    i = 0
                    break
                else:
                    x.tile += diecount
                    snakes.snakecheck(x)
                    ladder.laddercheck(x)
      
#functions
#welcome message
def welcome_msg(boardsize):
    msg = """
    Snake and Ladder.(V1.0.0)
    At first the players are at 0th tile.
    The first to reach """+str(boardsize)+"""th tile is the winner.
    """
    print(msg)

#execution
boardsize = 100
diceno = 1
board = Board(boardsize)
dice = Dice(diceno)
no_of_player = 2
playerlist = []
for x in range(int(no_of_player)):
    name = input("enter the name of player" + str(x+1) + ":")
    player = Player(name)
    playerlist.append(player)
board.playerlist = playerlist
welcome_msg(boardsize)
board.playerscheck()