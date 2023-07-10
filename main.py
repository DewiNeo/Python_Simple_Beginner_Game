from game import GuessNumber
from game import RPS
from game import hangman
from teks import Teks

def menu():
    while True:
        print("\n\n\n\n\n\n")
        print("let's play secret number game!!")
        print("-------------------------\n")
        print("1. You Guess the secret number")
        print("2. Computer guess your number")
        print("3. Rock Paper and Scissors")
        print("4. Hangman")
        print("5. exit game :(")
        try:
            print("\nplease input menu number [1-5]")
            menuInsert = int(input(">>> "))
        except ValueError:
            Teks.wrongInput(self=Teks)
            continue


        if 0 < menuInsert <= 5:
            length = 0
            while length <= 0 and menuInsert != 5 and menuInsert <= 2:
                try:
                    print("\nplease enter the maximum number")
                    length = int(input(">>> "))
                except ValueError:
                    Teks.wrongValue(self=Teks)
                    continue

                if length <= 0:
                    print("\nsorry, number must be above 0!!")
                    input("press enter to try again..")
                # else:
            match menuInsert:
                case 1:
                    GuessNumber.UserGuessNumber(length)
                    Teks.enter(self=Teks)
                case 2:
                    GuessNumber.ComputerGuessNumber(length)
                    Teks.enter(self=Teks)
                case 3:
                    RPS.playRockPaperScissors(self=RPS)
                    Teks.enter(self=Teks)
                case 4:
                    hangman.hangman(self=hangman)
                    Teks.enter(self=Teks)
                case 5:
                    print("are you sure you want to exit [ Y (yes) / N (no)]?")
                    yesno = input(">>> ").lower()
                    if yesno == 'y' or yesno == 'yes':
                        break
                    elif yesno != 'n' and yesno != 'no' and yesno != 'y' and yesno != 'yes':
                        print("input must be Yes [Y] or No [N]!")
                        Teks.enter(self=Teks)

        else:
            Teks.wrongInput(self=Teks)

if __name__ == '__main__':
    menu()

