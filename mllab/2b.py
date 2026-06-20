from queue import PriorityQueue
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
graph = {}
for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    graph[vertex] = []
print("\nEnter edges in the format:")
print("Source Destination Heuristic")
for i in range(e):
    source, destination, heuristic = input().split()
    heuristic = int(heuristic)
    graph[source].append((destination, heuristic))
start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")
def best_first_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))
    print("\nTraversal:")
    while not pq.empty():
        _, node = pq.get()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            if node == goal:
                print("\nGoal Found!")
                return
            for neighbor, heuristic in graph[node]:
                if neighbor not in visited:
                    pq.put((heuristic, neighbor))
    print("\nGoal Not Found!")
best_first_search(graph, start, goal)