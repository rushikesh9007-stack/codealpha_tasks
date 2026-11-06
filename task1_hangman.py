"""
CodeAlpha Python Programming Internship — Task 1: Hangman Game
A simple console-based Hangman game using five predefined words.
"""

import random

WORDS = ["python", "computer", "coding", "program", "developer"]
MAX_INCORRECT_GUESSES = 6


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0

    print("=" * 35)
    print("          HANGMAN GAME")
    print("=" * 35)
    print("Guess the hidden word one letter at a time.")
    print(f"You can make at most {MAX_INCORRECT_GUESSES} incorrect guesses.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        display_word = " ".join(
            letter if letter in guessed_letters else "_" for letter in secret_word
        )
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses remaining: {MAX_INCORRECT_GUESSES - incorrect_guesses}")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You guessed the word: {secret_word}")
            return

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")

    print(f"\nGame over! The word was: {secret_word}")


if __name__ == "__main__":
    play_hangman()
