# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
from random import sample

def list_rand_nums(count: int):
    if count <= 0:
        print("отрицательных чисел нет ")
        return []
    
    list_nums = sample(range(1,count * 2), count)
    return list_nums

def sum_odd_pos(list_nums: list):
    sum_num = 0
    for k in range(0, len(list_nums), 2):
        sum_num += list_nums[k]
    return sum_num

all_list = list_rand_nums(int(input("введите количество чисел ")))
print(all_list)
print(sum_odd_pos(all_list))