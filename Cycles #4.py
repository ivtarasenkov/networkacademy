# Напишите программу, в которой в бексонечном цикле пользователь вводит два числа, а программа выводит их сумму.

c=0
while c<1:
    a = int(input("введите первое число "))
    b = int(input("введите первое число "))
    print("Сумма чисел равна ",a+b)
    d=input("Завершить ввод (Y/y)?")
    if (d=='Y') or (d=='y'):
        c=1