from Puzzle import Puzzle
from Puzzle import State
from Utils import Metrics


def _normalize_initial_state(initial_board_or_state):
    if isinstance(initial_board_or_state, State.State):
        board = list(initial_board_or_state.board)
    else:
        board = list(initial_board_or_state)

    return State.State(board=board, depth=0, cost=0)


def depth_limited_search(state, limit, metrics, visited): 
    if Puzzle.is_goal(state):
        return state

    if limit == 0:
        return None

    visited.add(tuple(state.board))
    metrics.nodes_expanded += 1

    for next_board in Puzzle.get_successors(state):
        board_tuple = tuple(next_board)
        if board_tuple in visited:
            continue

        successor_state = State.State(
            board=next_board,
            parent=state,
            depth=state.depth + 1,
            cost=state.cost + 1,
        )

        result = depth_limited_search(successor_state, limit - 1, metrics, visited)
        if result is not None:
            return result

    visited.remove(tuple(state.board))
    return None


def solve(initial_board, max_depth=50, verbose=False):
    """Iterative Deepening Search (IDS) repeatedly runs depth-limited DFS."""

    metrics = Metrics.Metrics()
    initial_state = _normalize_initial_state(initial_board)

    for limit in range(max_depth + 1):
        visited = set()
        result_state = depth_limited_search(initial_state, limit, metrics, visited)

        if result_state is not None:
            metrics.stop()
            solution_path = Puzzle.reconstruct_path(result_state)

            if verbose:
                print("\n" + "=" * 40)
                print(f"IDS SOLUTION FOUND! (Depth limit: {limit})")
                print("=" * 40)
                for step, board in enumerate(solution_path):
                    print(f"Step {step}:")
                    Puzzle.print_puzzle(board)

            return {"solution": solution_path, "metrics": metrics}

    metrics.stop()
    return {"solution": None, "metrics": metrics}
