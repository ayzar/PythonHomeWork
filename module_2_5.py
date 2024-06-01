def get_matrix(n, m, value): # n - кол-во строк, m - кол-во столбцов, value - знач
  matrix = []
  for i in range(n):
    matrix.append([])
    for j in range(m):
      matrix[i].append(value) 
  return matrix
print(get_matrix(3, 4, 5))
print(get_matrix(2, 3, 'cat'))
print(get_matrix(4, 2, [1, 2]))