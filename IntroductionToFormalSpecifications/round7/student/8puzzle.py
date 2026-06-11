# COMP.CS.420 Introduction to Formal Specification
#
# Implementation of the 8-puzzle in Python
#
# YOUR TASK: Modify the part "TODO" in function solve()
# 
# 2-dimensional NxN playing field is presented as one dimensional list
# (row, col) => to col + (N * row)
# | (0,0) (0,1) |   
# | (1,0) (1,1) |  
# => 
# [(0,0), (0,1), (1,0), (1,1)]

# ====================================================================
# YOU NEED NOT MODIFY THIS PYTHON CLASS FOR THE EXERCISE - LEAVE AS IS
# 
# Every instance of this class corresponds to a SINGLE board position
# When do_action is called, we make a new instance of this class
# with a new board-state
# ====================================================================
class Puzzle:
    N = 3
    goal = []
    state = []
    depth = 0

    def __init__(self, state, depth=0, goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]):
        # Make sure we work with a valid puzzle
        assert len(state) / self.N == self.N
        assert goal == None or len(state) == len(goal)

        self.state = state
        self.goal = goal
        self.depth = depth

    # Is current state desired goal state
    def is_solved(self):
        return self.goal == self.state

    # Return the possible moves we can do for the empty block
    def get_actions(self):
        actions = []
        # Get (x,y) coordinates of the empty block
        x, y = (int(self.state.index(0) % self.N), int(self.state.index(0) / self.N))
        # Determine where we can move the block
        # Left  : Move empty by -1
        actions.append(-1) if (x - 1) >= 0 else None
        # Right : Move empty by 1 
        actions.append(1) if (x + 1) < self.N else None
        # Up    : Move empty by -N (row up)
        actions.append(-self.N) if (y - 1) >= 0 else None
        # Down  : Move empty by N (row down)
        actions.append(self.N) if (y + 1) < self.N else None
        return actions

    # Make a new instance of the class where we moved state according to action
    def do_action(self, action):
        # swap place of empty block
        new_state = self.state[:]
        idx = new_state.index(0)
        new_state[idx], new_state[idx + action] = new_state[idx + action], new_state[idx] 

        new_state = Puzzle(new_state, depth=self.depth + 1, goal=self.goal)
        new_state.parent = self
        return new_state
    
    # We cannot store a list to a set, we can use for example, a str instead
    def get_state_str(self):
        return str(self.state)

    # Draw the current state
    def visualize(self):
        for i in range(self.N):
            print("|{}|".format("".join(map(str, self.state[i*self.N:(i+1)*self.N]))))

# Checks if bottom row of the puzzle has a empty block
def bottom_row_has_empty(state, N):
    return 0 in state[-N:]

def solve():
    # Start the search from a solved puzzle
    initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    # Set goal to be None so that we explore all states reachable from solved state
    X = Puzzle(initial_state, goal=None)
    queue, visited = [X], set()
    # add first node to visited
    visited.add(X.get_state_str())

    # BFS-search
    max_depth = 0
    longest_puzzle_to_solve = None
    expanded_nodes = 0
    while queue:
        # 1 - Choose a state for expansion
        puzzle = queue.pop(0)
        expanded_nodes += 1
        
        # How many moves we need at maximum to reach the goal state ("hardest" puzzle to solve)
        if puzzle.depth > max_depth and bottom_row_has_empty(puzzle.state, 3):
            max_depth = puzzle.depth
            longest_puzzle_to_solve = puzzle

        # 2 - See if we found a desired goal solution
        # (You would use this if we were solving puzzle with a start and a goal)
        #if state.is_solved():
        #    state.visualize()
        #    break
    
        # 3 - Go over possible actions and expand
        for action in puzzle.get_actions():
            new_state = puzzle.do_action(action)

            if new_state.get_state_str() not in visited:
                    # TODO: When new_state needs to be explored
                    # 1 - append the new_state to the queue
                    queue.append(new_state)
                    # 2 - add a str version of the state from
                    #     new_state.get_state_str() to visited
                    visited.add(new_state.get_state_str())

    print("Explored {} different board positions".format(expanded_nodes))
    print("At most {} moves required to reach goal state".format(max_depth))
    print("One of the longest puzzles found:")
    longest_puzzle_to_solve.visualize()
    print("As a list: {}".format(longest_puzzle_to_solve.state))

if __name__ == '__main__':
    solve()
