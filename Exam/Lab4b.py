def a_star(graph, start, goal, h):

    open_list = [start]
    closed_list = set()

    g = {start: 0}
    parent = {start: None}

    while open_list:

        # Select node with minimum f(n)=g(n)+h(n)
        current = min(open_list, key=lambda x: g[x] + h[x])

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Path:", path)
            print("Cost:", g[goal])

            return path

        open_list.remove(current)
        closed_list.add(current)

        for neighbour, cost in graph[current]:

            new_cost = g[current] + cost

            if neighbour not in open_list and neighbour not in closed_list:

                open_list.append(neighbour)
                parent[neighbour] = current
                g[neighbour] = new_cost

            elif new_cost < g.get(neighbour, float('inf')):

                g[neighbour] = new_cost
                parent[neighbour] = current

                if neighbour in closed_list:
                    closed_list.remove(neighbour)
                    open_list.append(neighbour)

    print("No Path Found")
    return None


graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],
    'G': []
}

h = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0
}

a_star(graph, 'S', 'G', h)
