import functools


def mp(a, b):
    return a * b


c = [i for i in range(100, 1001) if i % 2 == 0]

print(functools.reduce(mp, c))

