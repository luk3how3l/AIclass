#water jug problem 

#queue used below
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

class stack:
    def __init__(self):
        self.lista= []
    def poop(self):
        return self.lista.pop()
    
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
        self.level = None   #to show the depth level to check in IDS

    def add_neighbor(self,value):
        if value not in self.neighbors:  # Avoid duplicate neighbors
            self.neighbors.append(value)

    def change_lvl(self, depth):
        self.level = int(depth)
        #return True

class grapth:
    '''the grapth is undirected and non-weighted'''
    def __init__(self,start,maxA,maxB):
        #mapping
        #self.start l= (start,depth)
        self.start = start
       
        self.visited = set()
        self.maxJuga = maxA
        self.maxJugb = maxB
        self.path = {}
        #stats
        self.nodes_expanded = 0
        self.nodes_generated = 0
        self.max_frontier_size = 0
        
    def clean_visited(self):
        self.visited = set()
        return
       
        
#BFS Algorithm
    def bfs(self, target):
        """Performs BFS to find the shortest sequence of steps to reach the target volume."""
        q = queue()
        q.push(self.start)
        self.visited.add(tuple(self.start))  # Convert list to tuple for immutability
        self.path[tuple(self.start)] = None  # Store parent for backtracking
        
        while not q.isempty():
            current = q.poop()
            x, y = current  # Current state of the jugs
            self.nodes_expanded += 1
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
                    self.nodes_generated += 1
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
            self.max_frontier_size += 1
            print(step)

        return steps

    #Iterative-Deepening Search Algorithm
    def ids(self,target):
        #check if self.start = target; ret itself
        if self.start == target:
            return self.start
        response  = "unreachable"
        limit = 1
        while response == "unreachable" and limit < 60:
            response = self.dls(target,limit)
            limit += 1
            #self.max_frontier_size = limit
            #print("the limit is at:",limit)
        return response

    def dls(self, target,limit):
        """Performs DPS to find the shortest sequence of steps to reach the target volume."""
        #frontier ← stack containing Make-Node(problem.initial)
        self.clean_visited()
        sk = stack()
        #took out tuple
        sk.push([tuple(self.start),0])
        #add depth value to node starting
        self.visited.add(tuple(self.start))  # Convert list to tuple for immutability
        self.path[tuple(self.start)] = None  # Store parent for backtracking
        
        #while frontier ̸= ∅ do
        while not sk.isempty():
            #node ← POP(frontier ) 
            current, current_depth = sk.poop()
            x, y = current  # Current state of the jugs
            self.nodes_expanded += 1
            # If we reached the target, reconstruct the path
            if x == target or y == target:
                #return SOLUTION(node)
                return self.reconstruct_path((x, y))
            
            if current_depth >= limit:
                continue
            # Generate all possible next states
            #A ← ACTIONS(problem, node.state)
            next_states = [
                (self.maxJuga, y),  # Fill Jug A
                (x, self.maxJugb),  # Fill Jug B
                (0, y),             # Empty Jug A
                (x, 0),             # Empty Jug B
                (x - min(x, self.maxJugb - y), y + min(x, self.maxJugb - y)),  # Pour A → B
                (x + min(y, self.maxJuga - x), y - min(y, self.maxJuga - x))   # Pour B → A
            ]

            # Process each valid state
            #for each a ∈ REVERSE(A) do 
            for state in next_states:
                #s′ ← TRANSITION(node.state, a)
                if state not in self.visited:
                    #PUSH(frontier , child)
                    self.visited.add(state)
                    self.nodes_generated += 1
                    self.path[state] = (x, y)
                    
                    sk.push((state,current_depth+ 1))

        return "unreachable"
