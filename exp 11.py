
colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

coloring = {}

def csp(node):
    if node == len(graph):
        return True

    state = list(graph.keys())[node]

    for color in colors:
        if all(coloring.get(n) != color for n in graph[state]):
            coloring[state] = color

            if csp(node + 1):
                return True

            del coloring[state]

    return False

if csp(0):
    print(coloring)
else:
    print("No solution")
