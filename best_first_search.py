import networkx as nx
import matplotlib.pyplot as plt


def best_first_search(graph, start, goal, heuristic):
    open_list = [(0, start)]
    closed_list = set()
    visited_path = []
    parent = {}

    while open_list:
        # Sort based on heuristic value
        open_list.sort(key=lambda x: heuristic[x[1]])

        cost, node = open_list.pop(0)

        if node not in closed_list:
            visited_path.append(node)
            closed_list.add(node)

            if node == goal:
                # Reconstruct actual path
                final_path = []
                current = goal

                while current != start:
                    final_path.append(current)
                    current = parent[current]

                final_path.append(start)
                final_path.reverse()

                return cost, final_path, visited_path

            for neighbour, neighbour_cost in graph[node]:
                if neighbour not in closed_list:
                    parent[neighbour] = node
                    open_list.append((cost + neighbour_cost, neighbour))

    return None

graph = {}
heuristic = {}

num_nodes = int(input("Enter number of nodes: "))

print("\nEnter node names:")
nodes = []
for i in range(num_nodes):
    node = input(f"Node {i+1}: ")
    nodes.append(node)

print("\nEnter heuristic values:")
for node in nodes:
    heuristic[node] = int(input(f"Heuristic value for {node}: "))

print("\nEnter neighbours and costs:")
for node in nodes:
    num_neighbours = int(input(f"\nHow many neighbours does {node} have? "))

    graph[node] = []

    for i in range(num_neighbours):
        neighbour = input(f"Enter neighbour {i+1} of {node}: ")
        cost = int(input(f"Enter cost from {node} to {neighbour}: "))
        graph[node].append((neighbour, cost))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

result = best_first_search(graph, start, goal, heuristic)

if result:
    total_cost, final_path, visited_path = result

    print("\nVisited Order:", visited_path)
    print("Best Path:", final_path)
    print("Total Cost:", total_cost)
# Simple Visualization
    G = nx.Graph()
    for node in graph:
        for neighbour, cost in graph[node]:
            G.add_edge(node, neighbour, weight=cost)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 7))
    node_colors = []
    for node in G.nodes():
        if node in final_path:
            node_colors.append("lightgreen")   
        elif node in visited_path:
            node_colors.append("yellow")       
        else:
            node_colors.append("lightblue")    
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=2000,
        font_size=12,
        font_weight='bold'
    )

    path_edges = list(zip(final_path, final_path[1:]))

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        edge_color='red',
        width=3
    )
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Best First Search Visualization")
    plt.show()

else:
    print(f"\nNo path found from {start} to {goal}")


#     Sample Input:
#     graph = {
#     'A': [('B', 11), ('C', 14), ('D', 7)],
#     'B': [('A', 11), ('E', 15)],
#     'C': [('A', 14), ('E', 8), ('D', 18), ('F', 10)],
#     'D': [('A', 7), ('F', 25), ('C', 18)],
#     'E': [('B', 15), ('C', 8), ('H', 9)],
#     'F': [('G', 20), ('C', 10), ('D', 25)],
#     'G': [],
#     'H': [('E', 9), ('G', 10)]
# }

# heuristic = {
#     'A': 40,
#     'B': 32,
#     'C': 25,
#     'D': 35,
#     'E': 19,
#     'F': 17,
#     'G': 0,
#     'H': 10
# }

# start = 'A'
# goal = 'G'

#OUTPUT

# Enter number of nodes: 8

# Enter node names:
# Node 1: A
# Node 2: B
# Node 3: C
# Node 4: D
# Node 5: E
# Node 6: F
# Node 7: G
# Node 8: H

# Enter heuristic values:
# Heuristic value for A: 40
# Heuristic value for B: 32
# Heuristic value for C: 5
# Heuristic value for D: 35
# Heuristic value for E: 19
# Heuristic value for F: 17
# Heuristic value for G: 10
# Heuristic value for H: 11

# Enter neighbours and costs:

# How many neighbours does A have? 3
# Enter neighbour 1 of A: B
# Enter cost from A to B: 11
# Enter neighbour 2 of A: C
# Enter cost from A to C: 14
# Enter neighbour 3 of A: D
# Enter cost from A to D: 7

# How many neighbours does B have? 2
# Enter neighbour 1 of B: A
# Enter cost from B to A: 11
# Enter neighbour 2 of B: E
# Enter cost from B to E: 15

# How many neighbours does C have? 4
# Enter neighbour 1 of C: A
# Enter cost from C to A: 14
# Enter neighbour 2 of C: E
# Enter cost from C to E: 8
# Enter neighbour 3 of C: D
# Enter cost from C to D: 18
# Enter neighbour 4 of C: F
# Enter cost from C to F: 10

# How many neighbours does D have? 3
# Enter neighbour 1 of D: A
# Enter cost from D to A: 7
# Enter neighbour 2 of D: F
# Enter cost from D to F: 25
# Enter neighbour 3 of D: C
# Enter cost from D to C: 18

# How many neighbours does E have? 3
# Enter neighbour 1 of E: B
# Enter cost from E to B: 15
# Enter neighbour 2 of E: C
# Enter cost from E to C: 8
# Enter neighbour 3 of E: H
# Enter cost from E to H: 9

# How many neighbours does F have? 3
# Enter neighbour 1 of F: G
# Enter cost from F to G: 20
# Enter neighbour 2 of F: C
# Enter cost from F to C: 10
# Enter neighbour 3 of F: D
# Enter cost from F to D: 25

# How many neighbours does G have? 0

# How many neighbours does H have? 2
# Enter neighbour 1 of H: E
# Enter cost from H to E: 19
# Enter neighbour 2 of H: G
# Enter cost from H to G: 11

# Enter start node: A
# Enter goal node: G

# Visited Order: ['A', 'C', 'F', 'G']
# Best Path: ['A', 'C', 'F', 'G']
# Total Cost: 44
