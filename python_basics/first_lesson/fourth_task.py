number = int(input("Enter positive natural number "))
biggest_digit = 0
while number:
    temp = number % 10
    number = number // 10
    if temp > biggest_digit:
        biggest_digit = temp
    if biggest_digit == 9:
        print(f"Biggest digit in the number is: {biggest_digit}")
        break
if biggest_digit < 9:
    print(f"Biggest digit in the number is: {biggest_digit}")
