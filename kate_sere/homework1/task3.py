#Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел
a = 5
b = 10
print('arithmetic mean =', (a + b) / 2)

#современный способ через f-string))

print(f'arithmetic mean = {(a + b) / 2}')

#3 — через конкатенацию строк, str() - превращает число в строку

print('arithmetic mean = ' + str((a + b) / 2))

#geometric mean
print('geometric mean =', (a * b)**0.5)