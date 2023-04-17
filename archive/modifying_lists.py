fruits = ["apple", "orange", "strawberry", "banana"]
fruits.append("melon")
fruits.append("grape")

fruits[2] = "blackberry"

print(fruits[1:4])

fruits[1:4] = ["lime"]

print()

for i in range(0,len(fruits)):
    print(fruits[i], i)
