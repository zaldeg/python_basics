words = input("Enter your words separated by spaces: ").split()
for number_of_word, word in enumerate(words, 1):
    print(number_of_word, word[:10])

""" solve with "while" and "pop"
counter = 1
while words:
    print(f"{counter} {words.pop(0)[:10]}")
    counter += 1 """
