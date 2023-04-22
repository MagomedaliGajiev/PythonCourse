# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те
# числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств

n = int(input('Enter a number n: '))
m = int(input('Enter a number m: '))

first_sequence = list()
second_sequence = list()

for i in range(n):
    first_sequence.append(int(input('Enter number of the first sequence: ')))

for i in range(m):
    second_sequence.append(int(input('Enter number of the second sequence: ')))

res = sorted(set(first_sequence).intersection(set(second_sequence)))

print(*res)
