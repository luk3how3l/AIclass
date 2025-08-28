import queue, bfs from 'waterjugProblem.py'_weakrefset
import time

def __main__():
    start_state = [0, 0]
    maxA = 6
    maxB = 4
    target = 1

    graph = grapth(start_state, maxA, maxB)
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



if __name__ == "__main__":
    __main__()