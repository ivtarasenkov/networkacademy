import random
a1=int(input('Введите первое число в диапазоне от 1 до 1000:'))
a2=int(input('Введите второе число в диапазоне от 1 до 1000:'))
a3=int(input('Введите третье число в диапазоне от 1 до 1000:'))
# Генерируется 2 случайных числа от 1 до 100:
b1=(random.randint(1,100))
b2=(random.randint(1,100))
# Определяем какое число больше и присваиваем значения новым переменным для дальнейшего упрощения:
if b1<=b2:
    c1=b1
    c2=b2
else:
    c1=b2
    c2=b1
print('Сгенерированные числа:',c1,c2)
# Перебор вариантов попадания чисел в диапазон:
if c1<=a1<=c2 and c1<=a2<=c2 and c1<=a3<=c2:
    print('Числа',a1,',',a2,'и',a3,'попали в диапазон между',c1,'и',c2)
elif c1<=a2<=c2 and c1<=a3<=c2:
    print('Числа',a2,'и',a3,'попали в диапазон между',c1,'и',c2)
elif c1<=a1<=c2 and c1<=a3<=c2:
    print('Числа',a1,+'и',a3,'попали в диапазон между',c1,'и',c2)
elif c1<=a1<=c2 and c1<=a2<=c2:
    print('Числа',a1,'и',a2,'попали в диапазон между',c1,'и',c2)
elif c1<=a3<=c2:
    print('Число',a3,'попало в диапазон между',c1,'и',c2)
elif c1<=a2<=c2:
    print('Число',a2,'попало в диапазон между',c1,'и',c2)
elif c1<=a1<=c2:
    print('Число',a1,'попало в диапазон между',c1,'и',c2)
else:
    print('Числа не попали в диапазон между',c2,'и',c2)