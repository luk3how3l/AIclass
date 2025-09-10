'''
create the first the instance 8 piece

'''

import search_algorithms as sza


class eight_piece:
    def __init__(self,start,endgoal):
        self.start = start
        self.state = start
        self.finalstate = endgoal
        self.blank = self.find_blank()
        self.aaction = []


    def action(self):
        actions = []
        #logic if the 0 is not the index positions 2,5,8. then left is valid
        if self.blank != 2 and self.blank != 5 and self.blank != 8:
            actions.append("Right")
        if self.blank != 0 and self.blank != 1 and self.blank != 2:
            actions.append("Up")
        if self.blank != 0 and self.blank != 3 and self.blank != 6:
            actions.append("Left")
        if self.blank != 6 and self.blank != 7 and self.blank != 8:
            actions.append("Down")
        if self.blank > 8 or self.blank < 0:
            print("something went wrong")
        
        self.aaction = actions
        return actions
    
    def Goal_Test(self):
        if self.state == self.finalstate:
            print("Goal has been achieved")
            return True
        else: 
            return False
        
    def Transition(self,nowaction):
        # Create a copy of the current state to avoid modifying the original list in place
        new_state = list(self.state)
        blank_index = self.find_blank()
        target_index = -1
        #sanity check
        if nowaction == "Right" and blank_index not in [2, 5, 8]:
            target_index = blank_index + 1
        elif nowaction == "Left" and blank_index not in [0, 3, 6]:
            target_index = blank_index - 1
        elif nowaction == "Up" and blank_index not in [0, 1, 2]:
            target_index = blank_index - 3
        elif nowaction == "Down" and blank_index not in [6, 7, 8]:
            target_index = blank_index + 3
        else:
            # The action is invalid for the current state.
            print(f"Invalid action: {nowaction} for current state.")
            return None

        # Perform the swap
        new_state[blank_index], new_state[target_index] = new_state[target_index], new_state[blank_index]
        #do I want it to change the state now??? below
        self.state = new_state
        self.blank = target_index
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

def build_start_instance():
    #states, start, final, trasition, action
    start_state = [1,2,3,4,5,6,0,7,8]
    endgoal = [1,2,3,4,5,6,7,8,0]

    puzzle_instance = eight_piece(start_state, endgoal)
    return puzzle_instance


if __name__ == "__main__":
    # Create the puzzle instance
    '''start
    [1,2,3,
    4,5,6,
    0,7,8]
    '''
    puzzle = build_start_instance()
    
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

