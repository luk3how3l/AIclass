#water jug problem 
class queue:
    def __init__(self):
        self.lista = []

    def poop(self):
        return self.lista.pop(0)
    
    def push(self,thing):
        return self.lista.append(thing)
    
    def isempty(self):
        if len(self.lista) == 0:
            return True
        return False


class node:
    def __init__(self,value):
        #plug in a list
        self.value = value # (x,y)
        self.neighbors = []

    def add_neighbor(self,value):
        if value not in self.neighbors:  # Avoid duplicate neighbors
            self.neighbors.append(value)

class grapth:
    '''the grapth is undirected and non-weighted'''
    def __init__(self,start,maxA,maxB):
        #plug in a list
        #mapping
        self.start = start
        #self.valuesTaken = []
        #self.neighbor = []
        self.visited = set()
        self.maxJuga = maxA
        self.maxJugb = maxB
        self.path = {}
       
        

    def bfs(self, target):
        """Performs BFS to find the shortest sequence of steps to reach the target volume."""
        q = queue()
        q.push(self.start)
        self.visited.add(tuple(self.start))  # Convert list to tuple for immutability
        self.path[tuple(self.start)] = None  # Store parent for backtracking
        
        while not q.isempty():
            current = q.poop()
            x, y = current  # Current state of the jugs
            
            # If we reached the target, reconstruct the path
            if x == target or y == target:
                return self.reconstruct_path((x, y))
            
            # Generate all possible next states
            next_states = [
                (self.maxJuga, y),  # Fill Jug A
                (x, self.maxJugb),  # Fill Jug B
                (0, y),             # Empty Jug A
                (x, 0),             # Empty Jug B
                (x - min(x, self.maxJugb - y), y + min(x, self.maxJugb - y)),  # Pour A → B
                (x + min(y, self.maxJuga - x), y - min(y, self.maxJuga - x))   # Pour B → A
            ]

            # Process each valid state
            for state in next_states:
                if state not in self.visited:
                    q.push(state)
                    self.visited.add(state)
                    self.path[state] = (x, y)  # Store where it came from

        return "unreachable"

    def reconstruct_path(self, end_state):
        """Reconstructs and prints the path from the start to the target state."""
        steps = []
        while end_state is not None:
            steps.append(end_state)
            end_state = self.path[end_state]
        steps.reverse()
        
        print("Steps to reach the target:")
        for step in steps:
            print(step)

        return steps



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


#psuedocode Breadth-First Search




#psuedo Iterative-Deepening Search

#setup var