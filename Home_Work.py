import random

# 1) Выведите на экран все числа в диапазоне от 1 до 100 кратные 7.

for i in range(1, 101):
    if not i % 7:
        print(i)

# 2) Вычислить с помощью цикла факториал числа n введенного с клавиатуры (4<n<16). Факториал числа - это произведение всех чисел от этого числа до 1. Например, 5!=5*4*3*2*1=120
print()

n = int(input("n = "))

fact = 1

if 4 < n < 16:
    for i in range(1, n + 1):
        fact *= i
    print(n, "! = ", fact, sep="")
else:
    print(n, "is out of range")

# 3) Напечатайте таблицу умножения на 5. Предпочтительно печатать 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10 и т. д.
print()

NUMBER = 5

for i in range(1, 11):
    print(i, "x", NUMBER, "=", i * NUMBER)

# 4) Выведите на экран прямоугольник из *. Причем, высота и ширина прямоугольника вводятся с клавиатуры. Например, ниже представлен прямоугольник с высотой 4 и шириной 5.
print()

width, height = int(input("width = ")), int(input("height = "))

SPACE = " "

for i in range(1, width + 1):
    print("*", end="")

print()

for j in range(2, height):
    print("*", SPACE * (width - 2), "*", sep="")

for i in range(1, width + 1):
    print("*", end="")

# 5) Дан список [0,5,2,4,7,1,3,19]. Написать программу для подсчета нечетных цифр в нем.
print()

ARRAY = [0, 5, 2, 4, 7, 1, 3, 19]

counter = 0

for number in ARRAY:
    if number % 2:
        counter += 1

print("There are", counter, "odd numbers in list")

# 6) Создайте список случайных чисел (размером 4 элемента). Создайте второй список в два раза больше первого, где первые 4 элемента должны быть равны элементам
# первого списка, а остальные элементы заполните удвоенными значением начальных. Например,
# Было → [1, 4, 7, 2]
# Стало → [1, 4, 7, 2, 2, 8, 14, 4]
print()

list_of_random_numbers_1 = random.sample(range(1, 100), 4)

list_of_random_numbers_2 = list_of_random_numbers_1[:]

for number in list_of_random_numbers_1:
    n = number * 2
    list_of_random_numbers_2.append(n)

print(list_of_random_numbers_1)
print(list_of_random_numbers_2)

# 7) Создайте список из 12 элементов. Каждый элемент этого списка представляет собой зарплату рабочего за месяц(случайное число от 7500 до 15000 грн.). Выведите этот
# список на экран и вычислите среднемесячную зарплату этого рабочего.
print()

salary = random.sample(range(7500, 15000), 12)

print(salary)
print("Average months salary:", round(sum(salary) / len(salary), 2))

# 8) Представьте в виде списка списков матрицу
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 10, 11, 12]
# [13, 14, 15, 16]
# Напишите программу, которая выведет эту матрицу на экран, вычислит и выведет сумму элементов этой матрицы.
print()

MATRIX = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

summ = 0

for row in MATRIX:
    print(row)

    tmp = row[:]
    summ += sum(tmp)

print("Sum of matrix is", summ)
