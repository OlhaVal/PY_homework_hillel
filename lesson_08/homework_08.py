numbers_list: list[str] = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
print(numbers_list)

def sum_number_list(list_of_numbers: list[str]) -> None:
    result: list[int] = list()
    try:
        for item in list_of_numbers:
            chars_list: list = item.split(",")
            result.append(sum(int(integer) for integer in chars_list))
    except ValueError as exception:
        print(f"Неможливо вивести суму для даного випадку: {exception}")
    else:
        print(result)

sum_number_list(numbers_list)
