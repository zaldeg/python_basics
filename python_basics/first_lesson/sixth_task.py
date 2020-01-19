a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
day = 1
progress = a
while progress <= b:
    progress = progress * 1.1
    day = day + 1
print(f"Sportsman has reached his goal in {day} days!")
