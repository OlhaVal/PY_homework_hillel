# Task 6.1
'''Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()'''

your_text = input("Введіть свій текст: ")
#your_text: str = "qwertyuiop"
#unic_count: int = 0
#for sumbol in your_text:
#    if your_text.count(sumbol) == 1:
#        unic_count += 1

unic_count = sum([1 for sumbol in your_text if your_text.count(sumbol) == 1])
#print(unic_count)
if unic_count > 10:
    print(f"Унікальних символів в вашому тексті {unic_count} - True")
else:
    print(f"Унікальних символів в вашому тексті {unic_count} - False")

# Task 6.2
'''Напишіть цикл, який буде вимагати від користувача ввести слово, 
в якому є літера "h" (враховуються як великі так і маленькі). 
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".'''

bool_value: bool = False
while not bool_value:
    your_word = input("Введіть слово: ").lower()
    if your_word.find("h") != -1:
        bool_value = True

# Task 6.3
'''Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, 
які присутні в lst1. Данні в лісті можуть бути будь якими'''

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = ([value for value in lst1 if isinstance(value,str)])

#for value in lst1:
#    if isinstance(value, str):
#        lst2.append(value)
print(lst2)

# Task 6.4
'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''
number_list = [123, 44, 10, 15, 6, 90]

sum_even_numbers = sum([number for number in number_list if number % 2 == 0])
print(f"Сума усіх парних чисел: {sum_even_numbers}")
