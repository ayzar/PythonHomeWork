x = 38
print('Дратути')
if x < 0:
  print('Меньше нуля')
print("дотвидания")
# Примеры
print(' ')
a, b = 10, 5
if a > b:
  print('a > b') 
if a > b and a > 0:
  print('успех')  
if a > b and (a > 0 or b < 1000):
  print('успех')  
if 5 < b and b < 10:
  print('успех')
# Можно сравнивать числа, строки, списки
print(' ')
if '34' > '123':
  print('успех')  
if '123' > '12':
  print('успех')
if [1, 2] > [1,1]:
  print('успех')
# Нельзя сравнивать разные типы
print(' ')
if '6' > 5:
  print('успех')
if [5, 6] > 5:
   print('успех')
# но
if '6' != 5:
  print('успех')
  

