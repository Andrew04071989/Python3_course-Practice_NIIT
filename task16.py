# Задание 16:
# Написать реализацию встроенной функции len:
# функция принимает список, возвращает его длину.


def len_a(a):
    i = 0
    for a[i] in a:
        i += 1
    return i


li = [1, 5, "a", 10, 65, 'Name']
print(len_a(li))
