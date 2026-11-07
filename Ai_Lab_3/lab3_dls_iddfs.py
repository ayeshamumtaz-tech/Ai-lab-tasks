class Search:
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["G"],
        "F": [],
        "G": []
    }
    def dls(self, node, goal, limit, path):
        # FOUND: Goal has been reached.
        if node == goal:
            return "FOUND", path
        # At the depth limit, check if deeper nodes are available.
        if limit == 0:
            for n in self.graph[node]:
                if n not in path:
                    return "CUTOFF", None
            return "FAILURE", None
        cutoff = False
        for n in self.graph[node]:
            # Path checking prevents cycles in the current path.
            if n not in path:
                status, result = self.dls(n, goal, limit - 1, path + [n])
                if status == "FOUND":
                    return status, result
                if status == "CUTOFF":
                    cutoff = True
        if cutoff:
            return "CUTOFF", None
        return "FAILURE", None

    def iddfs(self, start, goal, maximum):
        # IDDFS repeats DLS with increasing depth limits.Each iteration starts with a fresh path.
        attempted = []
        for limit in range(maximum + 1):
            attempted.append(limit)
            status, path = self.dls(start, goal, limit, [start])
            if status == "FOUND" or status == "FAILURE":
                return status, path, attempted
        return "CUTOFF", None, attempted
s = Search()
print("DLS RESULTS")
for limit in range(1, 5):
    status, path = s.dls("A", "G", limit, ["A"])
    print("Limit:", limit, "| Status:", status, "| Path:", path)
print("\nIDDFS RESULT")
status, path, limits = s.iddfs("A", "G", 4)
print("Status:", status)
print("Path:", path)
print("Limits Attempted:", limits)
# Test 1: Start node is already the goal.
print("\nSTART EQUALS GOAL")
print(s.dls("A", "A", 0, ["A"]))
# Test 2: Goal does not exist in the graph.
print("\nUNREACHABLE GOAL")
print(s.dls("A", "Z", 4, ["A"]))
# Test 3: Graph contains a cycle.
cycle_search = Search()
cycle_search.graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": []
}
print("\nCYCLE TEST")
print(cycle_search.dls("A", "C", 3, ["A"]))
