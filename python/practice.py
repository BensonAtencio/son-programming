import threading
import random

y = ["r", "p", "s"]

z = y[random.randint(0, 2)]

print("This is a game of rock paper scissors, just press the esc key if you want to quit")

player = False
exit = False

def game():
    while player == False:
        x = input("Rock(r), Paper(p), Scissors(s): ")

        if(x == z):
            print("Draw")
            player = True
        else:
            print("tama condition")
            player = True

def exT():
    if(exit == True):
        player = True
        return player
    else:
        player = False
        return player

t1 = threading.Thread(target=game)

t1.start()