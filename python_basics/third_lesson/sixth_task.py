def int_func(l):
    """ making first letter capital """
    return l[0].upper() + l[1:]


words = input("Enter some words separated by spaces ").split()
for i in words:
    print(int_func(i), end=" ")
