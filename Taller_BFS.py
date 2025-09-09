import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return "Start and goal noder are the same"
    
    while queue:
        path = queue.popleft()

        node = path[-1]

        if node not in visited:
            neighbors = graph.get(node,[])

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path
            
            visited.add(node)

    return "No path found between start and goal"

#Exmaple graph represented as an adjacency list

graph = {
    'S': ['A','B','D','E'],
    'A': ['F','G'],
    'G': [],
    'F': ['M'],
    'M': ['N'],
    'N': [],
    'B': ['H','R'],
    'H': ['O','Q'],
    'O': ['P'],
    'P': [],
    'Q': ['U'],
    'U': ['V','W'],
    'V': [],
    'W': [],
    'R': ['X','T'],
    'X': [],
    'T': ['GG'],
    'GG': [],
    'D': ['J'],
    'J': ['Y'],
    'Y': ['Z'],
    'Z': ['AA','BB'],
    'AA': [],
    'BB': [],
    'E': ['K','L'],
    'K': ['I'],
    'I': [],
    'L': ['CC'],
    'CC': ['DD','EE'],
    'DD': [],
    'EE': ['FF'],
    'FF': []   
}

start_node = 'S'
end_node = 'W'
print("BFS Path:", bfs(graph, start_node, end_node))
path = bfs(graph, start_node, end_node)

# Crear un objeto dirigido de networkx
G = nx.DiGraph()

# Añadir nodos y aristas al grafo
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Dibujar el grafo
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 8))

# Dibujar nodos y aristas
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Resaltar el camino si existe
if path:
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='lightgreen', node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=2, arrows=True)
    plt.title(f"Trayectoria de {start_node} a {end_node}\nCamino: {' -> '.join(path)}")
else:
    plt.title("No se encontró un camino")

plt.axis('off')
plt.show()