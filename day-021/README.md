# Day 21 - Snake Game Part 2

## What I learned

- How to use class inheritance (`super().__init__()`) to inherit from the Turtle class
- How to spawn and randomly relocate food on the screen
- How to create a scoreboard and update text dynamically using `write()`
- How to add new segments to the snake's body using list indexing (`[-1]`)
- How to detect collisions between the snake and the food

## Main Concepts

- Class Inheritance (Superclasses)
- List Indexing & Manipulation
- Text Rendering in Turtle
- Collision Detection

## Files

- `main.py`: Main game loop and collision logic for Day 21
- `snake.py`: Updated with the `extend()` method to grow the snake
- `food.py`: Food class implementation with random positioning
- `scoreboard.py`: Scoreboard class to track and display points (if applicable)

## Reflection

Today I completed the classic Snake Game.
I learned how powerful class inheritance can be by making the `Food` class inherit directly from the `Turtle` class. Implementing the scoreboard and understanding how to make the snake grow longer by manipulating lists was incredibly fun and rewarding. Overcoming some debugging challenges also helped me understand the importance of matching file paths and saving code.