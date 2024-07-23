class WordsFinder:
  def __init__(self, *file_names):
      self.file_names = file_names

  def get_all_words(self):
      all_words = {}
      # Список символов пунктуации, которые мы будем удалять
      punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
      for file_name in self.file_names:
          with open(file_name, 'r') as file:
              text = file.read().lower()  # Приводим текст к нижнему регистру
              # Удаляем пунктуацию
              for char in punctuation:
                  text = text.replace(char, '')
              words = text.split()
              all_words[file_name] = words
      return all_words

  def find(self, word):
      word = word.lower()
      all_words = self.get_all_words()
      result = {}
      for file_name, words in all_words.items():
          if word in words:
              result[file_name] = words.index(word)
      return result

  def count(self, word):
      word = word.lower()
      all_words = self.get_all_words()
      result = {}
      for file_name, words in all_words.items():
          result[file_name] = words.count(word)
      return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
