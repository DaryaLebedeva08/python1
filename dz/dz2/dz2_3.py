# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in 
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

n = int(input("Введите количество чисел "))
sum_n = 0
list_n = []
for i in range(1, n+1):
    itog = round((1+1 / i) ** i, 3)
    list_n.append(itog)
    sum_n += itog
print(list_n)
print(sum_n)