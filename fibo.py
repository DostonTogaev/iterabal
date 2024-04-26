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

print("Iterator:")
fib_iter = FibonacciIterator(20)
for num in fib_iter:
    print(num, end=" ")
