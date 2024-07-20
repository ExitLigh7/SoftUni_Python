class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = self.step * -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.count > 0:
            self.current += self.step
            self.count -= 1
            return self.current
        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
