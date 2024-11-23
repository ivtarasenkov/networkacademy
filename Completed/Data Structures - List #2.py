# Поменять местами самый большой и самый маленький элементы списка

import random

s=[]
a=int(input("Введите количество чисел в списке "))
for i in range(a):
    s.append(random.randint(0,100))
print("Исходный список: ",s)
print('Самый маленький элемент: ',min(s))
print('Самый большой элемент: ',max(s))
s[s.index(min(s))],s[s.index(max(s))]=s[s.index(max(s))],s[s.index(min(s))]
print("Новый список: ",s)
