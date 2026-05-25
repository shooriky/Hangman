import random

words = ["shelf", "book", "window", "door", "house", "tree", "bird", "ocean"]

def game():
    word = random.choice(words)
    tries = 6
    blanks = ["_"] * len(word)

    while tries > 0:
        print(" ".join(blanks))
        print("tries left:", tries)

        guess = input("what is your guess? ")

        # full word guess
        if guess == word:
            print("Congratulations! You guessed the word.")
            thx = input("thanks for playing!")
            return

        # single letter guess
        elif len(guess) == 1:
            if guess in word:
                print("Correct!")
                for i in range(len(word)):
                    if word[i] == guess:
                        blanks[i] = guess
            else:
                print("Wrong!")
                tries -= 1

        else:
            print("Sorry, that's not the word.")
            tries -= 1

        # check win
        if "_" not in blanks:
            print("You completed the word:", word)
            thx = input("thanks for playing!")
            return
            

    print("Game over. The word was:", word)
    thx = input("thanks for playing!")
def menu_Options():
    boot1 = input("enter your choice: ")
    if boot1 == "1":
        print("starting game...")
        game()
    elif boot1 == "2":
        print("quitting game...")
    else:
        print("invalid choice.")
        menu_Options()

print("hangman! The classic word guessing game.")
print("use numbers to navigate the game.")
print("1. play game")
print("2. quit")
menu_Options()