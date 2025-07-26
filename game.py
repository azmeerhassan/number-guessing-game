# game.py

import random

def print_welcome():
    print("🎉 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Your job is to guess the number based on hints.")
    print("Difficulty levels affect how many chances you get.\n")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)\n")

def get_attempts_by_difficulty():
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            print("\n🟢 Easy mode selected — You get 10 chances!\n")
            return 10
        elif choice == "2":
            print("\n🟡 Medium mode selected — You get 5 chances!\n")
            return 5
        elif choice == "3":
            print("\n🔴 Hard mode selected — You get 3 chances!\n")
            return 3
        else:
            print("❌ Invalid input. Please enter 1, 2, or 3.")


print_welcome()
attempts = get_attempts_by_difficulty()
print(f"🎯 You will have {attempts} attempts to guess the number.\n")



