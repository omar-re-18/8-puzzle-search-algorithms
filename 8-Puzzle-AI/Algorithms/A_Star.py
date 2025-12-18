import heapq
from Puzzle.Puzzle import get_successors, is_goal
from Puzzle.State import State
from Metrics.metrics import Metrics
from Heuristics.heuristics import manhattan_distance, misplaced_tiles


def solve(initial_state , heuristic = "manhattan"):

    """
    A* Search Algorithm
    متوافق 100% مع main.py
    """

    # اختيار heuristic
    if heuristic == "manhattan":
        h_func = manhattan_distance
    else:
        h_func = misplaced_tiles

    metrics = Metrics()

    open_list = []
    closed_set = set()
    counter = 0

    # حساب f للبداية
    start_h = h_func(initial_state.board)
    start_f = initial_state.cost + start_h

    heapq.heappush(open_list, (start_f, counter, initial_state))

    while open_list:
        _, _, current_state = heapq.heappop(open_list)

        # Goal Test
        if is_goal(current_state):
            metrics.stop()
            return {
                "solution": current_state,
                "metrics": metrics
            }

        closed_set.add(current_state)
        metrics.nodes_expanded += 1

        # Expand successors
        for board in get_successors(current_state):
            child = State(
                board=board,
                parent=current_state,
                cost=current_state.cost + 1,
                depth=current_state.depth + 1
            )

            if child in closed_set:
                continue

            g = child.cost
            h = h_func(board)
            f = g + h

            counter += 1
            heapq.heappush(open_list, (f, counter, child))

    metrics.stop()
    return {
        "solution": None,
        "metrics": metrics
    }
