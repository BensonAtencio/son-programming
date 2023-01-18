import threading
import random
import keyboard
import sys

y = ["r", "p", "s"]

z = y[random.randint(0, 2)]

print("This is a game of rock paper scissors, just press the esc key if you want to quit")

player = False

def game():
    global player
    global z
    while player == False:

        x = input("Rock(r), Paper(p), Scissors(s): ")

        if(x == z):
            print(f"Draw, parehas kayo {x}, at {z}")
        elif(x == 'r'):
            if(z == 'p'):
                print(f"You lose, talo ng {z} ang {x}")
            elif(z == 's'):
                print(f"You win, talo ng {x} ang {z}")
        elif(x == 'p'):
            if(z == 's'):
                print(f"You lose, talo ng {z} ang {x}")
            elif(z == 'r'):
                print(f"You win, talo ng {x} ang {z}")
        elif(x == 's'):
            if(z == 'r'):
                print(f"You lose, talo ng {z} ang {x}")
            elif(z == 'p'):
                print(f"You win, talo ng {x} ang {z}")
        else:
            print("Bonak mali input mo")
            player == False

        z = y[random.randint(0, 2)]

def exT():
    global player
    exit = False

    while exit == False:
        a = keyboard.read_key()
        if(a == 'esc'):
        # if (msvcrt.kbhit() and ord(msvcrt.getch()) == 27):
            player = True
            print("\nThank you for playing")
            sys.exit()
        else:
            continue


t1 = threading.Thread(target=game, daemon = True)
t2 = threading.Thread(target=exT)

t1.start()
t2.start()