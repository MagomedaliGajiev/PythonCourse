

n = input('Введите число N: ')
list = []
count = 0

for i in range(n):
    list.append(input())
x = input('Введите число X: ')

for i in list:
    if x == list[i]:
        count += 1
