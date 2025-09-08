from search_algorithms import grapth
import time


def print_results(graph_object, path, algorithm_name):
    print(f"Domain: Water Jug problem | Algorithm: {algorithm_name}")
    
    if not path or path == "unreachable":
        print("No solution found.")
        return

    # For unweighted graphs, cost and depth are the number of steps
    cost = len(path) - 1
    depth = len(path) - 1

    print(f"Solution cost: {cost} | Depth: {depth}")
    print(f"Nodes generated: {graph_object.nodes_generated} | Nodes expanded: {graph_object.nodes_expanded} | Max frontier: {graph_object.max_frontier_size}")
    print("Path:")

    # Loop from the first step
    for i in range(1, len(path)):
        action = path[i][0]
        from_state = path[i-1][1]
        to_state = path[i][1]
        # The ":<15" part adds padding to align the text nicely
        print(f"  {i}) {action:<15} {from_state} -> {to_state}")






def __main__():
    #switch it to tripuple
    start_state = [0, 0]
    maxA = 6
    maxB = 4
    target = 1

    graph = grapth(start_state, maxA, maxB)
     # --- Run BFS ---
    start_time = time.time() 
    bfs_path = graph.bfs(target)
    end_time = time.time()
    # Pass the object, path, and name to the print function
    print_results(graph, bfs_path, "BFS")
    duration = end_time - start_time
    print(f"Time elapsed: {duration:.6f} seconds")
    
    grapha = grapth(start_state, maxA, maxB)
    start_time2 = time.time()
    ids_path = grapha.ids(target)
    end_time2 = time.time() 
    print_results(grapha, ids_path, "IDS")
    duration2 = end_time2 - start_time2
    print(f"Time elapsed: {duration2:.6f} seconds")


    print("\n" + "="*40 + "\n")
    print("\n" + "="*40 + "\n")

    start_state = [0, 0]
    maxAa = 11
    maxBb = 5
    targett = 8

    ggraph = grapth(start_state, maxAa, maxBb)
     # --- Run BFS ---
    start_time = time.time() 
    bfs_path = ggraph.bfs(targett)
    end_time = time.time()
    duration = end_time - start_time
    # Pass the object, path, and name to the print function
    print_results(ggraph, bfs_path, "BFS")
    print(f"Time elapsed: {duration:.6f} seconds")
    
    #input("press enter:")

    agrapha = grapth(start_state, maxAa, maxBb)
    start_time2 = time.time()
    ids_path = agrapha.ids(targett)
    end_time2 = time.time()
    print_results(agrapha, ids_path, "IDS")
    duration2 = end_time2 - start_time2
    print(f"Time elapsed: {duration2:.6f} seconds")

    #not ready
def main1():

    # Time the function call, running it 10 times
    time_taken = timeit.timeit("my_function()", setup="from __main__ import my_function", number=10)

    print(f"Average time over 10 runs: {time_taken / 10:.6f} seconds.")

if __name__ == "__main__":
    __main__()



''' Goal for output to look like-> 
Domain: Water Jug problem | Algorithm: BFS
Solution cost: 7 | Depth: 7
Nodes generated: 23 | Nodes expanded: 15 | Max frontier: 6
Path:
  1) Move Goat       (L,L,L,L) -> (R,L,R,L)
  2) Return alone    (R,L,R,L) -> (L,L,R,L)
    ...


'''