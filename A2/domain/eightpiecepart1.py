'''
create the first the instance 8 piece

'''

from search_algorithms import grapth


class eight_piece:
    def __init__(self,start,endgoal):
        self.start = start
        self.state = start
        self.finalstate = endgoal
        self.blank = self.find_blank()
        self.aaction = []
        self.g = 0

    def get_action(self, state):
        actions = []
        # This uses the blank from the CURRENT state being considered
        blank_pos = state.index(0) 
        
        if blank_pos not in [0, 1, 2]:
            actions.append("Up")
        if blank_pos not in [6, 7, 8]:
            actions.append("Down")
        if blank_pos not in [0, 3, 6]:
            actions.append("Left")
        if blank_pos not in [2, 5, 8]:
            actions.append("Right")
            
        return actions
    
    def Goal_Test(self,state):
        if state == self.finalstate:
            print("Goal has been achieved")
            return True
        else: 
            return False
        
    def Transition(self, state, nowaction):
        # Create a copy of the current state to avoid modifying the original list in place
        new_state = list(state)
        blank_pos = new_state.index(0)
        

        if nowaction == "Up":
            swap_pos = blank_pos - 3
        elif nowaction == "Down":
            swap_pos = blank_pos + 3
        elif nowaction == "Left":
            swap_pos = blank_pos - 1
        elif nowaction == "Right":
            swap_pos = blank_pos + 1
        else:
            return new_state # Should not happen with valid actions
        # Perform the swap
        new_state[blank_pos], new_state[swap_pos] = new_state[swap_pos], new_state[blank_pos]
        return new_state

        

    def find_blank(self):
        #find black in what positon
        blank_pos = 9 #not real
        for pos in self.state:
            if pos == 0:
                #get the index num in array
                blank_pos = self.state.index(pos)
                continue
        return blank_pos
    
    
    def c(self,parent_node):
        #check if the aprent node is root, start at one
        if parent_node.parent == None:
            self.g = 1
            return  
        else:
            self.g = parent_node.g + 1

    
        


#main that use class eight piece and grapth to use the A* algorithm



def build_start_instance1():
    #states, start, final, trasition, action
    start_state = [1,2,3,4,5,6,0,7,8]
    endgoal = [1,2,3,4,5,6,7,8,0]

    puzzle_instance = eight_piece(start_state, endgoal)
    return puzzle_instance

def build_start_instance2():
    #states, start, final, trasition, action easy
    # An "easy" puzzle that can be solved in a few steps.
    start_state = [1, 2, 3, 4, 0, 5, 7, 8, 6] 
    endgoal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    puzzle_problem = eight_piece(start_state, endgoal_state)
    return puzzle_problem

def build_start_instance3():
    #states, start, final, trasition, action easy
    # An "easy" puzzle that can be solved in a few steps.
    start_state = [1, 6, 2, 7, 4, 3, 5, 0, 8] 
    endgoal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    puzzle_problem = eight_piece(start_state, endgoal_state)
    return puzzle_problem

def build_instance(state):
    start_state = state 
    endgoal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    puzzle_problem = eight_piece(start_state, endgoal_state)
    return puzzle_problem

def instance_list():
    """
    Returns a list of 10 solvable 8-puzzle start states.
    The goal state is assumed to be [1, 2, 3, 4, 5, 6, 7, 8, 0].
    """
    puzzle_list = [
        # Easy
        [1, 2, 3, 4, 5, 6, 7, 0, 8],
        [1, 2, 3, 4, 0, 5, 7, 8, 6],
        # Medium
        [1, 3, 0, 4, 2, 5, 7, 8, 6],
        [4, 1, 2, 7, 0, 3, 8, 5, 6],
        [5, 1, 7, 2, 3, 8, 0, 4, 6],
        # Hard
        [7, 2, 4, 5, 0, 6, 8, 3, 1],
        [8, 6, 7, 2, 5, 4, 3, 0, 1],
        [6, 4, 7, 8, 5, 0, 3, 2, 1],
        # Edge Cases
        [0, 1, 2, 3, 4, 5, 6, 7, 8],
        [1, 2, 3, 4, 5, 6, 8, 7, 0]
    ]
    return puzzle_list

def list_h():
    llist = [
        0,42,69
    ]
    return llist

def solve_puzzle():
    """
    Sets up and solves an instance of the 8-puzzle.
    """
    puzzle_problem = build_start_instance3()
    search_agent = grapth(puzzle_problem)

    print("Solving 8-Puzzle...")
    print("Start State:", puzzle_problem.start)
    print("Goal State: ", puzzle_problem.finalstate)
    print("-" * 25)

    # Solve using the Manhattan distance heuristic
    solution_path = search_agent.Astar(0)

    if solution_path:
        print("Solution Found!")
        for i, state in enumerate(solution_path):
            print(f"Step {i}: {state}")
    else:
        print("No solution found.")


def check_state_ai():
    # Create the puzzle instance
    '''start
    [1,2,3,
    4,5,6,
    0,7,8]
    '''
    puzzle = build_start_instance1()
    
    # Print the initial state
    print("Initial State:", puzzle.state)
    print("Blank position (index):", puzzle.blank)

    # Get the possible actions
    possible_actions = puzzle.action()
    print("Possible actions:", possible_actions)

    # Perform a transition
    if "Right" in possible_actions:
        print("\nPerforming action 'Right'...")
        puzzle.Transition("Right")
        print("New State:", puzzle.state)
        print("New blank position:", puzzle.blank)
        
    print("\nGetting new possible actions...")
    print("New possible actions:", puzzle.action())

    # Check goal test
    print("\nChecking if goal is reached...")
    print("Goal reached:", puzzle.Goal_Test())

    if "Right" in possible_actions:
        print("\nPerforming action 'Right'...")
        puzzle.Transition("Right")
        print("New State:", puzzle.state)
        print("New blank position:", puzzle.blank)

    print("\nChecking if goal is reached...")
    print("Goal reached:", puzzle.Goal_Test())

def solve_puzzles():
    """
    Sets up and solves an instance of the 8-puzzle.
    """

    #heuristic_list = list_h()
    puzzleinstances = instance_list()
    for instances in puzzleinstances:
        puzzle_problem = build_instance(instances)
        search_agent = grapth(puzzle_problem)

        print("Solving 8-Puzzle...")
        print("Start State:", puzzle_problem.start)
        print("Goal State: ", puzzle_problem.finalstate)
        print("-" * 25)

        # Solve using the Manhattan distance heuristic
        solution_path = search_agent.Astar(0)

        if solution_path:
            print("Solution Found!")
            for i, state in enumerate(solution_path):
                print(f"Step {i}: {state}")
        else:
            print("No solution found.")


if __name__ == "__main__":
    solve_puzzles()

