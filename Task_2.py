
# 2.Треугольник существует только тогда,
# когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить
# является ли треугольник разносторонним, равнобедренным или равносторонним.

def is_triangle():
    if a == b == c:
        return print('треугольник равносторонний.')
    if (a == b and a + b > c) or (b == c and b + c > a) or (c == a and c + a > b):
        return print('треугольник равнобедренный.')
    if a != b != c:
        print('треугольник разносторонний.')
    else:
        return print('такого треугольника не существует.')

a, b, c = int(input()), int(input()), int(input())
is_triangle()