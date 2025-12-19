import collections
from Puzzle import Puzzle
from Puzzle import State
from Utils import Metrics


def _normalize_initial_state(initial_board_or_state): 
    """Always return a fresh State instance starting from depth/cost = 0."""
    if isinstance(initial_board_or_state, State.State):
        board = list(initial_board_or_state.board)
    else:
        board = list(initial_board_or_state)

    return State.State(board=board, depth=0, cost=0)


def solve(initial_board, verbose=False):
    """Breadth-First Search (BFS) solver for the 8-puzzle."""

    metrics = Metrics.Metrics()
    initial_state = _normalize_initial_state(initial_board)

    queue = collections.deque([initial_state])
    visited = {tuple(initial_state.board)}

    while queue:
        current_state = queue.popleft() # Dequeue the front state
        metrics.nodes_expanded += 1

        if Puzzle.is_goal(current_state):
            metrics.stop()
            solution_path = Puzzle.reconstruct_path(current_state)

            if verbose:
                print("\n" + "=" * 40)
                print(f"BFS SOLUTION FOUND! (Total moves: {len(solution_path) - 1})")
                print("=" * 40)
                for i, board in enumerate(solution_path):
                    print(f"Step {i}:")
                    Puzzle.print_puzzle(board)

            return {"solution": solution_path, "metrics": metrics}

        for next_board in Puzzle.get_successors(current_state):
            board_tuple = tuple(next_board) # Convert board(list) to tuple for set operations because lists are unhashable and cannot be added to a set
            if board_tuple in visited:
                continue

            successor_state = State.State(
                board=next_board, # Create new State for the successor
                parent=current_state, # Link back to current state
                move=None,
                depth=current_state.depth + 1,
                cost=current_state.cost + 1,
            )

            visited.add(board_tuple)
            queue.append(successor_state)

    metrics.stop()
    return {"solution": None, "metrics": metrics}



