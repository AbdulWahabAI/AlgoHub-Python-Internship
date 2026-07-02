import random

def run_guessing_game():
    print("\n--- Welcome to the Guessing Game ---")
    print("I've picked a secret number from 1 to 100. Try to guess it!")
    
    target = random.randint(1, 100)
    user_attempts = 0
    
    while True:
        try:
            user_input = input("Enter your guess (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print(f"Game over. The number was {target}.")
                break
                
            guess = int(user_input)
            user_attempts += 1
        except ValueError:
            print("That's not a valid number. Try again.")
            continue
            
        if guess < target:
            print("Too low! Aim higher.")
        elif guess > target:
            print("Too high! Aim lower.")
        else:
            print(f"Awesome! You found it in {user_attempts} tries.")
            break