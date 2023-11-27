# Функция без параметров
# def имя функции(параметры):
#    блок_кода
# def draw_box():
#     for _ in range(3):
#         print('*' * 10)
#
# draw_box()
# print()
# draw_box()
# print()
# draw_box()
# print()


# def print_message():
#     print('Я - Сергей,')
#     print('король британцев.')
#
# print_message()

# Функции с параметрами

# def draw_box(haight, width):
#     for _ in range(haight):
#         print('*' * width)
#
# draw_box(5, 7)
# print()
# draw_box(10, 15)
# print()
# draw_box(3, 3)
# print()
# draw_box(5, 5)
# print()
# draw_box(4, 10)
# print()
#
# n = 3
# m = 9
# draw_box(n, m)

# локальные и локальные переменные

# x = 5                        # Глобальная переменная
# def func():
#     global x
#     x += 1
#
# print(x)
# func()
# print(x)

# def func():
#     x = 5   # локальная переменная
#
# func()
# print(x)

# Функции, возращающие значения

# def func():
#     x = 5
#     x += 10
#     return x
#
# result = func()
# print(result)
#
# print(func())

# def func():
#     x = 5
#     y = 10
#     return x, y
#
# result_1, result_2 = func()
# print(result_1, result_2)
#
# result_3 = func()
# print(result_3)
# print(func())

# def func():
#     x = 5
#     print('hello')
#     return x
#
# print(func())

# lambda функции
# result = lambda x: x + 5
# print(result(4))
#
# result_1 = lambda x, y: x + y
# print(result_1(11, 5))


# 1 задание
# def primougolnik(pervi, vtoroi):
#     print(2 * (pervi + vtoroi))
#     print(pervi * vtoroi)
#
# pv = int(input("Введи первую сторону: "))
# tp = int(input("Введи вторую сторону: "))
# primougolnik(pv, tp)

# 2 Задание
def god(vis):
    if (vis % 4 == 0 and vis % 100 != 0) or vis % 400 == 0:
        print("высокосный")
    else:
        print("не высокосный")

godik = int(input("Введи год: "))
god(godik)