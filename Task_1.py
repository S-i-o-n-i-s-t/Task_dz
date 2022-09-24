# Напишите программу, которая на вход принимает цифру, обозначающую день недели и проверяет, является ли этот день выходным
N = int(input('Введите число обозначающее день недели - '))
if N == 6 or N == 7:
    print('Выходной')
elif N < 1 or N > 7:
    print('Не является днем недели')
else:
    print('Рабочий день')

#     git remote add origin https://github.com/Sionist/Task_dz.git
#  git branch -M main 
# git push -u origin main

