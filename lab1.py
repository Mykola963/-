from numpy import inf

def read_graph_from_file(filename):
    """
    Зчитує матрицю суміжності графу з файлу filename.
    Повертає матрицю суміжності графу.
    """
    with open(filename, 'r') as f:
        num_vertices = int(f.readline().strip())
        graph = []
        for _ in range(num_vertices):
            row = [float('inf' if x == 'inf' else x) for x in f.readline().strip().split()]
            graph.append(row)
    return graph

def boruvka_mst(graph):
    """
    Знаходить мінімальний каркас графу за допомогою алгоритму Борувки.
    Повертає множину ребер, що входять до каркасу.
    """
    num_vertices = len(graph)
    mst = set()   # зберігає мінімальний каркас
    components = [{i} for i in range(num_vertices)]   # початкові компоненти

    while len(components) > 1:
        cheapest_edges = [None] * num_vertices   # зберігає найменше ребро для кожної компоненти

        # знаходимо найменше ребро для кожної компоненти
        for i in range(num_vertices):
            for j in range(num_vertices):
                if cheapest_edges[i] is None or graph[i][j] < graph[i][cheapest_edges[i]]:
                    cheapest_edges[i] = j

        # додаємо в каркас ребра для кожної компоненти
        for i in range(num_vertices):
            j = cheapest_edges[i]
            if j is not None:
                component_i = next((component for component in components if i in component))
                component_j = next((component for component in components if j in component))
                if component_i != component_j:
                    mst.add((i, j))
                    component_i |= component_j
                    components.remove(component_j)

    return mst

filename = 'graph.txt'
graph = read_graph_from_file(filename)
mst = boruvka_mst(graph)
print(mst)