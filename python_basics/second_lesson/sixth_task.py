goods = []
counter = 1
statistic = {}
while True:
    name = input("Enter name of the product: ")
    price = input("Enter price of the product: ")
    quantity = input("Enter quantity of the product: ")
    unit_of_measure = input("Enter what the product is measured in: ")
    goods.append(
        (
            counter,
            {
                "name": name,
                "price": price,
                "quantity": quantity,
                "unit_of_measure": unit_of_measure,
            },
        )
    )
    counter += 1
    flag = input(
        'If you want to continue write "c" if you want to quit and receive statistic write "q"(default)'
    )
    print(goods)
    if flag == "c":
        continue
    else:
        for tup in goods:
            for d in tup[1]:
                if d in statistic:
                    statistic[d].append(tup[1][d])
                else:
                    statistic[d] = [tup[1][d]]
        break

statistic["unit_of_measure"] = list(set(statistic["unit_of_measure"]))
print(statistic)
