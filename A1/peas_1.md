Title: 
The problem: Water pouring puzzles (also called water jug problems, decanting problems,[1][2] measuring puzzles, or Die Hard with a Vengeance puzzles) are a class of puzzle involving a finite collection of water jugs of known integer capacities (in terms of a liquid measure such as liters or gallons). Initially each jug contains a known integer volume of liquid, not necessarily equal to its capacity.

Puzzles of this type ask how many steps of pouring water from one jug to another (until either one jug becomes empty or the other becomes full) are needed to reach a goal state, specified in terms of the volume of liquid that must be present in some jug or jugs.

 In the goal state they should be filled with 4, 4 and 0 liters.




1: The Peas Assessment of the problem. 

The agent is the water jugs in this problem.(P) The performance is based of how filled is the jugs with integer capacities, how many steps it takes to satisfy the variable would be the optimal performance. (E) The Environment explained above is an abstract simpified environment; an set amount of jugs (the objects) with different set integer amount capacities, also the resource filling up these jugs is infinite, so no need to manage resource from the source; lastly, when dumping the water, it does not effect anything inside the control problem, so can do infinite times with no side effects. This environment is an very static and deterministic. (A) the Actuators within the scope of the environment would fill up the jugs, pour out a jug out into another jug and completely drain the jug of its resources. (S) the sensor would be the depth of the depth or say the integer amount of water inside the jug (example: the 5 gallon jug has 3 gallons) but not just sensor in one of the jugs but in all of them (example jug 1: 4/5 filled; jug 2: 2/9 filled).

2: State-Space Model: 
    1:Initial state- For my instance of this problem: The standard puzzle of this kind works with three jugs of capacity 8, 5 and 3 liters. These are initially filled with 8, 0 and 0 liters. (8,0,0)

    2: Actions: same thing as actuators, I can fill up a jug to full, Drain a jug completely, pour a jug into another jug. this applies to any jug in the problem. 

    3: Transition Model: I can fill up jug 1 , Drain jug 1, pour jug 1 into jug 2, pour jug 1 into jug 3, I can fill up jug 2 , Drain jug 2, pour jug 2 into jug 1, pour jug 2 into jug 3, I can fill up jug 3 , Drain jug 3, pour jug 3 into jug 2, pour jug 3 into jug 1.


    4: Goal test: for this instance the goals is they should be filled with 4, 4 and 0 liters. jug 1 with 4, jug 2 with 4 and jug 3 with 0. (4,4,0)

    5: Path cost: all path cost is uniform with each action but some actions are useless or say redundant.

    3. Python Implementation
         This section code can be found in the directory "domain" runjugs.py and can run it by these code 
         