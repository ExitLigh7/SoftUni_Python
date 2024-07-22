from typing import Iterable


def read_next(*collections: Iterable):
    for collection in collections:
        for el in collection:
            yield el


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
