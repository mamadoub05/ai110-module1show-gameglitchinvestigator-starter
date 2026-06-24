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

- [ ] Describe the game's purpose.
Glitchy Guesser is a number guessing game built with Streamlit where the player tries to guess a secret number within 8 attempts. The player selects a difficulty (Easy, Normal, or Hard), which controls the number range and attempt limit. 
- [ ] Detail which bugs you found.
check_guess returned "Go HIGHER" when the guess was too high and "Go LOWER" when it was too low, the exact opposite of correct behavior.
String conversion on even attempts — on every even-numbered attempt, the secret number was cast to a string using str().
New Game reset was broken — clicking New Game reset attempts to 0 instead of 1, used a hardcoded range of 1–100 ignoring the selected difficulty, and didn't reset status or history, so the game wasn't fully restarting.
Hard mode was easier than Normal — Hard mode used a range of 1–50, which is narrower than Normal's 1–100, making it accidentally easier to guess.
- [ ] Explain what fixes you applied.
Moved all game logic (check_guess, parse_guess, get_range_for_difficulty, update_score) out of app.py and into logic_utils.py, then imported them back into app.py.
Swapped the hint messages in check_guess so "Too High" correctly returns "Go LOWER" and "Too Low" returns "Go HIGHER."
Removed the str() conversion block entirely and replaced it 
Fixed the New Game block to reset attempts to 1, use the correct difficulty range via the low and high variables, and also reset status and history.
Changed Hard mode range to 1–200 so difficulty levels are ordered correctly

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. user enter a guess of 3 
2. game returns too low
3. user enters a guess of 60
4. game returns too high
5. score and # of attempts is updating correctly
6. user enters a guess of 52
7.game returns "correct you won" with correct score

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
