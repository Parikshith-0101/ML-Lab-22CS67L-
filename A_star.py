import networkx as nx
import matplotlib.pyplot as plt

def get_neighbors(v):
    if v in graph_nodes:
        return graph_nodes[v]
    return []

def h(n):
    return heuristic[n]

def a_star_algo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()

    g = {}
    parents = {}

    g[start_node] = 0
    parents[start_node] = start_node

    visited_nodes = []

    while len(open_set) > 0:
        n = None

        # Find node with lowest f(n) = g(n) + h(n)
        for v in open_set:
            if n is None or g[v] + h(v) < g[n] + h(n):
                n = v

        if n is None:
            print("Path does not exist!")
            return None

        visited_nodes.append(n)

        # Goal node reached
        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()

            return path, visited_nodes, g[stop_node]

        # Explore neighbors
        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            else:
                if g.get(m, float('inf')) > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None

graph_nodes = {}
heuristic = {}

num_nodes = int(input("Enter number of nodes: "))

nodes = []
print("\nEnter node names:")
for i in range(num_nodes):
    node = input(f"Node {i+1}: ")
    nodes.append(node)

print("\nEnter heuristic values:")
for node in nodes:
    heuristic[node] = int(input(f"Heuristic value for {node}: "))

print("\nEnter neighbours and edge costs:")
for node in nodes:
    num_neighbours = int(input(f"\nHow many neighbours does {node} have? "))
    graph_nodes[node] = []

    for i in range(num_neighbours):
        neighbour = input(f"Enter neighbour {i+1} of {node}: ")
        cost = int(input(f"Enter cost from {node} to {neighbour}: "))
        graph_nodes[node].append((neighbour, cost))

start_node = input("\nEnter start node: ")
stop_node = input("Enter goal node: ")


result = a_star_algo(start_node, stop_node)

if result:
    path, visited_nodes, total_cost = result

    print("\nVisited Nodes:", visited_nodes)
    print("Shortest Path:", path)
    print("Total Cost:", total_cost)


#   Visualization
    G = nx.DiGraph()

    for node in graph_nodes:
        for neighbour, cost in graph_nodes[node]:
            G.add_edge(node, neighbour, weight=cost)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 7))

    node_colors = []
    for node in G.nodes():
        if node in path:
            node_colors.append("lightgreen")   # Final path
        elif node in visited_nodes:
            node_colors.append("yellow")       # Visited nodes
        else:
            node_colors.append("lightblue")    # Other nodes

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=2000,
        font_size=12,
        font_weight='bold',
        arrows=True
    )

    path_edges = list(zip(path, path[1:]))

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        edge_color='red',
        width=3,
        arrows=True
    )

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("A* Algorithm Visualization")
    plt.show()
else:
    print(f"No path found from {start_node}  to {stop_node}")

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
# Visited Nodes: ['A', 'C', 'F', 'E', 'H', 'G']
# Shortest Path: ['A', 'C', 'E', 'H', 'G']
# Total Cost: 41
