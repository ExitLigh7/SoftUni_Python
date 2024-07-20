def reverse_text(text):
    last_idx = len(text) - 1
    while last_idx >= 0:
        yield text[last_idx]
        last_idx -= 1


for char in reverse_text("step"):
    print(char, end='')
