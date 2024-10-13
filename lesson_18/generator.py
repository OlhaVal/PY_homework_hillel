
def numbers_generator(N):
    for num in range(0, N + 1, 2):
        yield num


def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b


print('Result numbers_generator:')
for value in numbers_generator(10):
    print(value)

print('Result fibonacci_generator:')
for value in fibonacci_generator(10):
    print(value)
