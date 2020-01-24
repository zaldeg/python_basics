summa = 0

while True:
    try:
        new_line = input(
            "Enter your numbers separeted by spaces, 'Q' is special symbol for quit "
        ).split()
        if "Q" not in new_line:
            new_line = map(int, new_line)
            summa += sum(new_line)
        else:
            new_line = new_line[: new_line.index("Q")]
            new_line = map(int, new_line)
            summa += sum(new_line)
            break
    except ValueError:
        print("Pls use only numbers and speciall symbol 'Q'")

print(f"sum is: {summa}")

