def print_params(a = 1, b = 'строка', c = True):
  print(a, b, c)

print_params()
print_params(45, 'привет', False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [2, 'строка2', True]
values_dict = {'a': 11, 'b': 'строка1', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [22, 'строка22']
print_params(*values_list_2, 42)