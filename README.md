# MazeGame
Building a game on Python to practice data structures and algorithmic manipulation of arrays.

The game:
- builds x by y random bits 
- Uses the bit values modulo 4 to define the walls of an x by y maze
- Solves the maze by:
     - Starting at (0,0) and attempting to move throughout the maze
     - It stores each space within the maze in a dictionary
     - If the space is achievable from the startpoint, assigns an "empty" tag to it
- Places a goal at the center
     - If the goal is unachievable, it spirals the goal spot out until it is acheiveable
     - If the goal is >10 spaces from the center of the maze it rebuilds the maze
     - Tags that spot in the maze as "goal"
- Initiates a tkinter to provide the GUI for the player
     - Builds out a local maze walls using x_s by y_s 1x20 blocks
     - Places the goal at the top left block so it will be invisable until found
     - Places the character in the top left
- Initiates a local SQL database to store
     - Every move made
     - Time it was made
     - position it ended on
     - direction it moved
- Begins a loop to check for keyboard strokes
     - If 'qweasd' were pressed
          - Checks if the character can move that way in the maze
          - Updates the position on the big maze
          - Updates the position on the local maze
          - checks if it is the goal
          - Updates the tkinter window
- Once the goal is found
     - Changes the tkinter header to you win
     - Calls all the SQL entries since the game started
     - Plots the path the character took from the beginning
