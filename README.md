# Space Wars

**Space Wars** is an engaging 2D arcade-style shooter game where players control a cannon to battle waves of enemy UFOs. The game is developed in Python using the Pygame library and features multiple gameplay modes, dynamic menus, and visually captivating graphics.

---

##  Features


### 🚀 Gameplay
- **Classic Mode:** Progress through levels, defeating waves of UFOs. The difficulty increases as the game progresses.
- **Endless Mode:** Survive as long as you can in an infinite wave of UFOs and achieve a high score.

### 🕹️ Game Mechanics
- Smooth cannon controls for left and right movement.
- Ability to shoot bullets to eliminate UFOs.
- Real-time score and lives tracking.
- Dynamic difficulty scaling in Classic Mode.

### Menus
- Fully interactive start menu with options like:
  - Start Game
  - Settings
  - Exit
- Pause menu accessible during gameplay.
- Game over menu with options to restart, return to the main menu, or quit.

### Sound and Graphics
- Retro-style 8-bit background music and sound effects.
- Space-themed background and custom UFO and cannon sprites.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/space-wars.git
   cd space-wars
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the game:**
   ```bash
   python space_game.py
   ```

---

## 🕹️ Controls

- **Arrow Keys:** Move the cannon left and right.
- **Spacebar:** Shoot bullets.
- **Escape:** Open the pause menu.

---

## 📂 File Structure

```
space-wars/
├── assets/             # Images, fonts, and sound files
├── src/
│   ├── space_game.py   # Main game file
│   ├── controls.py     # Core game logic
│   ├── menu_handler.py # Menu handling logic
│   ├── button_logic.py # Button and event handling
│   ├── stats.py        # Game stats and tracking
│   ├── scores.py       # Score rendering logic
│   └── cannon.py       # Player-controlled cannon logic
└── README.md           # Project description
```

---

## 💡 Future Plans

- Implement power-ups for the cannon.
- Add new types of enemies and boss fights.
- Introduce online leaderboards to compete with friends.

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for feature requests or bug reports.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🖼️ Acknowledgments

- Thanks to [Pygame](https://www.pygame.org/) for providing an excellent library for game development.
- Special thanks to all contributors for their support and feedback!

---

⭐ If you like this project, consider giving it a star on GitHub!
