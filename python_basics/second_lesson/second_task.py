a = input("Enter your list separated by spaces: ").split()
print(a)
# a = [
#     "hello",
#     1,
#     True,
#     False,
#     [1, "world"],
#     None,
#     0b101001,
#     "a",
#     {1, "g", (1, 8)},
#     {25: "hello", 64: None}
#     ("t", "u", "p", "l", "e"),
# ]
length_a = len(a)
if length_a % 2 != 0:
    length_a -= 1

# for i in range(0, length_a, 2):
#     a[i], a[i + 1] = a[i + 1], a[i]
# solve problem with "range"

counter = 0
while counter < length_a:
    a[counter], a[counter + 1] = a[counter + 1], a[counter]
    counter += 2

print(a)

