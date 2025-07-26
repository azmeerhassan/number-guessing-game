# 🎯 Number Guessing Game - CLI Edition

A simple command-line number guessing game built in Python.  
Test your luck and intuition by guessing a randomly selected number within a limited number of attempts!

---

## 🚀 How It Works

- When the game starts, a random number between **1 and 100** is selected.
- The player chooses a **difficulty level** which determines the number of chances:
  - 🟢 Easy → 10 chances
  - 🟡 Medium → 5 chances
  - 🔴 Hard → 3 chances
- The player enters guesses and receives hints:
  - “📉 The number is greater”
  - “📈 The number is less”
- The game ends when the player:
  - Guesses the number correctly ✅
  - Or runs out of chances ❌
- Option to **play again** after each round!

---

## 📦 Requirements

- Python 3.x
- No external libraries required

---

## 🧑‍💻 Usage

### ▶️ Run the game:

```bash
python game.py
````

### 📸 Sample Output:

```
🎉 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2
🟡 Medium mode selected — You get 5 chances!

🎯 Attempt 1: Enter your guess: 45
📉 The number is greater than your guess.

⏳ Attempts remaining: 4
...
🎉 Congratulations! You guessed the correct number in 3 attempts.
```

---

## 🧠 Features

* Random number generation
* Difficulty selection
* Hints and attempt counter
* Replay support
* Error handling for invalid input

---

## 💡 Future Enhancements

* Track high scores
* Add a hint system
* Include a timer for each round
* Export game stats

---

## 🧑‍🎓 Built With

* Python Standard Library only
* Focused on logic, conditions, loops, and functions

---

## 📂 Project Structure

```
number-guessing-game/
├── game.py
└── README.md
```

---

## 👤 Author

Azmeer Hassan Ammad

---

## 🔖 License

This project is licensed for personal and educational use.

```

---

