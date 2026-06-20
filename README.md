# 🎯 Number Guessing Game

A fun and interactive number guessing game built with Python. The computer picks a random number, and the player has to guess it with helpful hints!

## 🎮 Game Overview

In this game:
- The computer generates a random number between 1 and 100
- The player tries to guess the number
- After each guess, the game provides helpful hints
- The goal is to guess the number in the minimum number of attempts
- The game tracks your best score

## ✨ Features

### Core Gameplay
- **Random Number Generation** - Computer picks a random number (1-100)
- **Interactive Guessing** - Player inputs guesses
- **Smart Hints** - "Higher" or "Lower" feedback after each guess
- **Attempt Counter** - Tracks number of guesses made
- **Victory Message** - Congratulates player with attempt count
- **Play Again** - Option to restart the game

### Enhanced Features
- **Difficulty Levels**
  - Easy: 1-50 range, more generous attempt limit
  - Medium: 1-100 range, standard attempt limit
  - Hard: 1-1000 range, limited attempt count

- **Score Tracking**
  - Best score (minimum guesses)
  - Game statistics
  - Win/Loss ratio (if applicable)

- **User-Friendly Interface**
  - Clear instructions
  - Clean output formatting
  - Input validation
  - Error handling

## 📦 Technologies Used

- **Python 3.x** - Core language
- **Random Module** - Number generation
- **Tkinter** (Optional) - GUI version
- **Pytest** (Optional) - Testing

## 📁 Project Structure

```
Number-Guessing-Game/
├── game.py                    # Main game logic
├── gui_game.py               # GUI version (if applicable)
├── config.py                 # Game configuration
├── test_game.py              # Unit tests
├── requirements.txt          # Dependencies
└── README.md                 # Documentation
```

## 🚀 Getting Started

### Prerequisites

```
Python 3.6+
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Furqan-Ahmed2006/Number-Guessing-Game.git
cd Number-Guessing-Game
```

2. **Run the game**
```bash
python game.py
```

### Optional: GUI Version

If a GUI version is available:
```bash
python gui_game.py
```

## 🎮 How to Play

### Command Line Version

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Can you guess it?

Enter your guess: 50
My number is higher than 50. Try again!

Enter your guess: 75
My number is lower than 75. Try again!

Enter your guess: 62
You got it! The number was 62.
You took 3 attempts to guess the number.

Play again? (yes/no): yes
```

## 🎯 Game Rules

1. Computer picks a random number
2. Player enters a guess
3. Game provides hint (Higher/Lower) or congrats on correct guess
4. Player continues until correct number is guessed
5. Score is calculated as number of attempts

## ⚙️ Configuration

Edit `config.py` to customize:

```python
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 10  # Optional attempt limit

DIFFICULTY_LEVELS = {
    'easy': {'range': (1, 50), 'attempts': 15},
    'medium': {'range': (1, 100), 'attempts': 10},
    'hard': {'range': (1, 1000), 'attempts': 7}
}
```

## 🎯 Difficulty Levels

### Easy Mode
- Number range: 1-50
- Attempts allowed: 15
- Difficulty: ⭐

### Medium Mode
- Number range: 1-100
- Attempts allowed: 10
- Difficulty: ⭐⭐

### Hard Mode
- Number range: 1-1000
- Attempts allowed: 7
- Difficulty: ⭐⭐⭐

## 📊 Scoring System

- **Optimal Score**: Minimum possible attempts (log₂ of range)
- **Good Score**: Within average attempts
- **Challenge Score**: Uses more attempts but still wins
- **Game Over**: Exceeds attempt limit

### Examples
- 1-100 range optimal: ~7 guesses (binary search)
- 1-50 range optimal: ~6 guesses

## 📈 Game Statistics

The game can track:
- Total games played
- Games won
- Best score (minimum guesses)
- Average attempts per game
- Win percentage

## 🧪 Testing

### Run Tests

```bash
pytest test_game.py -v
```

### Test Cases Include

- Random number generation
- Hint logic (Higher/Lower)
- Win condition detection
- Input validation
- Attempt counting

## 💡 Gameplay Strategies

### Optimal Strategy: Binary Search
For a number between 1-100:
1. Guess 50 (middle)
2. Based on hint, pick middle of new range
3. Continue halving the range
4. Typically solves in 7 attempts

### Example:
```
Range: 1-100 → Guess 50
Range: 50-100 → Guess 75
Range: 50-75 → Guess 62
Range: 62-75 → Guess 68
Range: 62-68 → Guess 65
Range: 62-65 → Guess 63
Range: 63-65 → Guess 64
```

## 📦 Dependencies

None required for basic version!

Optional for enhanced features:
```
pytest>=6.0.0
```

## 🎨 Customization

### Modify Messages
Edit string messages in `game.py` or `config.py`

### Add Features
- Difficulty selection menu
- Score leaderboard
- Sound effects
- GUI interface
- Multiplayer mode

## 🐛 Troubleshooting

### Game crashes on input
- Ensure you enter a valid integer
- Check if number is within specified range

### Always getting same message
- Game logic is working correctly
- Computer is picking a new random number each game

## 🚀 Future Enhancements

- [ ] Leaderboard system
- [ ] User accounts and persistent scores
- [ ] Multiplayer mode
- [ ] Sound effects and music
- [ ] GUI with graphics
- [ ] Difficulty progression
- [ ] Timed challenges
- [ ] AI opponent (player tries to beat AI)

## 🎓 Learning Outcomes

This project demonstrates:
- Random number generation
- Control flow (loops, conditionals)
- Input validation
- Game logic implementation
- User interaction handling
- Basic statistics tracking

## 🤝 Contributing

Contributions welcome! Feel free to:
- Add new features
- Improve UI/UX
- Fix bugs
- Add tests

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💼 Author

**Furqan Ahmed**
- GitHub: [@Furqan-Ahmed2006](https://github.com/Furqan-Ahmed2006)
- LinkedIn: [Furqan Ahmed](https://www.linkedin.com/in/furqanahmedcs)

## 🎮 Related Projects

- Rock Paper Scissors Game
- Snake Water Gun Game
- Tic Tac Toe Game

---

**Last Updated**: June 2026  
**Status**: Active & Maintained ✅
