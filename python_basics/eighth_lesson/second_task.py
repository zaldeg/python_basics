class ZerroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


data = list(map(int, (input("Enter some a, b separated by spaces:").split())))

try:
    if data[1] == 0:
        raise ZerroDiv("Zero devision, don't try it at home!!!")
    else:
        print(data[0] / data[1])
except ValueError:
    print("Use numbers!!")
except ZerroDiv as err:
    print(err)
