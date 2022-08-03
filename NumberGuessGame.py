import random
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(1, 101)
attempts = 0
user_choose = 0

def game(attempts, user_choose, number):
    while attempts > 0 and user_choose != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_choose = int(input("Make a guess: "))
        if user_choose == number:
            print("You guessed correctly. You win")
            break
        elif user_choose < number:
            print("Too low.")
            attempts -= 1
        else:
            print("Too high.")
            attempts -= 1
        if attempts == 0:
            print("You run out of guesses. You lose.")
if diff == "hard":
    game(5, user_choose, number)
elif diff == "easy":
    game(10, user_choose, number)
