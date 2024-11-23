# Для заданного интервала вывести все простые числа

import random

a=int(input("Введите нижнюю гарницу отрезка: "))
b=int(input("Введите верхнюю гарницу отрезка: "))
c=[]
if a>b:
    a,b=b,a

for i in range(a,b+1):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            c.append(i)
print(c)
