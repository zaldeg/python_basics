def now_its_digit(string):
    b = ""
    for literal in string:
        b += literal if literal.isdigit() else ""
    return b


d = {}
with open("educational_subjects.txt", encoding="utf-8") as f:
    for line in f.readlines():
        tmp = line.split()
        s = list(map(now_its_digit, tmp))
        summa = 0
        for i in s:
            if i.isdigit():
                summa += int(i)
        d[tmp[0].strip(":")] = summa
print(d)

