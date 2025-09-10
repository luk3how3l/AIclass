1: The Peas Assessment of the problem. 

The 15 puzzle (also called Gem Puzzle, Boss Puzzle, Game of Fifteen, Mystic Square and more) is a sliding puzzle. It has 15 square tiles numbered 1 to 15 in a frame that is 4 tile positions high and 4 tile positions wide, with one unoccupied position. Tiles in the same row or column of the open position can be moved by sliding them horizontally or vertically, respectively. The goal of the puzzle is to place the tiles in numerical order (from left to right, top to bottom).

Named after the number of tiles in the frame, the 15 puzzle may also be called a "16 puzzle", alluding to its total tile capacity. Similar names are used for different sized variants of the 15 puzzle, such as the 8 puzzle, which has 8 tiles in a 3×3 frame




1: PEAS-Performance Measure, Environment, Actuators, and Sensors.
 -Performance: the primary goal of this test is how little steps it takes to get to the end goal. if you can get to the minimum steps to reach finally goal from certain instances. also how long the computing takes. 
 - Environment of 8 piece puzzle is an rigid static 9 space which is always shape by 3 by 3 box. with 8 movable pieces. It is discrete due to finite numebr of moves. also the single agent with-in this environment.
 -Actions that we can take is move an puzzle piece if only there an nieghbor of piece that is empty. you can only check nieghbors to the top, right, left and bottom,
 Actuators- there is one actuactors can move the puzzle piece by piece to eventually get the end result. the only piece you can move is the empty space. Move Blank Up. Move Blank Down. Move Left. Move Blank Right.
 S- the sensors are if the puzzle pieces surrounding, like if it's available or it's closed. e.j. a puzzle piece is in the top right corner. the top and left are walls of the puzzle and are close and the right of it is another piece so it's closed. the bottom is the empty space, so it's open. the sensor may be the location of the each piece, since placement matters to reach end goal.




2: State-Space Model: 
    1:Initial state- For my instance of this problem: The standard puzzle of this kind works with empty space (0) on the top right corner. if the state was represented in an array would look like this:
    [ 
        8,5,0
        1,2,4
        3,7,6
    ]

    2: Actions: same thing as actuators, I can move the empty piece up, down, left & right.

    3: Transition Model: 
    The transition model describes the new state that results from applying an action to the current state. It answers the question: "If I am in state S and take action A, what is the new state S'?"

        Example:

        Given State (S): [[8, 5, 0], [1, 2, 4], [3, 7, 6]]

        The blank space is at position (0, 2).

        Action (A): LEFT

        Resulting State (S'): Applying the LEFT action swaps the blank space 0 with the tile to its left (5). The new state is [[8, 0, 5], [1, 2, 4], [3, 7, 6]].

    4: Goal test: he goal test is a function that returns True if the input state is identical to the target configuration, and False otherwise. For this problem, the goal state is:
    [
        1,2,3
        4,5,6
        7,8,0
    ]

    5: Path cost: all path cost is uniform with each action but some actions are redundant.




    3. Python Implementation
         This section code can be found in the directory "domain" run.py and can run it by these code 
