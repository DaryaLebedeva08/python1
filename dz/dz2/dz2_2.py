# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]


n=int(input("Введите целое число "))
list_num = []
m = 1
for i in range (n):
    m *= i+1
    list_num.append (m)
print (list_num)
