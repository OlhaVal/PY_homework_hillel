from PY_homework_hillel.lesson_22.add_student import add_student_to_course
from PY_homework_hillel.lesson_22.student_data_modul import create_tables
from PY_homework_hillel.lesson_22.work_with_db import get_students_by_course, get_courses_by_student

create_tables()

# Add a student and enroll them in a course
add_student_to_course("Valeyka", "Olga", "Math")
add_student_to_course("Stabrovsky", "Sergiy ", "Python")

# Get students enrolled in a course
get_students_by_course("Python")

# Get courses a student is enrolled in
get_courses_by_student("Valeyka", "Olga")
