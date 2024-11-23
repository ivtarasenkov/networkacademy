a=int(input('Введите длину коробки'))
b=int(input('Введите высоту коробки'))
c=int(input('Введите глубину коробки'))
x=int(input('Введите длину ящика'))
y=int(input('Введите высоту ящика'))
z=int(input('Введите глубину ящика'))
if a==x and b==y and c==z:
    print('Коробка и ящик одинаковые')
elif a<x and b<y and c<z:
    print('Коробка поместится в ящик')
elif (y<x<b<z and a<x and c<z) or (y<z<b<x and a<x and c<z) or (x<y<b<z and a<x and c<z) or (z<y<b<x and a<x and c<z):
    print('Коробка поместится в ящик')
elif (y<z<c<x and a<x and b<y) or (z<y<c<x and a<x and b<y) or (z<x<c<y and a<x and b<y) or (x<z<c<y and a<x and b<y):
    print('Коробка поместится в ящик')
elif (y<z<a<x and b<y and c<z) or (z<y<a<x and b<y and c<z) or (z<x<a<y and b<y and c<z) or (x<z<a<y and b<y and c<z):
    print('Коробка поместится в ящик')
elif (a>x and b<y and c<z) or (a>x and b<z and c<y) or (a>y and b<x and c<z) or (a>y and b<z and c<x) or (a>z and b<x and c<y) or (a>z and b<y and c<x):
    print('Коробка поместится в ящик')
elif (b>x and a<y and c<z) or (b>x and a<z and c<y) or (b>y and a<x and c<z) or (b>y and a<z and c<x) or (b>z and a<x and c<y) or (b>z and a<y and c<x):
    print('Коробка поместится в ящик')
elif (c>x and a<y and b<z) or (c>x and a<z and b<y) or (c>y and a<x and b<z) or (c>y and a<z and b<x) or (c>z and a<x and b<y) or (c>z and a<y and b<x):
    print('Коробка поместится в ящик')
else:
    print('Коробка не поместится в ящик')
