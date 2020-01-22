rating = [7, 5, 3, 3, 2]
print(f"Rating is {rating}")

while True:
    number = input('Enter your number (or "q" for quit): ')
    if number == "q":
        break
    else:
        number = int(number)
    if rating[-1] > number:
        rating.append(number)
    else:
        for i in rating:
            if i < number:
                rating.insert(rating.index(i), number)
                break
    print(rating)

