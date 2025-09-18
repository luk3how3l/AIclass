from cs4300_csp_parser import parse_cs4300
from cs4300_csp import solve_backtracking, solve_backtracking_withMRV
import time


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python run_csp.py <problem.csp>")
        sys.exit(1)
    csp = parse_cs4300(sys.argv[1])
    any_sol = False
    print("using default hueristic")
    start = time.time()
    for i, sol in enumerate(solve_backtracking(csp), 1):
        end = time.time()
        final = end - start
        any_sol = True
        print(f"Solution #{i}: {sol}")
        print(f"time it took {final:.5f}")        
    if not any_sol:
        print("No solutions.")

    print()
    
    #my heuristic MRV
    print("using MRV hueristic")
    any_sol = False
    start = time.time()
    for i, sol in enumerate(solve_backtracking_withMRV(csp), 1):
        end = time.time()
        final = end - start
        any_sol = True
        print(f"Solution #{i}: {sol}")
        print(f"time it took {final:.5f}")
    if not any_sol:
        print("No solutions.")
