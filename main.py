from calculator import run_calculator
from guessing_game import run_guessing_game

def main():
    while True:
        print("\n==============================")
        print("      WEEK 1 PROJECT MENU     ")
        print("==============================")
        print("1. Use Calculator")
        print("2. Play Guessing Game")
        print("3. Turn Off Program")
        
        user_choice = input("\nWhat do you want to do? (1-3): ").strip()
        
        if user_choice == '1':
            run_calculator()
        elif user_choice == '2':
            run_guessing_game()
        elif user_choice == '3':
            print("Closing application. See you later!")
            break
        else:
            print("Invalid option. Type 1, 2, or 3.")

if __name__ == "__main__":
    main()