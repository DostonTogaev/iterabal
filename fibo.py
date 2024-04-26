class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit <= 0:
            raise StopIteration
        self.limit -= 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

def fibonacci_generator(limit):
    a, b = 0, 1
    while limit > 0:
        yield a
        a, b = b, a + b
        limit -= 1

print("Iterator:")
fib_iter = FibonacciIterator(20)
for num in fib_iter:
    print(num, end=" ")
print("\n")

print("Generator:")
for num in fibonacci_generator(20):
    print(num, end=" ")
