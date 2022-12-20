# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.
from random import sample

def num_find (len_list, number):
    
    new_list = sample (range(1, len_list * 2), k=len_list)
    print (new_list)
    if number in new_list:
        return ("входит")
    return ("не входит")
print (num_find (int (input("введите длину списка ")), int(input("введите число "))))