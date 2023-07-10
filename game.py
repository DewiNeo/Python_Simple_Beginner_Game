import random
import string

from teks import Teks
from hangmanWords import hangmanWords

class GuessNumber:
    def UserGuessNumber(len):
        low = 0
        high = len
        answer = ''
        guess = random.randint(low, high)
        while answer != guess:
            print("\nguess the secret number here")
            try:
                answer = int(input(">>> "))
            except ValueError:
                Teks.wrongValue(self=Teks)
                continue
            if answer > guess:
                print("your number is to high!! lets try again!")
            elif answer < guess:
                print("your answer is to low!! lets try again")
            elif answer == guess:
                Teks.youwin(self=Teks)
                print("----------")
                print(f"YAY!! {answer} is the correct number!!")

    def ComputerGuessNumber(len):
        low = 0
        high = len
        answer = ''
        while answer != 'c':
            guess = random.randint(low, high)
            try:
                print(f"\n{guess} is too high (H) or to low(L) or correct (C)?")
                answer = input(">>> ").lower()
                if answer != 'h' and answer != 'l' and answer != 'c':
                    print("the answer must be 'H' for high, 'L' for low and 'C' for correct!")
                    Teks.enter(self=Teks)
            except ValueError:
                print("Ups!!... something when wrong.")
                break
            # answer.lower()
            if answer == "h":
                high = guess - 1
            elif answer == "l":
                low = guess + 1
        if answer == 'c':
            Teks.youwin(self=Teks)
            print("----------")
            print(f"YAY!! {guess} is the correct number!!")



class RPS:
    def playRockPaperScissors(self):
        print("'r' for rock || 'p' for paper || 's' for scissors!")
        user = input("input your choise [ r | p | s ] >> ").lower()
        computer = random.choice(['r', 'p', 's'])

        print("computer: " + computer)
        print("You: " + user)

        if user == computer:
            Teks.draw(self=Teks)
        elif self.win(user, computer):
            Teks.youwin(self=Teks)
        else:
            Teks.youlose(self=Teks)

    def win(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (
                player == 's' and opponent == 'p'):
            return True


class hangman:
    def getValidWord(hangmanWords):
        word = random.choice(hangmanWords)
        while ' ' in word or '-' in word:
            word = random.choice(hangmanWords)
        return word.upper()

    def hangman(self):
        word = self.getValidWord(hangmanWords)
        word_letters = set(word)
        alphabeth = set(string.ascii_uppercase)
        used_letters = set()

        life = 6
        print("\n\nHEY lets play HANGMAN!!")
        print("---------------------------")
        while len(word_letters) > 0 and life > 0: \
                # letters used
            # ' '.join(['a','b','c', 'd']) -->> 'a b c d'
            if life == 6:
                print(f"\nyou have {life} life")
            else:
                print(f'\n\nyou have {life} life left')
            print('you had used this letter:: ', ' '.join(used_letters))

            # what current word is (ex. c-c-nu-)
            wordList = [letter if letter in used_letters else '-' for letter in word]
            print('Current Word:: ', ' '.join(wordList))

            user_letter = input('Guess a letter >>>  ').upper()
            if user_letter in alphabeth - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    life -= 1
            elif user_letter in used_letters:
                print('\n\nyou already used the character. Please try again')
                Teks.enter(self=Teks)
            else:
                print('\n\nInvalid Character')
        if life == 0:
            print("\n\nups sorry, u died. The word was '", word, "'")
        else:
            print("\n\nYAY YOU SURVIVE!!")
            print("'", word, "'is the correct word! ^^")

