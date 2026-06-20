import math
def minimax(depth, nodeIndex, maximizingPlayer, values, height):
    if depth == height:
        return values[nodeIndex]
    if maximizingPlayer:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )
n = int(input("Enter number of leaf nodes (power of 2): "))
values = list(map(int, input("Enter leaf node values: ").split()))
height = int(math.log2(n))
result = minimax(0, 0, True, values, height)
print("Optimal Value:", result)