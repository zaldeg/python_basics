# while True:
#     data = input("Enter some string data (or press 'Enter' for exit): ")
#     if data.strip() == "":
#         break
#     with open("data.txt", "a") as f:
#         f.write(data + "\n")


def make_data():
    data = []
    while True:
        string = input("Enter some string data (or press 'Enter' for exit): ")
        if string.strip() == "":
            break
        data.append(string + "\n")
    return data


full_data = make_data()
with open("data.txt", "w") as f:
    f.writelines(full_data)

