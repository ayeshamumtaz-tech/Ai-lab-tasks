# Lab 3 – Search Algorithms

This lab covers two tasks using the given graph. Task 3 (Weighted UCS) is not included because it was skipped as instructed.

## Files

- `lab3_bfs_dfs.py` – Task 1: Breadth-First Search (BFS) and Depth-First Search (DFS).
- `lab3_dls_iddfs.py` – Task 2: Depth-Limited Search (DLS) and Iterative Deepening DFS (IDDFS).

## Graph Used

```python
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
```

## Task 1 – BFS and DFS

BFS uses a queue (FIFO) and explores the graph level by level. DFS uses a stack (LIFO) and explores one branch deeply before moving to another.

**Results:**

| Algorithm | Visit Order | Final Path |
|---|---|---|
| BFS | A, B, C, D, E, F, G | A → B → E → G |
| DFS | A, B, D, E, G | A → B → E → G |

Both algorithms find the same path, but their visit orders are different.

## Task 2 – DLS and IDDFS

DLS searches up to a fixed depth limit. IDDFS runs DLS repeatedly with increasing limits until the goal is found.

**DLS results:**

| Depth Limit | Status | Path |
|---|---|---|
| 1 | CUTOFF | Not Found |
| 2 | CUTOFF | Not Found |
| 3 | FOUND | A → B → E → G |
| 4 | FOUND | A → B → E → G |

**IDDFS results:**

| Maximum Depth | Status | Path | Limits Attempted |
|---|---|---|---|
| 1 | CUTOFF | Not Found | 0, 1 |
| 2 | CUTOFF | Not Found | 0, 1, 2 |
| 3 | FOUND | A → B → E → G | 0, 1, 2, 3 |
| 4 | FOUND | A → B → E → G | 0, 1, 2, 3 |

IDDFS stops when it finds the goal, so it does not attempt limit 4 when the maximum depth is 4 and the goal is found at limit 3.

**Why limits below 3 do not succeed:** The root node A is at depth 0 and G is at depth 3. Therefore, limits 1 and 2 cannot reach G.

**Repeated work:** IDDFS starts again from the root for each new depth limit. Some nodes are therefore visited more than once, but this allows it to search progressively deeper.

**Edge-case tests:**

| Test | Result |
|---|---|
| Start node is the goal (A to A) | FOUND |
| Unreachable goal (Z) | FAILURE |
| Graph containing a cycle | FOUND: A → B → C |

Path checking prevents a node already in the current path from being visited again.

## How to Run

Run each Python file separately:

```bash
python lab3_bfs_dfs.py
python lab3_dls_iddfs.py
```

## Key Concepts

- **BFS:** Queue, FIFO, level-by-level search.
- **DFS:** Stack, LIFO, deep-first search.
- **DLS:** DFS with a fixed depth limit.
- **IDDFS:** Repeats DLS with increasing depth limits.
- **FOUND:** The goal is reached.
- **CUTOFF:** The depth limit prevents the search from going deeper.
- **FAILURE:** The search finishes without finding a path.
