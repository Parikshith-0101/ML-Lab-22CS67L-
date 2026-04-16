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