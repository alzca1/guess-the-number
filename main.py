#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)


def play_game():

    attempts = 0
    print("\nWelcome to the Number Guessing Game.")
    print("I'm thinking of a number between 1 and 100.")

    difficulty_level = ""

    while difficulty_level != 'easy' and difficulty_level != 'hard':
        difficulty_level = input("Choose difficulty: 'easy' or 'hard': ")

    random_number = random.randint(1,100)
    if (difficulty_level == "easy"):
        attempts = 10
        print(f"You have {attempts} attempts to guess the number.")
    if (difficulty_level == "hard"):
        attempts = 5
        print(f"You have {attempts} attempts to guess the number")

    guess = ""

    while random_number != guess and attempts > 0:
      guess = int(input("Make a guess: "))

      if guess > random_number and attempts != 0:
        print("Too high.")
        attempts -= 1
      if guess < random_number and attempts  != 0:
        print("Too low.")
        attempts -= 1
      if guess == random_number:
        print(f"You got it! The answer was {random_number}")
        return 

      if(attempts > 0):
        print("Guess again.")
        print(f"You have {attempts} remaining to guess the number.")
      else:
        print("You've run out of guesses, you lose.")
        
play_game()
