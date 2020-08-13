from random import randint

class Game():

    def ask(self):
        choice = input("Do you want to play again?(y/n): ").lower()
        return True if choice=="y" else False

    def generateRandomNumber(self):
        return randint(1,20)


    def game(self):
        # print("I am thinking of a number....")
        print("Now guess the number that I am thinking...")
        chances = 5
        playing = True
        number = self.generateRandomNumber()
        while playing:
            print(f"You have {chances} chances more.")
            guess = int(input("Enter your guess: "))
            if guess==number:
                print("Yay! You've guessed it right!")
                chances=5
                number = self.generateRandomNumber()
                playing = self.ask()
            elif guess>number:
                print("Too high..!")
                chances-=1
            else:
                print("Too low..!")
                chances-=1
            if chances==0:
                print("Sorry, you've ran out of moves. Here is then number: %d".format(number))
                number = self.generateRandomNumber()
                chances=5
                playing = self.ask()


# while playing:
#     if chances==0:
#         print("Sorry, you ran out of moves! Here is the number: %d"%(number))
#         break
#     guess = int(input("Guess it: "))
#     if guess == number:
#         print("Yay! You've guessed it correct!")
#         break
#     if guess > number:
#         print("Too high!")
#         chances-=1
#         print("You have %d chances more!.."%(chances))
#     else:
#         print("Too Low!")
#         chances-=1
#         print("You have %d chances more!.."%(chances))
# choice = input("\nDo you want to play again(y/n): ").lower()
# if choice=="y":
#     game()
# else:
#     print("Thank you for playing! Have a nice day!")


Game().game()