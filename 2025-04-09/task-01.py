#!python

from collections.abc import Iterable


def grouper[T](iterable: Iterable[T], n: int) -> Iterable[tuple[T, ...]]:
    "Collect data into non-overlapping fixed-length chunks or blocks."
    iterators = [iter(iterable)] * n
    return zip(*iterators)


def count(a: int, b: int, c: int = 4, d: str = "Teste") -> None:
    for i in grouper(range(a, b), c):
        for n in i:
            print(n)
        print(d)


count(1, 13, 4, "olá")
