# Title: 2D space shooter survival game

## Repository: https://github.com/ygh241/GurnheeYoonFinal_2d-spaceshooter-game

## Description: This project is 2d shooter based game. I will use Python's random module to generate enemies to make the whole game challeneging.


## Features:
- Feature 1
Procedural Spawn System : The game uses random.randint() to determine the coordinates for the exit portal and enemy units, ensuring no two game sessions are identical.

- Feature 2
Dynamic Enemy AI : Enemies are programmed to track the player’s position using basic vector mathematics.

- Feature 3
Collision & Win/Loss Logic : I wil make collision to both enemy and player, this will allow me to make a "death" or "gameover" system when the player collide with enemies. I will also add bullet collision that destory the enemy instances.

## Challenges
- Implementing "Safe Zone" logic to prevent the exit or enemies from spawning directly on top of the player at the start of the game.
- Managing multiple game objects (bullets, enemies, walls) efficiently using Pygame's Sprite groups to maintain high performance.
- Designing a clear and responsive UI for the "Start," "Victory," and "Game Over" screens.

## Outcomes
Ideal Outcome: I expected it to be a retro style pixel 2d space shooter game with 80's style dot graphic designed sprites(both players and enemies). I will also add background music that feels like 80's Chiptune style. I will also make difficultly system, where player can chose the difficulty of the game.

Minimal Viable Outcome: Make a very basic system, players can shoot, move with x coordinates, and the enemies with red square randomly approach to the player. Escape key to exit the window.



## Milestones
- Week 1
  1. Set up the GitHub repository and initialize the Pygame window.
  2. Implement player movement (WASD/Arrow keys) and boundary constraints.

- Week 2
  1.  Develop the randomization logic for spawning the exit and enemies.
  2.  Implement collision detection and basic enemy tracking AI.
  
- Week 3
  1.  Add UI elements (Score/Timer) and sound effects.
  2.  Final code refactoring, bug fixes, and project submission to eLearning.



