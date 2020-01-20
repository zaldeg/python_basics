number_of_month = int(input("Enter a number of the month: "))
method = input("Enter method for solve (dict, list - default): ")

if method != "dict":
    print("solving by list")
    l = ["Winter", "Spring", "Summer", "Autumn"]

    if number_of_month == 12:
        number_of_month = 0
    print(f"Your month in {l[number_of_month // 3]}. ")
else:
    print("solving by dictionary")
    d = {0: "Winter", 1: "Spring", 2: "Summer", 3: "Autumn"}

    if number_of_month == 12:
        number_of_month = 0
    print(f"Your month in {d[number_of_month // 3]}.")
