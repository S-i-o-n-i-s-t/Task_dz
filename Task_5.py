# Напишите программу, колторая принимает на вход координаты 2х точек и находит расстояние между ними в 2д пространстве
print('Введите координаты точки a')
x1 = float(input('xa = '))
y1 = float(input('ya = '))
print('Введите координаты точки b')
x2 = float(input('xb = '))
y2 = float(input('yb = '))
N = ((x1-x2)**2)+((y1-y2)**2)
print(N)
N = N **(0.5)
print(N)