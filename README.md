# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
   - The purpose of this game is for the user to guess a number between 1 and 100. After each guess the user is told if the guess is too high or too low. The user has 8 guesses to win.
- [x] Detail which bugs you found.
   - The go higher/lower hints were reversed, pressing enter to submit a guess didn't work, the history in the debug panel didn't update immediately and didn't clear when starting a new game.
- [x] Explain what fixes you applied.
   - Fixed the too high/low logic, enter pressed submits the guess, and history list resets when the game restarts.

## 📸 Demo

- [x] Winning Game Screenshot
![Winning Game Screenshot](winning_screenshot.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
