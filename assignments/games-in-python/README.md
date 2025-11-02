# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a text-based Hangman game to practice working with strings, loops, conditionals, and user input. Focus on clear game flow and user-friendly messaging.

## 📝 Tasks

### 🛠️ Build the Hangman Core

#### Description
Implement the core Hangman gameplay: randomly choose a secret word, accept single-letter guesses from the player, reveal correct letters in their positions, track incorrect guesses, and end the game when the player either guesses the word or runs out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Display the word progress using underscores for unknown letters and reveal letters as they are guessed (e.g., _ a _ _ m a n).
- Accept single-letter guesses (case-insensitive) and ignore/notify on repeated guesses.
- Deduct one remaining attempt for each incorrect guess and display remaining attempts.
- End when the word is fully guessed (win) or when attempts reach zero (lose), showing a clear win/lose message and the correct word.
- Handle basic input validation (non-empty, single alphabetic character for letter guesses).

Example gameplay (text):
```
Secret word: _ a _ _ m a n
Guess: e
Incorrect. Attempts remaining: 5
Guess: g
Correct: _ a _ g m a n
...
```

### 🛠️ Add Enhancements (Optional)

#### Description
Enhance the user experience and extend functionality: add difficulty settings, full-word guesses, persistent word lists, or a hint system.

#### Requirements
If implemented, enhancements should be documented and meet these goals:

- Difficulty levels that adjust the allowed number of incorrect attempts or choose longer words.
- Option to guess the full word (accepted as a single guess) with appropriate win/lose handling.
- Maintain and load a word list from a file (e.g., words.txt) or include categories.
- Display the list of letters already guessed.
- Keep the core game behavior and validations intact.
