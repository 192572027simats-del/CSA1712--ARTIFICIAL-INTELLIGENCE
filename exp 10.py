
def astar(graph, h, start, goal):
    open_list = [(h[start], start, 0)]
    visited = set()

    while open_list:
        open_list.sort()
        f, node, g = open_list.pop(0)

        if node == goal:
            print("Goal reached:", node)
            print("Cost:", g)
            return

        if node not in visited:
            visited.add(node)

            for neighbour, cost in graph[node]:
                if neighbour not in visited:
                    new_g = g + cost
                    new_f = new_g + h[neighbour]
                    open_list.append((new_f, neighbour, new_g))

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

h = {'A': 5, 'B': 4, 'C': 4, 'D': 2, 'E': 1, 'F': 2, 'G': 0}

astar(graph, h, 'A', 'G')
