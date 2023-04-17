fruits = ["apple", "orange", "banana"]
animals = ["dog", "cat", "goat"]

for i, item in enumerate(fruits):
    print(i, item)

for fruit, animal in zip(fruits, animals):
    print(fruit, animal)