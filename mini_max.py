import math
import networkx as nx
import matplotlib.pyplot as plt

visited_nodes = []
node_values = {}

def minmax(depth, node_index, maximizing_player, values, max_depth):
    visited_nodes.append(node_index)

    # Leaf node
    if depth == max_depth:
        leaf_index = node_index - (2**max_depth - 1)
        val = values[leaf_index]
        node_values[node_index] = val
        return val

    if maximizing_player:
        best = -math.inf
        for i in range(2):
            child = 2 * node_index + i + 1
            value = minmax(depth + 1, child, False, values, max_depth)
            best = max(best, value)
    else:
        best = math.inf
        for i in range(2):
            child = 2 * node_index + i + 1
            value = minmax(depth + 1, child, True, values, max_depth)
            best = min(best, value)

    node_values[node_index] = best
    return best


max_depth = int(input("Enter depth of tree: "))
num_leaf_nodes = 2 ** max_depth

print(f"Enter {num_leaf_nodes} terminal node values:")
values = [int(input(f"Value {i+1}: ")) for i in range(num_leaf_nodes)]

result = minmax(0, 0, True, values, max_depth)

print("\nTerminal Node Values:", values)
print("Optimal Value:", result)



G = nx.DiGraph()
labels = {}
pos = {}

def build_tree(node_index, depth, x, y, spacing):
    node_name = f"N{node_index}"

    # Label with value (for both internal + leaf)
    val = node_values.get(node_index, "")
    labels[node_name] = f"{node_name}\n{val}"

    pos[node_name] = (x, y)

    if depth < max_depth:
        left = 2 * node_index + 1
        right = 2 * node_index + 2

        G.add_edge(node_name, f"N{left}")
        G.add_edge(node_name, f"N{right}")

        build_tree(left, depth + 1, x - spacing, y - 1, spacing / 2)
        build_tree(right, depth + 1, x + spacing, y - 1, spacing / 2)


build_tree(0, 0, 0, 0, 8)

plt.figure(figsize=(14, 8))

node_colors = [
    "lightgreen" if int(node[1:]) in visited_nodes else "lightblue"
    for node in G.nodes()
]

nx.draw(
    G,
    pos,
    labels=labels,
    with_labels=True,
    node_color=node_colors,
    node_size=2500,
    font_size=9,
    font_weight='bold'
)

plt.title("Minimax Tree (All Node Values Shown)")
plt.show()
