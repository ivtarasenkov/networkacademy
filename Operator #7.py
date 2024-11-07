pwd = int(input('Введите пароль из трёх цифр: '))
if pwd > 999:
    print("Вы ввели слишком длинный пароль")
a=pwd//100
b=(pwd%100)//10
c=(pwd%100)%10
x=b+c
y=a+b
#x1=x//10
#print(x1)
if (x>y) and ((x//10) < 1):
    sec = x*10+y
    print("Зашифрованный пароль:", sec)
elif (x>y) and ((x//10) >= 1):
    sec = x*100+y
    print("Зашифрованный пароль:", sec)
elif (y>x) and ((y//10) < 1):
    sec = y*10+x
    print("Зашифрованный пароль:", sec)
elif (y>x) and ((y//10) >= 1):
    sec = y*100+x
    print("Зашифрованный пароль:", sec)
elif (x==y) and ((x//10) < 1):
    sec = x*10+y
    print("Зашифрованный пароль:", sec)
elif (x==y) and ((x//10) >= 1):
    sec = x * 100 + y
    print("Зашифрованный пароль:", sec)