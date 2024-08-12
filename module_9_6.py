def all_variants(text):
  length = len(text)
  for start in range(length):  # Перебор всех возможных начальных позиций
      for end in range(start + 1, length + 1):  # Перебор всех возможных длин подпоследовательностей
          yield text[start:end]  # Возвращаем подпоследовательность

a = all_variants("abc")
for i in a:
  print(i)