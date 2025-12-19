import heapq
from Puzzle import Puzzle
from Puzzle.State import State
from Utils.Metrics import Metrics
from Utils.Heuristics import manhattan_distance, misplaced_tiles

def solve(initial_board, heuristic="manhattan", verbose=False):
    """A* search with selectable heuristic (Manhattan or Misplaced Tiles)."""

    h_func = manhattan_distance if heuristic == "manhattan" else misplaced_tiles

    metrics = Metrics()
    start_state =Puzzle._normalize_initial_state(initial_board)

    open_list = []
    best_cost = {tuple(start_state.board): 0}
    counter = 0

    start_f = start_state.cost + h_func(start_state.board)
    heapq.heappush(open_list, (start_f, counter, start_state))

    while open_list:
        _, _, current_state = heapq.heappop(open_list)
        metrics.nodes_expanded += 1

        current_board = tuple(current_state.board)

        if current_state.cost > best_cost.get(current_board, float("inf")):
            continue

        if Puzzle.is_goal(current_state):
            metrics.stop()
            solution_path = Puzzle.reconstruct_path(current_state)

            if verbose:
                print("\n" + "=" * 40)
                print(f"A* SOLUTION FOUND! (Heuristic: {heuristic})")
                print("=" * 40)
                for step, board in enumerate(solution_path):
                    print(f"Step {step}:")
                    Puzzle.print_puzzle(board)

            return {"solution": solution_path, "metrics": metrics}

        for board in Puzzle.get_successors(current_state):
            g_cost = current_state.cost + 1
            board_tuple = tuple(board)

            if g_cost >= best_cost.get(board_tuple, float("inf")): 
                continue

            best_cost[board_tuple] = g_cost

            child = State(
                board=board,
                parent=current_state,
                cost=g_cost,
                depth=current_state.depth + 1,
            )

            counter += 1
            f_score = g_cost + h_func(board)
            heapq.heappush(open_list, (f_score, counter, child))

    metrics.stop()
    return {"solution": None, "metrics": metrics}
