# Task 3: Reordering Branches
from task2_pruning import alpha_beta
tree1 = [
    [2, 8],
    [6, 9],
    [1, 7]
]
tree2 = [
    [6, 9],
    [2, 8],
    [1, 7]
]
result1, count1 = alpha_beta(tree1, 2, float("-inf"), float("inf"), True)
result2, count2 = alpha_beta(tree2, 2, float("-inf"), float("inf"), True)

print("Original Order:")
print("Minimax Value:", result1)
print("Leaves Evaluated:", count1)

print("\nReordered Branches:")
print("Minimax Value:", result2)
print("Leaves Evaluated:", count2)

print("\nSame Minimax Value:", result1 == result2)
print("Pruning Changed:", count1 != count2)