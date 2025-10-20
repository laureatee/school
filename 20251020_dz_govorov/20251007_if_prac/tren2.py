# Выяснить расстояние и время до дачи 
a = input('Введить расстояние до дачи')
b = input('Введить за сколько нужно доехать до дачи')

distance = int(a)
time = int(b)
speed = distance / time

if speed < 60:
    print('Вам нужно ехать со скоростью :', speed,'км/ч')
else: # speed > 60
    print('Вам придется ехать превышая скорость :', speed, 'км/ч')