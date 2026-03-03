# 🎮 Assignment: Games in Python

## 🎯 Objective

Practice core Python skills by building a text-based Hangman game. You will use loops, conditionals, strings, and user input to create an interactive game experience.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the basic game setup, including a list of possible words and logic to select one word at random.

#### Requirements
Completed program should:

- Define a list of at least 5 possible words.
- Randomly choose one word as the hidden word for the current game.
- Create a way to track guessed letters.
- Display the hidden word as underscores before guessing begins (example: `_ _ _ _`).

### 🛠️ Handle Player Guesses

#### Description
Add the main game loop that asks the player for a letter and updates game progress based on correct or incorrect guesses.

#### Requirements
Completed program should:

- Prompt the player to enter one letter per turn.
- Reveal correctly guessed letters in their correct positions.
- Track and display the number of incorrect guesses remaining.
- Prevent duplicate guesses from counting as new turns.

### 🛠️ Finish the Game

#### Description
Complete the win/lose logic and display a clear result message to the player.

#### Requirements
Completed program should:

- End the game when the player guesses all letters in the word.
- End the game when the player runs out of attempts.
- Display a win message if the word is guessed.
- Display a lose message and reveal the word if attempts are exhausted.
- Show one short sample interaction in your README or code comments for testing.
