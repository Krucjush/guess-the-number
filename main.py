import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
def set_attempts(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        exit(f"Unknown difficulty {difficulty}\nAborting...")
attempts = set_attempts(difficulty)
game_over = False
while not game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
        game_over = True
    elif guess > number:
        print("Too high.")
        attempts -= 1
    else:
        print("Too low.")
        attempts -= 1
    if attempts < 1:
        print(f"You've run out of guesses, you lose. The answer was {number}.")
        game_over = True