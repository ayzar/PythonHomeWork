def get_multiplied_digits(number='0'):
  number = int(number)
  str_number = str(number)
  first = int(str_number[0])
  if len(str_number) > 1:
    return first * get_multiplied_digits(int(str_number[1:]))
  else:
    return first

print(get_multiplied_digits(1230))
print(get_multiplied_digits('0123'))