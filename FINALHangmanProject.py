
# hangman_refactored.py

import random
import time
import turtle

WORDS = ['Thunder', 'Microwave', 'Geography', 'Algorithm', 'Computer']

class Validator:
    @staticmethod
    def is_valid_letter(letter):
        return letter.isalpha() and len(letter) == 1

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1

class HangmanGame:
    def __init__(self, word=None):
        self.word = (word or random.choice(WORDS)).lower()
        self.display = ['_' for _ in self.word]
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect = 6

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            print("You already guessed that letter.")
            return False
        self.guessed_letters.add(letter)
        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.display[i] = letter
            return True
        else:
            self.incorrect_guesses += 1
            return False

    def is_won(self):
        return '_' not in self.display

    def is_lost(self):
        return self.incorrect_guesses >= self.max_incorrect

    def show_progress(self):
        print("Word: " + ' '.join(self.display))

class HangmanDrawing:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.width(3)

    def draw(self, stage):
        # A very simplified drawing function for clarity
        steps = [
            lambda: self.t.forward(100),
            lambda: self.t.circle(20),
            lambda: self.t.right(90) or self.t.forward(50),
            lambda: self.t.left(45) or self.t.forward(30),
            lambda: self.t.right(90) or self.t.forward(30),
            lambda: self.t.left(45) or self.t.forward(40)
        ]
        if stage <= len(steps):
            steps[stage - 1]()

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    game = HangmanGame()
    drawer = HangmanDrawing()
    start_time = time.time()

    while not game.is_won() and not game.is_lost():
        game.show_progress()
        guess = input("Enter a letter: ").lower()
        if not Validator.is_valid_letter(guess):
            print("Invalid input. Please enter a single letter.")
            continue
        if not game.guess(guess):
            print("Wrong guess.")
            drawer.draw(game.incorrect_guesses)

    if game.is_won():
        print(f"Congratulations, {player.name}! You guessed the word: {game.word}")
    else:
        print(f"Sorry, {player.name}. You lost. The word was: {game.word}")

    end_time = time.time()
    print(f"Game duration: {round(end_time - start_time, 2)} seconds")

if __name__ == "__main__":
    main()
