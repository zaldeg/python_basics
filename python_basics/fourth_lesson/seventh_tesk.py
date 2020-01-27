def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
        yield s


b = 10

for a in fact(b):
    print(a)
