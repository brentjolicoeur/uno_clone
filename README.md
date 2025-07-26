# Text-Based Uno (CLI)

A text-based clone of the classic card game Uno, playable entirely from the command line. Created as a personal project for boot.dev, this game lets you challenge computer-controlled opponents and enjoy Uno's fast-paced gameplay—no cards or friends required!

> **Note:** This project is not licensed, endorsed, or affiliated with Mattel or Uno®.

---

## Features

- **Classic Uno Gameplay:** Simulates the official Uno rules (no stacking of special cards).
- **Choose Opponents:** Select from 1 to 9 computer-controlled opponents.
- **Random AI:** Opponents always play a random valid card.
- **Standard Scoring:** End rounds and score just like the real game.
- **Flexible Play:** Play single rounds or continue for as many as you like.
- **CLI-Based:** No GUI—play directly in your terminal.

## Installation

1. **Requirements**
   - Python 3.7 or higher

2. **Clone the Repository**
   ```sh
   git clone https://github.com/brentjolicoeur/uno_clone.git
   cd uno_clone
   ```

3. **(Optional) Create a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage

1. **Start the Game**
   ```sh
   python main.py
   ```

2. **Follow the Prompts**
   - Choose the number of computer opponents.
   - Play Uno by selecting cards and following the on-screen game prompts.
   - Play as many rounds as you wish, or exit after any round.

3. **Gameplay Notes**
   - The game enforces official Uno rules.
   - Special cards (Skip, Reverse, Draw Two, Wild, Wild Draw Four) are implemented.
   - No stacking of special cards is allowed.
   - The AI always selects randomly from valid plays.


## Disclaimer

This project is for educational purposes only and is not affiliated with, endorsed, or sponsored by Mattel or Uno®.

---

Enjoy playing Uno in your terminal!