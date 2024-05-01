# Snake Game for Python

Welcome to my Snake Game on Python project! This project is a personal journey into learning Python. I've built this simple yet fun Snake game as a way to explore programming concepts and get hands-on experience with Python.

## Project Overview

The Snake Game is a classic video game concept where the player maneuvers a line which grows in length, with the line itself being a primary obstacle. The goal is to collect food, avoid hitting the walls and the snake's own growing body. Each time the snake eats a piece of food, it grows longer, making the game increasingly difficult.

## Learning Objectives

Through this project, I aimed to understand and implement:
- Basic syntax and operations of Python.
- Use of libraries such as Pygame, which is pivotal for game development in Python.
- Event handling and rendering graphics on the screen.
- Logic for handling collisions, game state, and scoring.

## Development Environment

This game was developed on a macOS system, utilizing:
- Python 3.7
- Pygame for handling graphics and game dynamics
- PyInstaller for generating executable files for both macOS and Windows

## How to Run the Game

To run the game, you will need Python and Pygame installed on your system. Once those prerequisites are met, you can clone this repository and run the script `main.py`:

```bash
git clone <repository-url>
cd pythonSnake
python3 main.py
```

## Building Executable Files

For convenience, I've also included steps to create executable files for macOS and Windows using PyInstaller. This allows the game to be played without a Python interpreter installed.

- macOS: pyinstaller --onefile --windowed main.py
- Windows: On a Windows machine or virtual environment, run pyinstaller --onefile --windowed main.py to generate a .exe file.