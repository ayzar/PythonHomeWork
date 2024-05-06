def password_(first_number):
  second_number = ""
  for i in range(1, first_number // 2 + 1):
    for j in range(i, first_number):
      if (i != j) and (first_number % (i + j) == a0):
        second_number += str(i) + str(j)
  print("Your password is: ", second_number)

first_number = int(input("Enter your first number: "))
# проверка на корректность вводных данных
while True:
  try:
    while first_number < 3 or first_number > 20:
      first_number = int(input("Введите число в диапазоне от 3 до 20: "))
    break
  except ValueError:
   print('Должно быть число')
# print(first_number)
password_(first_number)