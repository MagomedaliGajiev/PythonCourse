# Задача №17. Решение в группах Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] 
# Output: 6



spisok = [1, 1, 2, 2, 0, -1, 3, 4, 4, 4, 9]

# amount_of_numbers = 1
# for i in range(0, len(spisok) - 1):
#     if spisok[i] != spisok[i + 1]:
#         amount_of_numbers += 1

print(len(set(spisok)))