def my_func(a, b, c):
    try:
        l = sorted([a, b, c], reverse=True)
        return l[0] + l[1]
    except:
        print("Pls enter numbers!!!")


e = 3
f = 7
g = "b"
print(my_func(e, f, g))
