gain = int(input("Enter gain here: "))
expenses = int(input("Enter expenses here: "))
if gain >= expenses:
    print("The firm works with frofit.")
    number_of_employee = int(input("Enter number of employee: "))
    print(f"Profitability of the firm is: {gain / expenses * 100 :.2f}%")
    print(
        f"Gain per person in the firm is: {(gain - expenses) / number_of_employee :.2f}"
    )
else:
    print("The firm works with loss.")
