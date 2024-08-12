class dictionary_iter:

    def __init__(self, dict_object: dict):
        self.dict_tuple = tuple(dict_object.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.dict_tuple):
            idx = self.i
            self.i += 1
            return self.dict_tuple[idx]
        raise StopIteration


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)


