# Задача 1
# Пользователь определяет размеры отрезка в диапазоне 0 до 1000.
# Выполнить контроль ввода данных
# - если пользователь ввел отрицательное число
# - если пользователь ввел число вне отрезка
# Датчик случайных чисел генерирует 10 чисел в диапазоне  0 до 1000.
# Подсчитать количество чисел попавших в заданный отрезок и их вывести
# Пример
# Границы 100   200
# Датчик  50 101 200 300 403 176  155 981  765  10
# Результат попало 4 числа  101 200 176  155

import random

a=int(input("Введите первую границу отрезка от 0 до 1000"))
b=int(input("Введите вторую границу отрезка от 0 до 1000"))
if a>b:
    a,b=b,a
if (a<0) or (b>1000):
    print("Вы ввели неверные данные")
#print(a,b)
otr=[]
for i in range(a,b+1):
    otr.append(i)
#print(otr)

count=0
gen=[]
while count < 10:
    gen.append(random.randint(0,1000))
    count=count+1
print(gen)
sov=[]
for i in otr:
    if i in gen:
        sov.append(i)
print("Совпавшие числа: ",sov)