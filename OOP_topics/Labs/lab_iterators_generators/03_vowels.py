class vowels:

    def __init__(self, text: str):
        self.text = text
        self.all_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.vowels_from_string = [el for el in self.text if el.lower() in self.all_vowels]
        self.current_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_idx += 1
        if self.current_idx < len(self.vowels_from_string):
            return self.vowels_from_string[self.current_idx]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


