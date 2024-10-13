class ReverseIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = len(my_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.my_list[self.index]


class EvenNumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                result = self.current
                self.current = self.current + 1
                return result
            self.current = self.current + 1
        raise StopIteration


print('Result ReverseIterator:')
reversed_list = ReverseIterator([1, 2, 3, 4, 5, 6, 7, 8])
for item in reversed_list:
    print(item)

print('Result EvenNumberIterator:')
even_iter = EvenNumberIterator(10)
for num in even_iter:
    print(num)
