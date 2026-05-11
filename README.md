Final project: Retro 2d space shooter game
Video link: https://youtu.be/ianHIqTSPAU
About the game: This is a retro style shooter game, where players have to kill as many as enemies they can, since there are endless enemy waves.

Key features: 
sprite arts: I used 2d pixel style sprites, just to give the players retro game feel.
Hitbox: when player collide enemy, the game is over, players can destory enemy with the bullets that collide with enemy.
socre system: Each kill of an enemy, players will get 10 points. Once player collide with enemy, the game over screen shows the final score of the player.
Full screen support: This game support fullscreen gameplay.
Brutal health mechanism: A lot of space shooter game has helath bars, or defense system, but my game does not have them. Once player collide with enemy, the game is over, the score does not save, players will have to restart the game.

choice of Design: The reason why I chose the retro style pixel graphic sprites is because I wanted to give players ab old 80's vibe game. I also chose to use 24x 14 for enemy, 42x42 pixel sprite for player ship, because The old games are basically pixelated, low resolutioned. 
State managements: Instead of simply using `sys.exit()`, I implemented a `game_over` boolean state. This allows the game to pause and display a "Retry" prompt, enhancing the user experience compared to a sudden crash or exit.
Optimization and efficiency: I used `convert_alpha()` for sprites to ensure transparency was handled efficiently, improving the game's performance more optimized.

File included:  
project.py: It is the main python code that running the whole game. I donwloaded and imported pygame, random, and sys library.
requirements: I listed a external library called "pygame", which the users have to manually download.
src file directory: Under the src file directory, I have all sprites(spaceship, enemy, and background). I also included project.py which is the main code of the project.

How to run game:
1. Install pip install -r requirements.txt
2. Run the game with open the terminal opened: spacehooter -> src ->  and type "python project.py" in terminal
3. Controls: 
                Arrow keys to move
                Space bar key to shoot bullets
                R key to restart
                ESC key to quit the game.


About the Author: This game is fully created by Gurnhee Yoon(who is currently majoring in Animation and Games major at UTD)

