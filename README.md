# 🧩 8-Puzzle AI Project

## 📌 Overview

This project addresses the classic 8-Puzzle problem, a well-known problem in Artificial Intelligence, by applying and comparing multiple search algorithms.

The main objective is to analyze and compare uninformed and informed search strategies based on:

- Execution time
- Number of expanded nodes
- Solution optimality
- Path cost

The project is implemented in Python as part of an AI academic course.

## 🧠 Implemented Search Algorithms

The following algorithms are implemented and evaluated:

### 🔹 Uninformed Search

1- Breadth-First Search (BFS)  
2- Depth-First Search (DFS)  
3- Uniform-Cost Search (UCS)  
4- Iterative Deepening Search (IDS)

### 🔹 Informed / Heuristic Search

1- A* Search (A*)  
2- Hill Climbing

## 🧩 Problem Description

The 8-Puzzle consists of a 3×3 grid containing numbers from 1 to 8 and one empty tile.
The goal is to reach a predefined goal state by sliding tiles into the empty position using the minimum number of moves (when applicable).

## 📂 Project Structure

```

8-puzzle-ai/
│
├── algorithms/ # Search algorithms implementations
│ ├── BFS.py
│ ├── DFS.py
│ ├── UCS.py
│ ├── IDS.py
│ ├── A_Star.py
│ └── Hill_Climbing.py
│
├── puzzle/ # Puzzle logic and state representation
│ ├── state.py
│ └── puzzle.py
│
├── utils/ # Heuristics and performance metrics
│ ├── heuristics.py
│ └── metrics.py
│
├── experiments/ # Scripts for running comparisons
│ └── run_all.py
│
├── report/ # Final report and analysis
│ └── Report File
│
├── main.py # Project entry point
└── README.md
```

## ▶️ How to Run the Project

### Run a single algorithm

- python main.py

### Run all algorithms and compare their performance

- python experiments/run_all.py

## 📊 Evaluation Metrics

For each algorithm, the following metrics are collected and analyzed:

- Execution Time
- Number of Expanded Nodes
- Path Cost
- Solution Depth
- Space Complexity
- Optimality (Yes / No)

These metrics are used to produce a detailed comparison in the final report.

## 🧪 Heuristics Used (A\*)

- Misplaced Tiles Heuristic
- Manhattan Distance Heuristic

Both heuristics are admissible, ensuring optimal solutions for A\*.

## 📦 Requirements

- Python 3.x

No external libraries required (standard Python only)

## 👥 Team Members

- Donya Sameh Fathy Abdelshafy

- Ahmed Ashraf Elsayed Kamal

- Ahmed Awad Hassan Mohamed

- Omar Hany Fathy Ali

## 📄 Notes

- The project is designed for educational and experimental purposes.

- Results may vary depending on the initial puzzle configuration.

- Hill Climbing does not guarantee an optimal solution.

## ⭐ Acknowledgment

This project was developed as part of an Artificial Intelligence course to demonstrate practical implementation of search algorithms and performance evaluation.
