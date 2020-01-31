import json

d = {}
avarage_profit = 0
counter = 0
with open("firms.txt", encoding="utf-8") as f:
    for line in f.readlines():
        tmp = line.split()
        profit = int(tmp[2]) - int(tmp[3])
        d[tmp[0]] = profit
        if profit > 0:
            avarage_profit += profit
            counter += 1
l = [d, {"avarege_profit": avarage_profit / counter}]

with open("firms_stats.json", "w", encoding="utf-8") as f:
    json.dump(l, f, indent=4, ensure_ascii=False)

