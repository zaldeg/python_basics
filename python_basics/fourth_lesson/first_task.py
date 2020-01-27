from sys import argv

try:
    _, time_h, salary_h, bonus = argv

    print(f"Your salary is: {int(time_h) * int(salary_h) + int(bonus)}")
except ValueError:
    print("Not enough params, or your are trying to write words!")
