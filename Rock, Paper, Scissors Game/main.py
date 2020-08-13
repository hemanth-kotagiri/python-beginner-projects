import sys
import random
import os
count = 0
def game():
    global count
    os.system('cls')
    moves = ["ROCK","PAPER","SCISSORS"]
    if count==0:print("Let's play some Rock Paper Scissors!") # This statement appears only when the game is runned for the first time
    else:
       if count-1: print("Lets play "+"again, "*(count-1) + "and again..")
       else: print("Let's play again..")
    while True:
        given = input("Your move: ").upper()
        if given == "EXIT": 
            "Handles if the given input is exit"
            os.system('cls')
            print("Thank you for playing! Have a nice day!")
            sys.exit(0)
        if given in moves:
            CompChoice = random.choice(moves)
            print("Computer move: %s\n"%(CompChoice))
            if given == CompChoice:
                print("Its a TIE. Try again!...")
                continue
            if (given=="ROCK" and CompChoice=="SCISSORS") or (given=="SCISSORS" and CompChoice=="PAPER"):
                print("\nYay! You won!")
                break
            else:
                print("\nSorry! Computer won!")
                break
        else:
            print("\nPlease enter only valid input")

    choice = input("Want to play again?(y/n): ").lower()
    if choice=="y":
        count+=1
        game()
    else:
        os.system('cls')
        print("Thank you for playing! Have a nice day!")

if __name__ == "__main__":
    game()
