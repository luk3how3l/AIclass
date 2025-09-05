1: The Peas Assessment of the problem. 

The 15 puzzle (also called Gem Puzzle, Boss Puzzle, Game of Fifteen, Mystic Square and more) is a sliding puzzle. It has 15 square tiles numbered 1 to 15 in a frame that is 4 tile positions high and 4 tile positions wide, with one unoccupied position. Tiles in the same row or column of the open position can be moved by sliding them horizontally or vertically, respectively. The goal of the puzzle is to place the tiles in numerical order (from left to right, top to bottom).

Named after the number of tiles in the frame, the 15 puzzle may also be called a "16 puzzle", alluding to its total tile capacity. Similar names are used for different sized variants of the 15 puzzle, such as the 8 puzzle, which has 8 tiles in a 3×3 frame




1: PEAS-Performance Measure, Environment, Actuators, and Sensors.





2: State-Space Model: 
    1:Initial state- For my instance of this problem: The standard puzzle of this kind works with three jugs of capacity 8 & 5 liters. These are initially filled with both 0 liters. (0,0)

    2: Actions: same thing as actuators, I can fill up a jug to full, Drain a jug completely, pour a jug into another jug. this applies to any jug in the problem. 

    3: Transition Model: I can fill up jug 1 , Drain jug 1, pour jug 1 into jug 2, I can fill up jug 2 , Drain jug 2, pour jug 2 into jug 1.


    4: Goal test: for this instance the goals is they should be filled with 4 and 0 liters. jug 1 with 4, jug 2 with 0. (4,0)

    5: Path cost: all path cost is uniform with each action but some actions are useless or say redundant.

    3. Python Implementation
         This section code can be found in the directory "domain" runjugs.py and can run it by these code 
