# Задание 7:
# Интерполировать некие шаблоны в строке.
# Есть строка с определенного вида форматированием.
# Необходимо заменить в этой строке все вхождения шаблонов
# на их значение из словаря.
d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}


def countdown():
    s = 'Ready, set, 5, 4, 3, 2, 1, Go!'
    for key in d:
        s = s.replace(str(key), d[key])
    return s


print(countdown())
