def read_from_file(name):
    data = []
    with open(name) as f:
        for line in f.readlines():
            data.append(line.split())
    return data


def write_into_file(name, data):
    with open(name, "w") as f:
        for line in data:
            f.writelines(f"{line[0]} {line[1]} {line[2]}\n")


d = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять",
    "Six": "Шесть",
    "Seven": "Семь",
    "Eight": "Восемь",
    "Nine": "Девять",
    "Ten": "Десять",
}


data = read_from_file("numbers.txt")
for i in data:
    i[0] = d[i[0]]
write_into_file("numbers1.txt", data)

