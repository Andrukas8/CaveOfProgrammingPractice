animals1 = ["dog", "goat", "sloth", "tiger"]

"""
animals2 = animals1

del animals2[1]

print(animals1)
print(animals2)


animals3 = animals1.copy()
del animals3[1]
print(animals1)
print(animals3)
"""

animals4 = [animal.upper() for animal in animals1]

print(animals4)

lengths = [len(text) for text in animals1]
print(lengths)

numbers1 = [3, 6, 3, 8, 5]
squares = [num ** 2 for num in numbers1]
print(squares)