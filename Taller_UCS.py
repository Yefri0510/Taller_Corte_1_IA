import heapq
import networkx as nx
import matplotlib.pyplot as plt

def reconstruir_camino(padre, meta):
    camino = []
    actual = meta
    while actual is not None:
        camino.append(actual)
        actual = padre.get(actual)  # Usar get para evitar KeyError
    camino.reverse()
    return camino

def ucs(grafo, inicio, meta):
    cola = [(0, inicio)] # (costo, nodo)
    visitados = set()
    costo_acumulado = {inicio: 0}
    padre = {inicio: None}

    while cola:
        costo, nodo = heapq.heappop(cola)
        if nodo in visitados:
            continue
        visitados.add(nodo)
        if nodo == meta:
            break
        for vecino, costo_arista in grafo[nodo]:
            nuevo_costo = costo + costo_arista
            if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                heapq.heappush(cola, (nuevo_costo, vecino))
                padre[vecino] = nodo

    return reconstruir_camino(padre, meta), costo_acumulado.get(meta, float('inf'))

grafo_costo = {
    'S': [('A',1),('B',1),('D',1),('E',1)],
    'A': [('F',1),('G',1)],
    'G': [],
    'F': [('M',1)],
    'M': [('N',1)],
    'N': [],
    'B': [('H',1),('R',1)],
    'H': [('O',1),('Q',1)],
    'O': [('P',1)],
    'P': [],
    'Q': [('U',1)],
    'U': [('V',1),('W',1)],
    'V': [],
    'W': [],
    'R': [('X',1),('T',1)],
    'X': [],
    'T': [('GG',1)],
    'GG': [],
    'D': [('J',1)],
    'J': [('Y',1)],
    'Y': [('Z',1)],
    'Z': [('AA',1),('BB',1)],
    'AA': [],
    'BB': [],
    'E': [('K',1),('L',1)],
    'K': [('I',1)],
    'I': [],
    'L': [('CC',1)],
    'CC': [('DD',1),('EE',1)],
    'DD': [],
    'EE': [('FF',1)],
    'FF': []   
}

start_node = 'S'
end_node = 'W'
camino, costo = ucs(grafo_costo, start_node, end_node)
print("UCS - Camino:", camino, "Costo:", costo)

# Crear un objeto dirigido de networkx
G = nx.DiGraph()

# Añadir nodos y aristas al grafo con sus costos
for node, neighbors in grafo_costo.items():
    for neighbor, weight in neighbors:
        G.add_edge(node, neighbor, weight=weight)

# Dibujar el grafo
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(12, 8))

# Dibujar nodos y aristas
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Dibujar etiquetas de costos en las aristas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Resaltar el camino si existe
if camino:
    path_edges = list(zip(camino, camino[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=camino, node_color='gold', node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='orange', width=3, arrows=True)
    plt.title(f"Trayectoria UCS de {start_node} a {end_node}\nCamino: {' -> '.join(camino)}\nCosto total: {costo}")
else:
    plt.title("No se encontró un camino")

plt.axis('off')
plt.show()