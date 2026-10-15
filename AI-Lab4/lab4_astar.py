# Lab 4: Informed Search - Heuristics and A*
# Simple priority queue using sort() and pop(0)
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}
heuristic = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}
def search(h, name):
    queue = []
    visited = []
    best_cost = {"S": 0}
    queue.append((h["S"], 0, "S", ["S"]))
    expanded = 0

    print()
    print(name)

    while queue:
        queue.sort()
        f, cost, node, path = queue.pop(0)

        if node in visited:
            continue

        if cost != best_cost[node]:
            continue

        visited.append(node)
        print("Node:", node, "Cost:", cost, "f:", f)

        if node == "G":
            print("Path:", " -> ".join(path))
            print("Total cost:", cost)
            print("Processed nodes:", visited)
            print("Expanded nodes:", expanded)
            return path, cost, visited, expanded

        expanded = expanded + 1

        for child, edge_cost in graph[node]:
            new_cost = cost + edge_cost

            if child not in best_cost or new_cost < best_cost[child]:
                best_cost[child] = new_cost
                new_f = new_cost + h[child]
                queue.append((new_f, new_cost, child, path + [child]))

    print("Goal not found.")
    return [], None, visited, expanded

# Task 2: A* with the given heuristic
search(heuristic, "A* with given heuristic")

# Task 3-A: UCS uses a heuristic of zero for every node
zero_h = {
    "S": 0,
    "A": 0,
    "B": 0,
    "C": 0,
    "G": 0
}
search(zero_h, "Uniform Cost Search (UCS)")

# Task 3-B: Change only h(C) to 10
high_h = heuristic.copy()
high_h["C"] = 10
search(high_h, "A* with h(C) = 10")