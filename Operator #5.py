a = int(input('Введите число '))
b = [2, 3, 4, 5, 6, 7, 8, 9, 10]
c = []
for i in b:
    if a % i == 0:
        c.append(i)
        pass
if len(c) == 0:
    print('У числа нет делителей среди чисел от 2 до 10')
else:
    print('Делители вашего числа:', c)
