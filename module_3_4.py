def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру для нечувствительного к регистру сравнения
    root_word_lower = root_word.lower()

    # Пустой список для слов, которые удовлетворяют условиям
    same_words = []

    # Перебираем все слова из *other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем, является ли root_word подстрокой слова или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем исходное слово (чтобы сохранить регистр)

    # Возвращаем список найденных слов
    return same_words


# Пример вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты
print(result1)
print(result2)