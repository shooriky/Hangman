import random

words = ["shelf", "book", "window", "door", "house", "tree", "bird", "ocean"]

def game():
    word = random.choice(words)
    tries = 6
    blanks = ["_"] * len(word)
    guessed = set()

    while tries > 0:
        print(" ".join(blanks))
        print("tries left:", tries)
        print("guessed letters:", " ".join(sorted(guessed)) if guessed else "-")

        guess = input("what is your guess? ").strip().lower()

        if not guess:
            print("Please enter a letter or a word.")
            continue

        # full word guess
        if len(guess) > 1:
            if guess == word:
                print("Congratulations! You guessed the word.")
                input("thanks for playing!")
                return
            else:
                print("Sorry, that's not the word.")
                tries -= 1
                continue

        # single letter guess
        if not guess.isalpha():
            print("Please enter a letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    blanks[i] = guess
        else:
            print("Wrong!")
            tries -= 1

        # check win
        if "_" not in blanks:
            print("You completed the word:", word)
            input("thanks for playing!")
            return

    print("Game over. The word was:", word)
    input("thanks for playing!")

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