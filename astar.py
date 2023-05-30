import heapq

# Class representing a node in the search tree
class Node:
    def __init__(self, state, parent=None, move=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = self.heuristic() + self.move

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.state == other.state

    # Returns the heuristic value (Manhattan distance) for the current state
    def heuristic(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                tile = self.state[i][j]
                if tile != 0:
                    goal_row = (tile - 1) // 3
                    goal_col = (tile - 1) % 3
                    distance += abs(i - goal_row) + abs(j - goal_col)
        return distance

    # Generates the possible next states from the current state
    def generate_next_states(self):
        next_states = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible moves: right, down, left, up

        for direction in directions:
            new_state = [row[:] for row in self.state]
            i, j = self.find_blank_tile()

            ni, nj = i + direction[0], j + direction[1]
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                next_states.append(new_state)

        return next_states

    # Finds the position of the blank tile in the current state
    def find_blank_tile(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    # Prints the sequence of moves from the initial state to the current state
    def print_moves(self):
        if self.parent is not None:
            self.parent.print_moves()
        print("Move:", self.move)
        print_state(self.state)
        print()

# Helper function to print the state
def print_state(state):
    for row in state:
        print(row)
    print()

# A* algorithm implementation
def solve_8_puzzle(initial_state, goal_state):
    open_list = []
    closed_list = set()

    start_node = Node(initial_state)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            print("Solution found!")
            current_node.print_moves()
            return

        closed_list.add(current_node)

        next_states = current_node.generate_next_states()
        for state in next_states:
            new_node = Node(state, current_node, current_node.move + 1)

            if new_node in closed_list:
                continue

            if new_node not in open_list:
                heapq.heappush(open_list, new_node)
            else:
                for node in open_list:
                    if node == new_node and node.cost > new_node.cost:
                        open_list.remove(node)
                        heapq.heappush(open_list, new_node)
                        break

    print("No solution found!")

# Example usage
initial_state = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 0]]  # Initial state of the puzzle

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # Goal state of the puzzle

solve_8_puzzle(initial_state, goal_state)
