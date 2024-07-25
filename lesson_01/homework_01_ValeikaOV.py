# task 01 == Виправте синтаксичні помилки
print("Task_1:")
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
print("", "Task_2:", sep="\n")
hello = "Hello"
world = "world"

print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print("", "Task_3:", sep="\n")
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = 4*apples

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
print("", "Task_6:", sep="\n")
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print("Пареметр фігури = ", perimetery)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
print("", "Task_7:", sep="\n")
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_tree = 4
pear_tree = apple_tree + 5
plam_tree = apple_tree - 2
all_tree = apple_tree + pear_tree + plam_tree

print("В саду посадили ", apple_tree, " яблуні, (", apple_tree, "+5)= ",
      pear_tree, " груш, та (", apple_tree, "-2)= ", plam_tree, " сливи.", sep="")
print("Відповідь: Сума всіх дерев дорівнює", all_tree)

# task 08
print("", "Task_8:", sep="\n")
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning = 0 + 5
afternoon = morning - 10
evening = afternoon + 4

print("Температура до обіду була", morning, "градусів,\n після обіду", afternoon,
      "градусів,\n та в ввечорі", evening, "градусів")

print("Відповідь: Надвечір температура дорівнює", evening, "градус")


# task 09
print("", "Task_9:", sep="\n")
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boy = 24
girl = int(boy * 0.5)
absent_student = 1 + 2
all_children_today: int = boy + girl - absent_student

print("В гуртку займаються", boy, "хлопчиків,", girl,
      "дівчат,\n та сьогодні відсутніми були", absent_student, "дітей")

print("Відповідь: В театральному гуртку сьогодні було", all_children_today, "дитини.")

# task 10
print("", "Task_10:", sep="\n")
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1 = float(8)
book_2 = book_1 + 2
book_3 = (book_1+book_2)/2
sum_book = book_1 + book_2 + book_3

print("Вартість першої книги", book_1, "грн,\n другої", book_2, "грн,\n третьої", book_3, "грн.")

print("Відповідь: Всього всі книжки будуть коштувати", sum_book, "грн")

print("test pull request")
