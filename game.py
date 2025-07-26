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

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts_left = get_attempts_by_difficulty()
    attempt_count = 0

    while attempts_left > 0:
        try:
            guess = int(input(f"🎯 Attempt {attempt_count + 1}: Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        attempt_count += 1

        if guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed the correct number in {attempt_count} attempts.")
            return
        elif guess < number_to_guess:
            print("📉 The number is **greater** than your guess.\n")
        else:
            print("📈 The number is **less** than your guess.\n")

        attempts_left -= 1
        if attempts_left == 0:
            print(f"❌ You've run out of attempts. The correct number was {number_to_guess}.")
        else:
            print(f"⏳ Attempts remaining: {attempts_left}\n")

def main():
    while True:
        print_welcome()
        play_game()
    
        play_again = input("🔁 Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("👋 Thanks for playing! See you next time.")
            break
        print("\n" + "="*50 + "\n")  # Separator between games

if __name__ == "__main__":
    main()



