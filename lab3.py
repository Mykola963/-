import numpy as np
import itertools

# Зчитуємо матрицю відстаней з текстового файлу
with open('LAB3.txt', 'r') as f:
    distances = np.loadtxt(f)

# Визначаємо кількість вузлів
n = distances.shape[0]

# Створюємо список усіх можливих перестановок вузлів
permutations = itertools.permutations(range(n))

# Ініціалізуємо змінну, що буде містити найдешевший шлях
min_distance = np.inf

# Перебираємо усі можливі перестановки вузлів
for permutation in permutations:
    # Ініціалізуємо змінну, що буде містити відстань для поточної перестановки
    distance = 0
    # Обчислюємо відстань для поточної перестановки
    for i in range(n-1):
        distance += distances[permutation[i]][permutation[i+1]]
    # Додаємо відстань від останнього вузла до першого, щоб закрити цикл
    distance += distances[permutation[-1]][permutation[0]]
    # Перевіряємо, чи є поточна відстань меншою за мінімальну
    if distance < min_distance:
        min_distance = distance

# Виводимо найдешевший шлях
print('Minimum distance:', min_distance)
