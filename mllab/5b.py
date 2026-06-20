import math
def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):
    if depth == height:
        return values[nodeIndex]
    if maximizingPlayer:
        best = -math.inf
        for i in range(2):
            value = alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                values,
                alpha,
                beta,
                height
            )
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf

        for i in range(2):
            value = alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                values,
                alpha,
                beta,
                height
            )
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
n = int(input("Enter number of leaf nodes (power of 2): "))
values = list(map(int, input("Enter leaf node values: ").split()))
height = int(math.log2(n))
result = alphabeta(
    0,
    0,
    True,
    values,
    -math.inf,
    math.inf,
    height
)
print("Optimal Value:", result)