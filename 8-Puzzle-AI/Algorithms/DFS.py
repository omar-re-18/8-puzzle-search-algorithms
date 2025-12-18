from Puzzle import Puzzle
from Puzzle import State
from Utils import Metrics


def _normalize_initial_state(initial_board_or_state):
    """Return a clean State object starting from depth/cost = 0."""
    if isinstance(initial_board_or_state, State.State): # If already a State, copy its board
        board = list(initial_board_or_state.board) # Make a fresh copy to avoid side-effects
    else:
        board = list(initial_board_or_state) # Assume it's a raw board list

    return State.State(board=board, depth=0, cost=0) # Create new State with depth/cost 0


def solve(initial_board, verbose=False):
    """Depth-First Search (DFS) solver for the 8-puzzle."""

    metrics = Metrics.Metrics()
    initial_state = _normalize_initial_state(initial_board)

    stack = [initial_state]
    visited = {tuple(initial_state.board)} # Track visited states to avoid cycles

    while stack:
        current_state = stack.pop()
        metrics.nodes_expanded += 1

        if Puzzle.is_goal(current_state):
            metrics.stop()
            solution_path = Puzzle.reconstruct_path(current_state)

            if verbose: # Print the solution steps if verbose mode is on
                print("\n" + "=" * 40)
                print("DFS SOLUTION FOUND!")
                print("=" * 40)
                for step, board in enumerate(solution_path):
                    print(f"Step {step}:")
                    Puzzle.print_puzzle(board)

            return {"solution": solution_path, "metrics": metrics}

        for next_board in reversed(Puzzle.get_successors(current_state)): 
            board_tuple = tuple(next_board) 
            if board_tuple in visited:
                continue

            successor_state = State.State(
                board=next_board,
                parent=current_state,
                depth=current_state.depth + 1,
                cost=current_state.cost + 1,
            )

            visited.add(board_tuple)
            stack.append(successor_state)

    metrics.stop()
    return {"solution": None, "metrics": metrics}
