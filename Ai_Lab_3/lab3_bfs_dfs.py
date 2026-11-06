from collections import deque
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def bfs(start, goal):
    # BFS uses FIFO queue and explores level by level.
    q = deque([[start]])
    seen = {start}
    visited = []

    while q:
        path = q.popleft()
        node = path[-1]
        visited.append(node)
        if node == goal:
            return visited, path
        for x in graph[node]:
            if x not in seen:
                seen.add(x)
                q.append(path + [x])

def dfs(start, goal):
    # DFS uses LIFO stack and explores one branch deeply first.
    stack = [[start]]
    seen = set()
    visited = []

    while stack:
        path = stack.pop()
        node = path[-1]
        if node in seen:
            continue
        seen.add(node)
        visited.append(node)
        if node == goal:
            return visited, path
        # Reversed order keeps the original successor order in DFS.
        for x in reversed(graph[node]):
            if x not in seen:
                stack.append(path + [x])
bfs_order, bfs_path = bfs("A", "G")
dfs_order, dfs_path = dfs("A", "G")
print("BFS Visit Order:", bfs_order)
print("BFS Final Path:", bfs_path)

print("\nDFS Visit Order:", dfs_order)
print("DFS Final Path:", dfs_path)