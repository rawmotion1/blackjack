# Blackjack Console Game

This is a simple command-line Blackjack game written in Python. It simulates a game of Blackjack between the player and the computer.

## Features

* Draw cards randomly from a deck
* Automatic Ace value adjustment (11 or 1) to avoid busting
* Computer follows Blackjack rules (hits until at least 17)
* Game ends when the player busts, passes, or the computer completes its turn
* Uses ASCII art (requires `art.py` with a `logo` variable)

## Requirements

* Python 3.x
* `art.py` module (a custom module or placeholder file containing a `logo` string)

## How to Play

1. Run the program in your terminal.
2. Type `'y'` to start a new game or `'n'` to quit.
3. View your cards and choose whether to hit (`'y'`) or pass (`'n'`).
4. Try to beat the computer's hand without going over 21.

## Example Output

```
Your cards: [10, 7], current score: 17
Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [10, 7], final score: 17
Computer's final hand: [6, 8, 7], final score: 21
You lose.
```

## Notes

* Aces count as 11 unless that would cause a bust, in which case they're counted as 1.
* The `art.py` module should define a `logo` variable with ASCII art to be displayed at the start of the game.

Enjoy playing Blackjack!
