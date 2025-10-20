# Уточнить какой возраст

s = input('Добрый день! Укажите свой возраст: ')
n = 2025


start = int(s)
now = int(n)

age = now - start

if age < 0:
    print('Данные введены некоректно')
else:
    print(f'Спасибо! Вы {age} года!')
