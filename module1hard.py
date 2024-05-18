grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Сортировка множества студентов по алфавиту и преобразование его в список
sorted_students = sorted(students)

# Создание словаря, объединение отсортированного списка имен и списка средних оценок
average_grades = dict(zip(
    sorted_students, 
    [sum(grade_list) / len(grade_list) for grade_list in grades]
))

print(average_grades)