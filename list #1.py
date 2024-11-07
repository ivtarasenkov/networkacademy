# Дан список некоторых целых чисел,
# найдите значение 20 в нем и, если оно присутствует,
# замените его на 200.
# Обновите список только при первом вхождении числа 20.

import random

list=[]
a=int(input("Введите количество чисел в списке "))
for i in range (a):
    list.append(random.randint(0,100))
print("Исходный список: ",list)
flag=0
for y,x in enumerate(list):
    if x == 20:
        while flag < 1:
            list[y] = 200
            flag=1
print("Новый список: ",list)