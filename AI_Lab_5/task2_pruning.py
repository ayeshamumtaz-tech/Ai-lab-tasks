#Minimax and Alpha-Beta Pruning
def minimax(node, depth, maximizing):
 
    if depth == 0:
        return node, 1
    if maximizing:
        best_value = float("-inf")
        leaf_count = 0
        for child in node:
            value, count = minimax(child, depth - 1, False)
            leaf_count += count
            best_value = max(best_value, value)
        return best_value, leaf_count
    else:
        best_value = float("inf")
        leaf_count = 0
        for child in node:
            value, count = minimax(child, depth - 1, True)
            leaf_count += count
            best_value = min(best_value, value)
        return best_value, leaf_count

def alpha_beta(node, depth, alpha, beta, maximizing):

    if depth == 0:
        return node, 1
    if maximizing:
        best_value = float("-inf")
        leaf_count = 0

        for child in node:
            value, count = alpha_beta(child, depth - 1, alpha, beta, False)
            leaf_count += count
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
        return best_value, leaf_count
    else:
        best_value = float("inf")
        leaf_count = 0

        for child in node:
            value, count = alpha_beta(child, depth - 1, alpha, beta, True)
            leaf_count += count
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if alpha >= beta:
                break
        return best_value, leaf_count

# Original game tree
tree = [[[3, 5], [2, 9]], [[0, 7], [0, 0]]]
# Reversed branch order
reverse_tree = [[[0, 0], [0, 7]], [[2, 9], [3, 5]]]

# Normal order comparison
print("NORMAL BRANCH ORDER")
value, count = minimax(tree, 3, True)
print("Minimax Value:", value)
print("Leaf Count:", count)
value, count = alpha_beta(tree, 3, float("-inf"), float("inf"), True)
print("Alpha-Beta Value:", value)
print("Leaf Count:", count)

# Reversed order comparison
print("\nREVERSED BRANCH ORDER")
value, count = minimax(reverse_tree, 3, True)
print("Minimax Value:", value)
print("Leaf Count:", count)
value, count = alpha_beta(reverse_tree, 3, float("-inf"), float("inf"), True)
print("Alpha-Beta Value:", value)
print("Leaf Count:", count)

# Edge case: All leaf values are equal
print("\nEDGE CASE TEST")
edge_tree = [[4, 4], [4, 4]]
value, count = minimax(edge_tree, 2, True)
print("Minimax Value:", value)
value, count = alpha_beta(edge_tree, 2, float("-inf"), float("inf"), True)
print("Alpha-Beta Value:", value)
