#water jug problem 
import itertools # Useful for a tie-breaking counter
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
        self.cost = 0

    def add_neighbor(self,value):
        if value not in self.neighbors:  # Avoid duplicate neighbors
            self.neighbors.append(value)

    def change_lvl(self, depth):
        self.level = int(depth)
        #return True
    def change_cost(self, price):
        self.cost = int(price)
        #return True


class grapth:
    '''the grapth is undirected and non-weighted'''
    def __init__(self,start,maxA,maxB):
        #mapping
        #self.start l= (start,depth)
        self.start = start
        self.problem = None
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
    
    def insert_problem(self,object):
        self.problem = object
        return True
       
        
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
    
    def Heuristics(self, value):
        if value == 0:
            return 0
        if value == 42:
            kount = 0
            #how many are out of place
            for i in range(self.problem.state):
                if self.problem.goalstate != self.problem.state:
                    kount += 1
            return kount
        if value == 67:
            #mattaham grid
            #do some math
            #implement later
            return 0
    

    def Astar(self,target,limit):
        """
        Performs an A* Tree Search to find the lowest-cost path from a start state to a goal.

        A* search is an informed search algorithm that balances the cost to reach a node (g-score)
        with an estimated cost to get from that node to the goal (h-score from the heuristic).
        The evaluation function is f(n) = g(n) + h(n).

        This implementation is for a TREE SEARCH, meaning it does not check for previously visited
        states. This is faster but is only optimal if the graph is a tree (has no cycles).

        Args:
            start_state: The state where the search begins.
            goal_test_func: A function that takes a state and returns True if it is a goal state.
            actions_func: A function that takes a state and returns a list of all possible actions.
            transition_func: A function that takes a state and an action, and returns the resulting state.
            step_cost_func: A function that takes a state and an action, and returns the cost of that step.
            heuristic_func: A function that takes a state and returns an estimated cost to the goal (h-score).

        Returns:
            A list representing the solution path from the start state to the goal state, or None if no
            solution is found.
        """
        #
        # HINT 1: The frontier is a min-priority queue ordered by the f-score. As with UCS,
        # Python's `heapq` module is the right tool.
        frontier = []

        #
        # HINT 2: A* needs to track not just the state, but also its parent and its g-score.
        # A simple helper class or a `collections.namedtuple` is a great way to create a 'Node'
        # to store this information (e.g., Node(state, parent, g_score)).
        #
        # from collections import namedtuple
        # Node = namedtuple('Node', ['state', 'parent', 'g_score'])

        #
        # HINT 3: To handle cases where two nodes have the same f-score, it's good practice
        # to add a unique, incrementing counter as a tie-breaker. The heapq will then sort by
        # (f_score, counter, node).
        tie_breaker = itertools.count()

        #
        # HINT 4: Create the initial root node and calculate its f-score. The g-score (cost from start)
        # for the root node is always 0.
        g_score = 0
        h_score = Heuristics(start_state)
        f_score = g_score + h_score
        root_node = (start_state, None, g_score) # (state, parent, g_score)

        #
        # HINT 5: Push the first node onto the frontier with its f-score and the tie-breaker.
        heapq.heappush(frontier, (f_score, next(tie_breaker), root_node))

        #
        # HINT 6: The main loop continues as long as there are nodes to explore in the frontier.
        while frontier:
            #
            # HINT 7: Pop the node with the lowest f-score. The item will be the full tuple,
            # but you only need to work with the node object itself.
            f_cost, _, current_node = heapq.heappop(frontier)
            current_state, current_parent, current_g_score = current_node

            #
            # HINT 8: Check if the state of the popped node is the goal. If so, you've found the solution.
            # You would then write a helper function to backtrack from this node using its parent pointers.
            if goal_test_func(current_state):
                # return reconstruct_path_from_node(current_node)
                pass

            #
            # HINT 9: Expand the current node by generating all of its children. ⭐️
            for action in actions_func(current_state):
                #
                # HINT 10: For each action, calculate the child's state and its g-score.
                child_state = transition_func(current_state, action)
                g_prime = current_g_score + step_cost_func(current_state, action)

                #
                # HINT 11: Create the new child node, calculate its f-score using the heuristic,
                # and push it onto the frontier.
                # NOTE: Because this is a TREE search, we do NOT check if we've seen this state before.
                # We simply create a new node for every child and add it to the frontier.
                h_prime = heuristic_func(child_state)
                f_prime = g_prime + h_prime
                child_node = (child_state, current_node, g_prime) # (state, parent_node, g_score)

                heapq.heappush(frontier, (f_prime, next(tie_breaker), child_node))

        #
        # HINT 12: If the loop finishes, the frontier is empty but the goal was never found.
        return None
    
    
