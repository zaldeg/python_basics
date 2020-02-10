class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


result = []

while True:
    number = input("Enter number or 'Stop' for results: ")
    if number == "Stop":
        break
    try:
        if number.isdigit():
            result.append(int(number))
        else:
            raise NotNumber("This is not a number!!!")
    except NotNumber as err:
        print(err)

print(result)
