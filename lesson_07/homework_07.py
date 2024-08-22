# task 1
print("Task_1:")
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
print("", "Task_2:", sep="\n")
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(numbers_1: int, numbers_2:int):
    return numbers_1+numbers_2

print(sum_two_numbers(1,2))

# task 3
print("", "Task_3:", sep="\n")
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_average_of_numbers(*args):
    sum_numbers = 0
    for numbers in args:
        sum_numbers = sum_numbers + numbers
    return sum_numbers/len(args)

print(arithmetic_average_of_numbers(5,10,5,50))

# task 4
print("", "Task_4:", sep="\n")
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_text(text: str):
    return text[::-1]

print(reverse_text('приймає рядок та повертає його у зворотному порядку'))

# task 5
print("", "Task_5:", sep="\n")
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
list_word = ["Olga", "Valeyka", "QA"]

def max_word (word_list: list):
    return max(word_list, key=lambda x: len(x))

print(max_word(list_word))

# task 6
print("", "Task_6", sep="\n")
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

print("", "Task_7", sep="\n")
adwentures_of_tom_sawer = ['Tom gave up the brush with reluctance in his face but alacrity in his heart',
                           'And while the late steamer "Big Missouri" worked and sweated in the sun, the retired artist sat on a barrel in the shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents',
                           'There was no lack of material; boys happened along every little while; they came to jeer, but remained to whitewash',
                           'By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour',
                           'And when the middle of the afternoon came, from being a poor poverty, stricken boy in the morning, Tom was literally rolling in wealth.']
find_text = "By the time"

""" Перевірте чи починається якесь речення з "By the time".
"""
def if_any_sentence_begins_with_word (text: list, find_sentence: str):
    """
    Функція перевіряє чи починається якесь речення зі списку з необхідного тексту
    :param text: список речень
    :param find_sentence: початок речення по якому буде пошук
    """
    cout_test = sum([1 for test in text if test.startswith(find_sentence)])
    if cout_test >= 1:
        print("Якесь речення починається з By the time")
    else:
        print("Жодне з речень не починається з By the time")
    return

if_any_sentence_begins_with_word(adwentures_of_tom_sawer,find_text)

print("", "Task_8", sep="\n")
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

def cost_of_books (book_1: float):
    """
    Функція вирішення задачі про книжки:
    Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
    а третя - як половина вартості першої та другої разом.
    :param book_1: вартість першої книжки
    :return: Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
    """
    book_2: float = book_1 + 2
    book_3: float = (book_1 + book_2) / 2
    sum_book: float = book_1 + book_2 + book_3
    return print(f"Вартість першої книги {book_1} грн,\n другої {book_2} грн,\n третьої {book_3} грн.\n "
                 f"Відповідь: Всього всі книжки будуть коштувати {sum_book} грн")

cost_of_books(1)
cost_of_books(11)

print("", "Task_9", sep="\n")
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = [8019, 9907, 2789, 7248, 7128, 19224]
b = (8, 9, 5, 6, 5, 9)


def leftover_from_division (a,b):
    """
    Функція знаходження остачі від ділення
    :param a: перше число
    :param b: друге число
    :return: остача від ділення
    """
    print(f'Остача від ділення {a} на {b} дорівнює {a % b}, '
          f'де {a} - {a // b} * {b} = {a % b}')
    return a % b

print(leftover_from_division(8019,8))

print("", "Task_10", sep="\n")

'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''
number_list = [123, 44, 10, 15, 6, 90]

def sum_of_all_even_numbers (number_list: list):
    """
    Функція суми усіх ПАРНИХ чисел в цьому лісті
    :param number_list: список чисел
    :return: сума усіх ПАРНИХ чисел
    """
    return sum([number for number in number_list if number % 2 == 0])

print(f"Сума усіх парних чисел: {sum_of_all_even_numbers(number_list)}")
