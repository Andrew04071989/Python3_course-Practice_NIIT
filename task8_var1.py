# Задание 8 (Вариант 1):
# Есть список списков (матрица).
# Каждый внутренний список – это строка матрицы.
# Необходимо реализовать функцию,
# которая удаляет столбец, содержащий заданную цифру.
matrix = [[10, 2, 3, 5, 7],
          [3, 5, 99, 100, 21],
          [0, 8, 7, 4, 3],
          [1, 9, 3, 1, 2],
          [12, 11, 111, 661, 77]]
print(matrix)
z = int(input('Выберите и введите число из матрицы: '))


def kick_column():
    for i in matrix:
        for j in i:
            if z == j:
                n = i.index(z)
                for m in matrix:
                    del m[n]
                kick_column()
    return matrix


print(kick_column())





