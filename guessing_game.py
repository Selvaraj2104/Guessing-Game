import random

number = random.randint(1,100)
attempts = 0
max_attempts = 7

print("...Guess the number (1 to 100)...")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts+=1

        if guess == number:
            print("Correct you guessed it...")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        print("Please Enter a valid number.")
        
if attempts == 7:
    print(f"Out of attempts! The number was {number}.")
