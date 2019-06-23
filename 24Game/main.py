import random
from libs.game import Game_Main
from libs.calculator import Calc_Main

def Welcome():
    print("24 Calculator:")
    print("Enter 4 integers to calc 24.")
    print('Enter "game" to play the game')
    print('Enter "exit" to exit the program')

Welcome()
while True:
    command = input()
    if command == "exit":
        break
    elif command == "game":
        Game_Main()
        Welcome()
    else:
        Calc_Main(command)