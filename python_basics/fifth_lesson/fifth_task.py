from random import randint


def numbers():
    """ return string with 15 random numbers separated by spaces"""
    nums = ""
    for i in range(15):
        nums += f"{randint(0, 100)} "
    return nums


with open("text1.txt", "w") as f:
    f.write(numbers())

with open("text1.txt", "r") as f:
    a = f.readline().split()

print(sum(map(int, a)))
