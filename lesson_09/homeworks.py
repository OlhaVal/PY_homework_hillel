def leftover_from_division(a,b):
    """
    Функція знаходження остачі від ділення
    :param a: перше число
    :param b: друге число
    :return: остача від ділення
    """
    #print(f'Остача від ділення {a} на {b} дорівнює {a % b}, '
    #      f'де {a} - {a // b} * {b} = {a % b}')
    return a % b

#print(leftover_from_division(8019,0))

def if_any_sentence_begins_with_word (text: list, find_sentence: str):
    """
    Функція перевіряє чи починається якесь речення зі списку з необхідного тексту
    :param text: список речень
    :param find_sentence: початок речення по якому буде пошук
    """
    cout_test = sum([1 for test in text if test.startswith(find_sentence)])
    #if cout_test >= 1:
    #    print("Якесь речення починається з By the time")
    #else:
    #    print("Жодне з речень не починається з By the time")
    return cout_test >= 1

def max_word(word_list: list):
    return max(word_list, key=lambda x: len(x))

word_list = "12345"
print(max_word(word_list))

















def div(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("b is equal 0! Fix it!")
       #return
    return result

def is_ping_db(conut_pings: int) -> bool:
    if 54 > conut_pings >= 5:
        return True
    elif conut_pings >= 55:
        raise TooLargeError("Too fast! Dont use local host")#conut_pings
    else:
        # built-in
        raise ConnectionError("Error db connection")

class TooLargeError(Exception):
    def __init__(self, value) -> None:
        message = f"Value {value} is too large and hard to calculate"
        super().__init__(message)