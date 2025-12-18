from Algorithms import BFS, DFS, UCS, IDS, A_Star, Hill_Climbing
from Puzzle.Puzzle import is_solvable, print_puzzle


# --- الإعدادات العامة ---
INITIAL_CONFIGS = {
    "Solvable": [
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    ]
}

ALGORITHMS = {
    "BFS": BFS.solve,
    "DFS": DFS.solve,
    "UCS": UCS.solve,
    "IDS": IDS.solve,
    "A* (Manhattan)": lambda board: A_Star.solve(board, heuristic="manhattan"),
    "A* (Misplaced)": lambda board: A_Star.solve(board, heuristic="misplaced"),
    "Hill Climbing": Hill_Climbing.solve,
}


def _format_board(board):
    lines = []
    for r in range(0, 9, 3):
        row = board[r : r + 3]
        lines.append("  " + " | ".join(str(tile) for tile in row))
    return "\n".join(lines)


def _summarize_run(algo_name, board_name, board, solve_fn):
    try:
        result = solve_fn(board)
    except Exception as exc:  # التقاط أي أخطاء غير متوقعة أثناء التنفيذ
        return {
            "algorithm": algo_name,
            "board_type": board_name,
            "status": "error",
            "path_cost": None,
            "nodes": None,
            "time_ms": None,
            "note": f"Exception: {exc}",
        }

    metrics = result.get("metrics")
    solution = result.get("solution")
    best_path = result.get("best_path")  # خاص بـ Hill Climbing لما يعلق في Plateaus

    if solution:
        path_cost = len(solution) - 1
        status = "Solved"
    elif best_path:
        path_cost = len(best_path) - 1
        status = result.get("status", "Plateau")
    else:
        path_cost = None
        status = result.get("status", "No Solution")

    nodes = metrics.nodes_expanded if metrics else None
    time_ms = metrics.time_taken if metrics else None

    note = result.get("message")
    return {
        "algorithm": algo_name,
        "board_type": board_name,
        "status": status,
        "path_cost": path_cost,
        "nodes": nodes,
        "time_ms": time_ms,
        "note": note,
    }


def _print_report_section(board_name, board, rows):
    solvable = is_solvable(board)
    header = f"\n{'=' * 70}\nTest: {board_name} (Solvable = {solvable})\n{'=' * 70}"
    print(header)
    print("Initial Board:")
    print(_format_board(board))

    columns = [
        ("Algorithm", 18),
        ("Status", 14),
        ("Path Cost", 15),
        ("Nodes", 12),
        ("Time (ms)", 12),
        ("Note", 20),
    ]

    def fmt(text, width):
        txt = "-" if text in (None, "") else str(text)
        return txt[: width - 1].ljust(width)

    header_line = "".join(fmt(name, width) for name, width in columns)
    print("\n" + header_line)
    print("-" * len(header_line))

    for row in rows:
        if row["board_type"] != board_name:
            continue
        line = "".join(
            [
                fmt(row["algorithm"], 18),
                fmt(row["status"], 14),
                fmt(row["path_cost"], 15),
                fmt(row["nodes"], 12),
                fmt(f"{row['time_ms']:.2f}" if row["time_ms"] else None, 12),
                fmt(row.get("note"), 20),
            ]
        )
        print(line)


def main():
    summary_rows = []

    for board_name, board in INITIAL_CONFIGS.items():
        board_rows = []

        solvable = is_solvable(board)

        for algo_name, solve_fn in ALGORITHMS.items():

            # 🚫 لو الحالة Unsolvable → نتخطى Algorithms البحث الكامل
            if not solvable and algo_name in ("BFS", "DFS", "UCS", "IDS"):
                board_rows.append({
                    "algorithm": algo_name,
                    "board_type": board_name,
                    "status": "Skipped",
                    "path_cost": None,
                    "nodes": None,
                    "time_ms": None,
                    "note": "Unsolvable state",
                })
                continue

            board_rows.append(
                _summarize_run(algo_name, board_name, board, solve_fn)
            )

        summary_rows.extend(board_rows)
        _print_report_section(board_name, board, board_rows)

    print("\n" + "#" * 70)
    print("All algorithms have been run on both cases and the results are shown above.")
    print("#" * 70)


if __name__ == "__main__":
    main()
