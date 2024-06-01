def single_root_words(root_word, *other_words):

  root_word_lower = root_word.lower() 
  same_words = []


  for word in other_words:     
      word_lower = word.lower()
      # Проверяем, содержится ли root_word в word или наоборот
      if root_word_lower.count(word_lower) > 0 or word_lower.count(root_word_lower) > 0:
        same_words.append(word)
  return same_words


print(single_root_words("ТРансМИссия", "миссия", "трансмиссия не исправна", "Транс", 
                        "help"))