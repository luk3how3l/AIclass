from search_algorithms import grapth
from eightpiecepart1 import eight_piece
import time

import pandas as pd
import cv2 

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
       
        # Easy (2-6 steps)
       
        [1, 2, 3, 4, 5, 6, 7, 0, 8],  
        [1, 2, 3, 4, 0, 5, 7, 8, 6],  # 
        [1, 2, 0, 4, 5, 3, 7, 8, 6],
        [1, 2, 3, 0, 4, 5, 7, 8, 6],
        [1, 2, 3, 4, 5, 6, 0, 7, 8],
        [0, 1, 2, 3, 4, 5, 6, 7, 8],  #
        [1, 0, 3, 4, 2, 5, 7, 8, 6],

        # Medium (8-15 steps)

        [1, 3, 0, 4, 2, 5, 7, 8, 6],  
        [4, 1, 2, 7, 0, 3, 8, 5, 6],  
        [2, 3, 5, 1, 4, 6, 7, 8, 0],
        [1, 4, 2, 0, 7, 5, 3, 6, 8],
        [1, 3, 5, 4, 2, 0, 7, 8, 6],
        [4, 7, 2, 1, 8, 5, 3, 0, 6],
        [5, 1, 7, 2, 3, 8, 0, 4, 6], 

     
        # Hard (16-22 steps)

        [7, 2, 4, 5, 0, 6, 8, 3, 1],  # 
        [6, 4, 7, 8, 5, 0, 3, 2, 1],  
        [5, 4, 3, 6, 0, 2, 7, 8, 1],
        [3, 7, 1, 4, 0, 2, 6, 8, 5],
        [2, 6, 3, 4, 1, 5, 0, 7, 8],
        [7, 1, 2, 8, 0, 3, 6, 5, 4],
        [4, 8, 1, 3, 0, 2, 7, 6, 5],

        # Very Hard / Pathological (23-31 steps)
       
        [8, 6, 7, 2, 5, 4, 3, 0, 1], 
        [6, 5, 8, 4, 0, 1, 7, 2, 3],
        [8, 7, 1, 6, 0, 2, 5, 4, 3],
        [5, 6, 7, 4, 0, 8, 3, 2, 1],
        [8, 7, 6, 5, 4, 3, 2, 1, 0],
        [3, 5, 6, 8, 7, 1, 4, 0, 2],
        [2, 7, 5, 0, 8, 4, 6, 1, 3],
        [8, 5, 6, 7, 2, 3, 4, 1, 0]   # hardest cases
    ]
    return puzzle_list

def list_h():
    llist = [
        0,42,67
    ]
    return llist

def which_h(gg):
    if gg == 0:
        return "none"
    if gg == 67:
        return "Mattahattem"
    if gg == 42:
        return "Left one"
   
def count_inversions(state):
    """
    Counts the number of inversions in a given puzzle state.
    An inversion is any pair of tiles (excluding the blank '0') where a
    larger number appears before a smaller number in the flat list.
    """
    # Create a new list without the blank tile (0)
    tiles_only = [tile for tile in state if tile != 0]
    inversion_count = 0
    
    # Get the total number of tiles to compare
    num_tiles = len(tiles_only)
    
    # Compare every tile with every other tile that comes after it
    for i in range(num_tiles):
        for j in range(i + 1, num_tiles):
            if tiles_only[i] > tiles_only[j]:
                inversion_count += 1
                
    return inversion_count

def is_solvable(start_state, goal_state):
  
    start_inversions = count_inversions(start_state)
    goal_inversions = count_inversions(goal_state)
    
    # A puzzle is solvable if the parity of inversions is the same.
    # (i.e., both are even, or both are odd).
    return (start_inversions % 2) == (goal_inversions % 2)



def solve_puzzles():
    """
    Sets up and solves an instance of the 8-puzzle.
    """

    heuristic_list = list_h()
    puzzleinstances = instance_list()
    for instances in puzzleinstances:
        puzzle_problem = build_instance(instances)
        search_agent = grapth(puzzle_problem)
       
        #inversions = count_inversions(puzzle_problem.start)
        solvable_result = is_solvable(puzzle_problem.start, puzzle_problem.finalstate)
        print(f"Is this puzzle solvable? {solvable_result}")
        print("Solving 8-Puzzle...")
        print("Start State:", puzzle_problem.start,"and Goal State: ", puzzle_problem.finalstate )
        #print()
        print("-" * 25)
        for Hnumber in heuristic_list:
            # Solve using the Manhattan distance heuristic
            start = time.time()
            solution_path = search_agent.Astar(Hnumber)
            end = time.time()

            
            #time calc : start - end in millseconds and print it out
            # and print the elapsed time ---
            elapsed_time_ms = (end - start) * 1000
            print(f"Time to solve: {elapsed_time_ms:.4f} ms")

            htype = which_h(Hnumber)
            if solution_path:
                #print("Solution Found!")

                print(f"Solution Found using {htype} in {len(solution_path) - 1} steps!")
                print("-" * 25)
                print("Metrics:")
                metrics = search_agent.get_metrics()
                for key, value in metrics.items():
                    print(f"- {key}: {value}")
                print("-" * 25)
            else:
                print("No solution found.")

def run_all_benchmarks():
    """
    Runs all puzzle instances with all heuristics, collects the data,
    and displays it in a Pandas DataFrame table.
    """
    puzzle_instances = instance_list()
    heuristics = list_h()
    
    # This list will store a dictionary for each test run
    results_data = []
    kkount = 0
    print("Running all benchmarks... This may take a moment.")
    
    for i, instance_state in enumerate(puzzle_instances):
        puzzle_problem = eight_piece(instance_state, [1, 2, 3, 4, 5, 6, 7, 8, 0])
        search_agent = grapth(puzzle_problem)

        for code in heuristics:
            start_time = time.time()
            solution_path = search_agent.Astar(code)
            end_time = time.time()
            name = which_h(code)
            elapsed_time_ms = (end_time - start_time) * 1000
            
            # Create a dictionary for the current run's results
            run_metrics = search_agent.get_metrics()
            result_row = {
                "Puzzle ID": i + 1,
                "Heuristic": name,
                "Time (ms)": round(elapsed_time_ms, 4),
                "Solved": bool(solution_path),
            }
            # Merge the metrics from the agent into our result row
            result_row.update(run_metrics)
            kkount += 1
            # Add the completed row to our list of data
            results_data.append(result_row)

    # --- Create and display the Pandas DataFrame ---
    print("\n" + "="*80)
    print("Benchmark Results")
    print("="*80)
    
    # Create the DataFrame from our list of dictionaries
    df = pd.DataFrame(results_data)
    
    # Define a logical order for the columns
    column_order = [
        "Puzzle ID", "Heuristic", "Time (ms)", "Solved", 
        "Solution Cost/Depth", "Nodes Expanded", "Nodes Generated", "Max Frontier Size"
    ]
    df = df[column_order]

    # Use to_string() to ensure the entire table is printed without truncation
    print(df.to_string())

    try:
        output_filename = "benchmark_results.csv"
        df.to_csv(output_filename, index=False)
        print("\n" + "="*80)
        print(f"Results successfully saved to '{output_filename}'")
        print("="*80)
    except Exception as e:
        print(f"\nError saving to CSV: {e}")


if __name__ == "__main__":
    run_all_benchmarks()
    #solve_puzzles()