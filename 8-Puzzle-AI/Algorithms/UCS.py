import heapq
from Puzzle import Puzzle
from Puzzle import State
from Utils import Metrics


def solve(initial_board, verbose=False):
    """Uniform-Cost Search (UCS) expands the cheapest frontier node first."""

    metrics = Metrics.Metrics()
    start_state = Puzzle._normalize_initial_state(initial_board)

    frontier = []
    tie_breaker = 0
    best_cost = {tuple(start_state.board): 0}

    heapq.heappush(frontier, (0, tie_breaker, start_state))

    while frontier:
        cost, _, current_state = heapq.heappop(frontier)
        metrics.nodes_expanded += 1

        current_board = tuple(current_state.board)
        if cost > best_cost.get(current_board, float("inf")):
            continue

        if Puzzle.is_goal(current_state):
            metrics.stop()
            solution_path = Puzzle.reconstruct_path(current_state)

            if verbose:
                print("\n" + "=" * 40)
                print(f"UCS SOLUTION FOUND! (Cost: {len(solution_path) - 1})")
                print("=" * 40)
                for step, board in enumerate(solution_path):
                    print(f"Step {step}:")
                    Puzzle.print_puzzle(board)

            return {"solution": solution_path, "metrics": metrics}

        for next_board in Puzzle.get_successors(current_state):
            new_cost = current_state.cost + 1  # all moves cost 1 in 8-puzzle
            board_tuple = tuple(next_board)

            if new_cost >= best_cost.get(board_tuple, float("inf")):
                continue

            best_cost[board_tuple] = new_cost

            neighbor_state = State.State(
                board=next_board,
                parent=current_state,
                depth=current_state.depth + 1,
                cost=new_cost,
            )

            tie_breaker += 1
            heapq.heappush(frontier, (new_cost, tie_breaker, neighbor_state))

    metrics.stop()
    return {"solution": None, "metrics": metrics}

