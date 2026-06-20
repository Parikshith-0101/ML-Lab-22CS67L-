from queue import PriorityQueue
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
graph = {}
heuristic = {}
for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    graph[vertex] = []
print("\nEnter heuristic values:")
for i in range(n):
    vertex = input("Vertex: ")
    h = int(input(f"Heuristic value of {vertex}: "))
    heuristic[vertex] = h
print("\nEnter edges in the format:")
print("Source Destination Cost")
for i in range(e):
    source, destination, cost = input().split()
    graph[source].append((destination, int(cost)))
start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")
def a_star(graph, heuristic, start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], 0, start, [start]))
    visited = {}
    while not pq.empty():
        f, g, node, path = pq.get()
        if node == goal:
            print("\nPath:", " -> ".join(path))
            print("Total Cost:", g)
            return
        if node in visited and visited[node] <= g:
            continue
        visited[node] = g
        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            pq.put((new_f, new_g, neighbor, path + [neighbor]))
    print("Goal Not Found!")
a_star(graph, heuristic, start, goal)