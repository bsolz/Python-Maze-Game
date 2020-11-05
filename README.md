# Python-Maze-Game

## What Is It?

A Python based game in which a user is given a randomly generated maze. The user is then asked to give a series of inputs, in which after being executed should land the player to the end of the maze. The user has 30 seconds to solves as many mazes as he/she can. Your score increases by 15 for every correct maze that you solve and decreases by 2 for every time you put in a wrong input

### Starting Point
<img src="/start.png" alt="Start Image" width="200"/>

### End Goal
<img src="/end.png" alt="End Image" width="200"/>

## How to Play

You will need to have the terminal open along with the main game window. For every move you want to make, you must input either W, A, S or D and press enter per move

**W** - Move Up\n
**S** - Move Down\n
**A** - Move Left\n
**D** - Move Right\n

Once you think you have a valid sequence of moves, input in 'e' and press enter

If the sequence was correct, you're given a new maze and your score goes up by 15
If the sequence was not, you can try again with a -2 deduction on your total score

### Valid Input
<img src="/validinput.png" alt="Valid Input" width="200"/>

**However be aware** of the 30 second time limit as if you try to input a sequence and you are over the time limit, you do not receive those points. Nor will you be deducted for a false sequence after the time


## How Was It Built?

**maze.cpp/maze.h/main.cpp**\n
This project was actually inspired by an assignment I had to do in my Data Structures & Algorithms class where I had to generate random mazes. I then modified the code to generate 500 random mazes of the same size, which represent the different levels the maze can choose from. These mazes are output as text files of size 3x3, where each coordinate is an integer that represents a certain wall configuration.

### Wall configurations
<img src="/walls.png" alt="Walls" width="200"/>

**mazegame.py**\n
I then transformed the wall configurations into a 9x9 grid, and made the game more interractive by adding a visual interface using the turtle module, and added the games rules into the implementation

## How Do You Run?
1. Download all files
2. cd into directory where files were downloaded
3. In terminal, run `python3 mazegame.py`