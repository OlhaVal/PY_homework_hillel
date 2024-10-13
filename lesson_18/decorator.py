def logging_args_and_results(func):
    def wrapper(*args, **kwargs):
        print(f"Аргументи: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper


def exceptions_arise_in_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка при виконанні функції: {e}")
    return wrapper


@logging_args_and_results
@exceptions_arise_in_function
def div(a, b):
    return a / b

div(35, 2)
div(35, 0)