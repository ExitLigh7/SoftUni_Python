class countdown_iterator:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        i = self.count
        if i >= 0:
            self.count -= 1
            return i
        raise StopIteration

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
