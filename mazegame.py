import turtle
import os
import random
import time

window = turtle.Screen()
window.bgcolor("black")
window.title("Maze Game")
window.setup(460,460)

# Pen Class
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

# Player Calls
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# Setup Maze
def setup_maze(level):
    
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            screen_x = -108 + (x*24)
            screen_y = 108 - (y*24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                Walls.append((screen_x, screen_y))
                pen.stamp()
            if character == "P":
                player.goto(screen_x, screen_y)

    for x in range(60, -108, -24):
        #Walls.append(((x), (-144)))
        #Walls.append(((x), (168)))
        Finishline.append(((x), (-108)))

#Dictionary that corresponds integer from txt file to proper "art"
CellArt = {
    1: [["X  "], 
        ["X  "],
        ["X  "]],
    2: [["  X"],
        ["  X"],
        ["  X"]],
    3: [["X X"],
        ["X X"],
        ["X X"]],
    4: [["   "],
        ["   "],
        ["XXX"]],
    5: [["X  "],
        ["X  "],
        ["XXX"]],
    6: [["  X"],
        ["  X"],
        ["XXX"]],
    7: [["X X"],
        ["X X"],
        ["XXX"]],
    8: [["XXX"],
        ["   "],
        ["   "]],
    9: [["XXX"],
        ["X  "],
        ["X  "]],
    10:[["XXX"],
        ["  X"],
        ["  X"]],
    11:[["XXX"],
        ["X X"],
        ["X X"]],
    12:[["XXX"],
        ["   "],
        ["XXX"]],
    13:[["XXX"],
        ["X  "],
        ["XXX"]],
    14:[["XXX"],
        ["  X"],
        ["XXX"]],
    15:[["XXX"],
        ["X X"],
        ["XXX"]],
}


### MAIN COMMANDS ###
### MAIN COMMANDS ###
### MAIN COMMANDS ###
### MAIN COMMANDS ###
### MAIN COMMANDS ###
### MAIN COMMANDS ###
### MAIN COMMANDS ###


# Delcaring Variables and the initial prompt
TrueCounter = 0
StartTime = time.time()
TimeLimit = 30
score = 0
falseinput = False
Prompt = "\nYour goal is to put in a Use WASD to make inputs. Press enter after every input \nPress 'e' then enter one you're done making inputs \n\nScore goes up 15 if correct input \nScore goes down by 2 if wrong input \n\nYou have 30 seconds to solve as many mazes as possible"

print(Prompt)

# Main While Loop for the game
# Set max mazes to be solved in 30 seconds, 10 mazes
while TrueCounter != 10:

    print("Score: " + str(score))
    #Create an empty list of strings for each row of the maze
    level = [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ]
    Walls = []
    TextFileInts = []
    Blocks = []
    Finishline = []
    FileName = random.choice(os.listdir("Levels"))
    FileName = "./Levels/" + FileName

    # Choose random level and put them in a 1d list
    with open(FileName) as f:
        for line in f:
            TextFileInts.append([int(x) for x in line.split()])

    # Correspond each int in the 1d list to its matching 3x3 configuration and append blocks to create a list of 3 element lists
    for x in range(3):
        for y in range(3):
            Blocks.append(CellArt[TextFileInts[x][y]])

    CorrespondingRows = [[],[],[]]

    # Parse list properly to make the level
    for i in range(9):
        CorrespondingRows[0].extend(Blocks[i][0])
        CorrespondingRows[1].extend(Blocks[i][1])
        CorrespondingRows[2].extend(Blocks[i][2])



    j = 0
    for x in range(0, 9, 3):
        #for y in range(4):
        for y in range(3):
            level[x] += CorrespondingRows[0][j]
            level[x+1] += CorrespondingRows[1][j]
            level[x+2] += CorrespondingRows[2][j]
            j+=1

    
    # Places start point
    Start = 'P'
    level[0] = level[0][:1] + Start + level[0][1 + 1:]

    # Set Up Maze
    pen = Pen()
    player = Player()
    setup_maze(level)

    Solved = False
    # A while loop that breaks if the correct sequence is given
    while Solved == False:
        # Takes in input and stores it in an array
        NewInput = ''
        UserInput = []
        while NewInput != 'e':
            NewInput = input("Enter input: ")
            if NewInput != 'e' and len(NewInput) == 1:
                UserInput.append(NewInput)

        # Starting Coordinated
        FinalX = player.xcor()
        FinalY = player.ycor()

        # Perform moves on starting coordinate and make player go to coordinate
        for x in range(len(UserInput)):
            if UserInput[x] == 'w':
                FinalY += 24
            if UserInput[x] == 's':
                FinalY -= 24
            if UserInput[x] == 'a':
                FinalX -= 24
            if UserInput[x] == 'd':
                FinalX += 24
        player.goto(FinalX, FinalY)

        # Checks if final coordinates is in the finished position
        for x in range(len(Finishline)):
            if ( Finishline[x] == ((FinalX), (FinalY))):
                Solved = True
                if((time.time() - StartTime) < TimeLimit):
                    score += 15
                    TrueCounter += 1
        # If statements to check if input was given in time
        if((time.time() - StartTime) > TimeLimit):
            falseinput = True
            print("Time is up. Your score is: " + str(score))
            break

        if Solved == False:
            if((time.time() - StartTime) < TimeLimit):
                score -= 2
            print("Score: " + str(score))
            player.goto(-84,108)

        print(Solved)


    if(falseinput == True):
        break
    if(time.time() - StartTime > TimeLimit):
        print("Time is up. Your score is: " + str(score))
        break

    # Resets maze for new generation
    player.goto(-84,108)
    pen.reset()

if(TrueCounter == 10):
    print("You did it! You're final score is: " + str(score))

# Exit prompt
Exit = input("Press Q to exit window: ")

if(Exit == "Q"):
    turtle.bye()
