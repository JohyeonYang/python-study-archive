# Day 22 - Classic Pong Game 🏓

## Overview
A recreation of the classic arcade game "Pong" built using Python's `turtle` module. This project focuses on applying Object-Oriented Programming (OOP) concepts to manage multiple game objects and user interactions.

## What I Learned
- Creating independent objects from classes (Paddles, Ball, Scoreboard).
- Using class inheritance to extend the built-in `Turtle` class.
- Binding keyboard inputs to class methods using event listeners (`screen.onkey()`).
- Understanding the crucial difference between function calls and callback functions.
- Implementing continuous movement and bounce physics within a `while` game loop.

## Files
- `main.py`: The main game loop and screen setup.
- `paddle.py`: The `Paddle` class that controls player movement.
- `ball.py`: The `Ball` class handling movement and collision logic.

## How to Play
Run `main.py` to start the game. 
- **Right Player:** Use the `Up` and `Down` arrow keys.
- **Left Player:** Use the `W` and `S` keys. (Modify key bindings in `main.py` as needed!)

## Reflection
Building Pong helped me solidify my understanding of OOP and class inheritance. Figuring out how to separate the code into different modules (`paddle.py`, `ball.py`) made the main game loop much cleaner and easier to read. Debugging parameter errors and function references was tricky but highly rewarding!