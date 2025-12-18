"""Hill Climbing search for the 8-puzzle problem."""

from Puzzle.Puzzle import (
    get_successors,
    is_goal,
    reconstruct_path,
    print_puzzle,
)
from Puzzle.State import State
from Utils.Heuristics import manhattan_distance
from Utils.Metrics import Metrics


def _normalize_initial_state(initial_board_or_state):
    """Ensure we always start from a fresh State object (depth/cost reset to 0)."""

    if isinstance(initial_board_or_state, State):
        board = list(initial_board_or_state.board)
    else:
        board = list(initial_board_or_state)

    return State(board=board, parent=None, depth=0, cost=0)


def solve(initial_board, verbose=True):
    """Simple hill climbing using the Manhattan heuristic (no sideways moves)."""

    metrics = Metrics()
    current_state = _normalize_initial_state(initial_board)

    while True:
        metrics.nodes_expanded += 1

        if is_goal(current_state):
            metrics.stop()
            solution_path = reconstruct_path(current_state)

            if verbose:
                print("\n" + "=" * 40)
                print("HILL CLIMBING REACHED THE GOAL!")
                print("=" * 40)
                for step, board in enumerate(solution_path):
                    print(f"Step {step}:")
                    print_puzzle(board)

            return {
                "solution": solution_path,
                "metrics": metrics,
                "status": "goal",
            }

        # تجمع كل الحالات المجاورة اللي نقدر نوصلها بخطوة واحدة
        neighbors = []
        for next_board in get_successors(current_state):
            neighbor = State(
                board=next_board,
                parent=current_state,
                depth=current_state.depth + 1,
                cost=current_state.cost + 1,
            )
            neighbors.append(neighbor)

        current_h = manhattan_distance(current_state.board)
        best_neighbor = None
        best_h = current_h

        # نختار أفضل جار أقل في قيمة الـ heuristic
        for neighbor in neighbors:
            neighbor_h = manhattan_distance(neighbor.board)
            if neighbor_h < best_h:
                best_h = neighbor_h
                best_neighbor = neighbor

        # لو مفيش جار أحسن → وقفنا في Local Optimum
        if best_neighbor is None:
            metrics.stop()
            plateau_path = reconstruct_path(current_state)

            if verbose:
                print("\n" + "=" * 40)
                print("Hill Climbing علق في Local Optimum") 
                print("=" * 40)
                print_puzzle(current_state.board)

            return {
                "solution": None,
                "best_path": plateau_path,
                "metrics": metrics,
                "status": "plateau",
                "message": "Reached local optimum (no better neighbor).",
            }

        current_state = best_neighbor
