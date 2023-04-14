import numpy as np

# Зчитуємо матрицю відстаней з текстового файлу
with open('LAB2.txt', 'r') as f:
    distances = np.loadtxt(f)

# Задаємо початковий вузол
start_node = 0

# Створюємо список відвіданих вузлів та додавамо початковий вузол
visited_nodes = [start_node]

# Створюємо змінну, що міститиме вагу мінімального кісткового дерева
mst_weight = 0

# Повторюємо цикл, доки всі вузли не будуть відвідані
while len(visited_nodes) < distances.shape[0]:
    # Знаходимо найближчий невідвіданий вузол до поточного множини відвіданих вузлів
    closest_node = None
    closest_distance = np.inf
    for i in visited_nodes:
        for j in range(distances.shape[0]):
            if j not in visited_nodes and distances[i][j] < closest_distance:
                closest_node = j
                closest_distance = distances[i][j]
    # Додаємо найближчий вузол до списку відвіданих та додаємо вагу до загальної ваги мінімального кісткового дерева
    visited_nodes.append(closest_node)
    mst_weight += closest_distance

# Виводимо загальну вагу мінімального кісткового дерева
print('Minimum spanning tree weight:', mst_weight)