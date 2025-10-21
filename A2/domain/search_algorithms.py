#water jug problem 
import heapq
import itertools # Useful for a tie-breaking counter
#from eightpiecepart1 import eight_piece
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
    def __init__(self,state,action,parent,g,h_score ):
        #plug in a list
        self.state = state # [1,2,3...]
        self.parentnode = parent #point to parent
        self.action = action
        self.level = None   #to show the depth level to check in IDS
        self.cost = g
        self.h_score = h_score
        self.f_score= g + h_score
        
    def __lt__(self, other):
        return self.f_score < other.f_score

   
    def change_cost(self, price):
        self.cost = int(price)
        #return True

    
    def add_neighbor(self,value):
        if value not in self.neighbors:  # Avoid duplicate neighbors
            self.neighbors.append(value)

    def change_lvl(self, depth):
        self.level = int(depth)
        #return True
    

class grapth:
    '''the grapth is directed and weighted'''
    def __init__(self,problem):
        #mapping
        #self.start l= (start,depth)
        #self.start = start
        self.problem = problem
        self.reset_metrics()
        self.path = {}
        #stats
        
    def clean_visited(self):
        self.visited = set()
        return
    
    def Heuristics(self,state, value):
        goal = self.problem.finalstate
        curr_state= state

        if value == 42:
            kount = 0
            #how many are out of place
            for i in range(len(state)):
                if state[i] != 0 and state[i] != goal[i]:
                    kount += 1
            return kount
        if value == 67:
            #mattaham grid
            
            distance = 0
            for i in range(0, 8):
                current_pos = curr_state.index(i)
                goal_pos = goal.index(i)
                current_row, current_col = divmod(current_pos, 3)
                goal_row, goal_col = divmod(goal_pos, 3)
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
            return distance
        return 0
       
        
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
        if not isinstance(end_state, node):
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
        else:
            """
            Backtracks from the goal node construct the solution path.
            """
            path = []
            while end_state:
                path.append(end_state.state)
                end_state = end_state.parentnode
            return list(reversed(path))

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
    
    
    def reset_metrics(self):
        """Resets metrics for a new search."""
        self.nodes_expanded = 0
        self.nodes_generated = 0
        self.max_frontier_size = 0
        self.solution_cost = 0

    def get_metrics(self):
        """Returns a dictionary of the final search metrics."""
        return {
            "Nodes Expanded": self.nodes_expanded,
            "Nodes Generated": self.nodes_generated,
            "Max Frontier Size": self.max_frontier_size,
            "Solution Cost/Depth": self.solution_cost
        }

    def Astar(self, heuristic):
        
        self.reset_metrics() # Reset stats for this run

        start_state = self.problem.state
        # ordered by the f-score. nodes
        h_score = self.Heuristics(start_state, heuristic)
        root_node = node(state=start_state, parent=None, action=None, g=0, h_score=h_score)
        
        #frontier ← min-priority queue by f (n) = g(n) + h(n)
        frontier = [root_node]
        self.nodes_generated = 1 #<-- METRIC
        self.max_frontier_size = 1 #<-- METRIC

        explored_states = {}
        explored_states[tuple(start_state)] = 0
        
        while frontier:
            self.max_frontier_size = max(self.max_frontier_size, len(frontier)) #<___METRRIC

            current_node = heapq.heappop(frontier)
            self.nodes_expanded += 1 #METRICCC
            if self.problem.Goal_Test(current_node.state):
                self.solution_cost = current_node.cost
                return self.reconstruct_path(current_node)

            for action in self.problem.get_action(current_node.state):
                child_state = self.problem.Transition(current_node.state, action)
                new_g_score = current_node.cost + 1


                if tuple(child_state) in explored_states and explored_states[tuple(child_state)] <= new_g_score:
                    continue
                
                explored_states[tuple(child_state)] = new_g_score
                # Calculate the child's h-score and create the node
                h_prime = self.Heuristics(child_state, heuristic)
                child_node = node(state=child_state, 
                                  parent=current_node, 
                                  action=action, 
                                  g=new_g_score, 
                                  h_score=h_prime)
                self.nodes_generated += 1 #METRUCCI
                # Push the new child node onto the frontier
                heapq.heappush(frontier, child_node)

        return None
    
    
