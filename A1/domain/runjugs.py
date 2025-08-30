from search_algorithms import node, grapth, queue, stack
import timeit

def main():
    #switch it to tripuple
    start_state = [0, 0]
    maxA = 6
    maxB = 4
    target = 1

    graph = graph(start_state, maxA, maxB)
    print("Output 1")
    result = graph.bfs(target)
    print(result)
    input("press enter:")

    start_state = [0, 0]
    maxAa = 11
    maxBb = 5
    targett = 8
    graphg = grapth(start_state, maxAa, maxBb)
    print("Output 2")
    resultt = graphg.bfs(targett)
    #print(resultt)
def __main__():

    # Time the function call, running it 10 times
    time_taken = timeit.timeit("my_function()", setup="from __main__ import my_function", number=10)

    print(f"Average time over 10 runs: {time_taken / 10:.6f} seconds.")

if __name__ == "__main__":
    __main__()



''' Goal for output to look like-> 
Domain: WGC | Algorithm: BFS
Solution cost: 7 | Depth: 7
Nodes generated: 23 | Nodes expanded: 15 | Max frontier: 6
Path:
  1) Move Goat       (L,L,L,L) -> (R,L,R,L)
  2) Return alone    (R,L,R,L) -> (L,L,R,L)
  ...


'''