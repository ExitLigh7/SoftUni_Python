class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.number:
            raise StopIteration
        output = self.sequence[self.index]
        self.index = (self.index + 1) % len(self.sequence)
        self.count += 1
        return output


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
