with open("data.txt") as f:
    for index, line in enumerate(f.readlines()):
        print(f"in line №{index + 1}: {len(line.split())} words")
    print(f"number of strings is {index + 1}")
