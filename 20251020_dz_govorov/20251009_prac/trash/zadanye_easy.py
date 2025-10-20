name = input('Добрый день!')

age_input = input('Укажите, сколько Вам лет: ')

age = float(age_input)

if age < 16: 
    print('Вы слишком юны для получения прав')
else:
    print('Вы можете получаться права!')