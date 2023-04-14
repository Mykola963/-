def are_isomorphic(graph1, graph2):
    if len(graph1) != len(graph2):
        return False

    # порівнюємо множини ступенів кожної вершини у графах
    degrees1 = sorted([sum(graph1[i]) for i in range(len(graph1))])
    degrees2 = sorted([sum(graph2[i]) for i in range(len(graph2))])
    if degrees1 != degrees2:
        return False

    # створюємо множини вершин, які мають кожен окремий ступінь
    degree_sets1 = {}
    degree_sets2 = {}
    for i in range(len(graph1)):
        degree1 = sum(graph1[i])
        if degree1 not in degree_sets1:
            degree_sets1[degree1] = {i}
        else:
            degree_sets1[degree1].add(i)

        degree2 = sum(graph2[i])
        if degree2 not in degree_sets2:
            degree_sets2[degree2] = {i}
        else:
            degree_sets2[degree2].add(i)

    # порівнюємо множини вершин кожного ступеня
    for key in degree_sets1:
        if degree_sets1[key] != degree_sets2[key]:
            return False

    # порівнюємо множини суміжних вершин для кожної вершини
    vertex_sets1 = []
    vertex_sets2 = []
    for i in range(len(graph1)):
        vertex_set1 = set([j for j in range(len(graph1)) if graph1[i][j] == 1])
        vertex_set2 = set([j for j in range(len(graph2)) if graph2[i][j] == 1])
        if vertex_set1 not in vertex_sets1:
            vertex_sets1.append(vertex_set1)
        if vertex_set2 not in vertex_sets2:
            vertex_sets2.append(vertex_set2)

    # порівнюємо множини суміжних вершин кожної вершини
    return sorted(vertex_sets1) == sorted(vertex_sets2)

# матриці графів
matrix1 = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

matrix2 = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

# перевірка ізоморфізму графів
if are_isomorphic(matrix1, matrix2):
    print("Матриці задають ізоморфні графи")
else:
    print("Матриці не задають ізоморфні")

