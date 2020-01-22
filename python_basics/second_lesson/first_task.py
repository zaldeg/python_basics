l = [
    "hello",
    1,
    True,
    False,
    [1, "world"],
    None,
    0b101001,
    "a",
    {1, "g", (1, 8)},
    {25: "hello", 64: None},
    ("t", "u", "p", "l", "e"),
]

for i in l:
    print(f"{str(i)} have a type: {type(i)}")

