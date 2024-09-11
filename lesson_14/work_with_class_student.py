from PY_homework_hillel.lesson_14.student import Student

student_1 = Student('Olga',30, 66)
student_2 = Student("Incognito", 99, 100)
student_3 = Student("Superhero", 10, 200)

print(f'For student {student_1.name} with {student_1.age} average score = {student_1.average_score}')

student_1.change_average_score(100)
print(f'After changing ror student {student_1.name} average score = {student_1.average_score}')
