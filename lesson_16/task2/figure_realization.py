from PY_homework_hillel.lesson_16.task2.figure import Figure
from PY_homework_hillel.lesson_16.task2.rectangle import Rectangle
from PY_homework_hillel.lesson_16.task2.square import Square
from PY_homework_hillel.lesson_16.task2.triangle import Triangle

square_f: Square = Square(10)

rectangle: Rectangle = Rectangle(10, 5)

triangle: Triangle = Triangle(5, 6, 9, 3)

figure_list: list[Figure] = [square_f, rectangle, triangle]
list_tuple_perimetr_and_square: list[tuple[int, object]] = [(figure.calculate_perimetr(), figure.calculate_square()) for figure in figure_list]

for item in list_tuple_perimetr_and_square:
    print(item[0], item[1])