print(1/1)  # падает с ошибкой
result = 0
znam = int(input('Введите число, я найду обратное:'))
try:
    result = 1 / znam
except ZeroDivisionError:
    result = None
if result:
    print('Обратное равно ', result)