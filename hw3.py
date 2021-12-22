#ВЫЧИСЛЕНИЕ ПЛОЩАДИ ФИГУРЫ
from math import pi, tan, sqrt

print('Расчет плоащади фигур: \n 1-круг \n 2-правильный многоугольник '
      '\n 3-треугольник \n 4-прямоугольник \n 5-трапеция')
choise = int(input('Выберите № фигуры: '))

if choise < 1 or choise >5:
    print('введите число от 1 до 5')
    choise = int(input('Выберите № фигуры: '))

if choise==1:
    r=float(input('Введите радиус круга: '))
    print('Площадь круга = ', round(pi*(r**2),3))

if choise==2:
    m=float(input('Введите длину стороны: '))
    n = float(input('Введите количество сторон: '))
    print('Площадь пр многоугольника = ', round((n*(m**2))/(4*tan(pi/n)), 3))

if choise == 3:
    a=float(input('Введите длину 1-й стороны: '))
    b = float(input('Введите длину 2-й стороны: '))
    c = float(input('Введите длину 3-й стороны: '))
    p=(a+b+c)/2
    print('Площадь треугольника = ', round(sqrt(p*(p-a)*(p-b)*(p-c)),3))

if choise == 4:
    d = float(input('Введите длину 1-й стороны: '))
    e = float(input('Введите длину 2-й стороны: '))
    print('Площадь прямоугольника = ', round(d*e, 3))

if choise == 5:
    f = float(input('Введите длину основания 1: '))
    g = float(input('Введите длину основания 2: '))
    h = float(input('Введите длину высоты: '))
    print('Площадь трапеции = ', round(((f+g)/2)*h, 3))











