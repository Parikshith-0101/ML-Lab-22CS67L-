import math
import networkx as nx
import matplotlib.pyplot as plt

visited_nodes = []
pruned_nodes = []

def alphabeta(depth, node_index, maximizing_player, values, alpha, beta, max_depth):
    current_node = f"N{node_index}"
    visited_nodes.append(current_node)

    # Leaf node reached
    if depth == max_depth:
        return values[node_index]

    if maximizing_player:
        best = -math.inf

        for i in range(2):
            child_index = node_index * 2 + i
            child_node = f"N{child_index}"

            value = alphabeta(
                depth + 1,
                child_index,
                False,
                values,
                alpha,
                beta,
                max_depth
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                # Remaining child is pruned
                for j in range(i + 1, 2):
                    pruned_child = f"N{node_index * 2 + j}"
                    pruned_nodes.append(pruned_child)
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            child_index = node_index * 2 + i
            child_node = f"N{child_index}"

            value = alphabeta(
                depth + 1,
                child_index,
                True,
                values,
                alpha,
                beta,
                max_depth
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                # Remaining child is pruned
                for j in range(i + 1, 2):
                    pruned_child = f"N{node_index * 2 + j}"
                    pruned_nodes.append(pruned_child)
                break

        return best


max_depth = int(input("Enter depth of tree: "))

num_leaf_nodes = 2 ** max_depth
print(f"Enter {num_leaf_nodes} terminal node values:")

values = []
for i in range(num_leaf_nodes):
    value = int(input(f"Value {i+1}: "))
    values.append(value)


result = alphabeta(
    0,
    0,
    True,
    values,
    -math.inf,
    math.inf,
    max_depth
)

print("\nTerminal Node Values:", values)
print("Optimal Value:", result)
print("Pruned Nodes:", pruned_nodes)


# Visualization
G = nx.DiGraph()
labels = {}
pos = {}

def build_tree(node_index, depth, x, y, spacing):
    current_node = f"N{node_index}"

    # Label leaf nodes with terminal values
    if depth == max_depth:
        labels[current_node] = str(values[node_index])
    else:
        labels[current_node] = current_node

    pos[current_node] = (x, y)

    if depth < max_depth:
        left_child = f"N{node_index * 2}"
        right_child = f"N{node_index * 2 + 1}"

        G.add_edge(current_node, left_child)
        G.add_edge(current_node, right_child)

        build_tree(node_index * 2, depth + 1, x - spacing, y - 1, spacing / 2)
        build_tree(node_index * 2 + 1, depth + 1, x + spacing, y - 1, spacing / 2)

build_tree(0, 0, 0, 0, 4)

plt.figure(figsize=(14, 8))

node_colors = []
for node in G.nodes():
    if node in pruned_nodes:
        node_colors.append("red")         
    elif node in visited_nodes:
        node_colors.append("lightgreen")   
    else:
        node_colors.append("lightblue")    

nx.draw(
    G,
    pos,
    labels=labels,
    with_labels=True,
    node_color=node_colors,
    node_size=2500,
    font_size=10,
    font_weight='bold'
)

plt.title("Alpha-Beta Pruning Visualization")
plt.show()