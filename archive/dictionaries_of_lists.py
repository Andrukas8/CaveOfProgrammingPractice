people = {
    "Al": ["Running", "Programming"],
    "Clare": ["Hiking", "Reading", "Skiing"],
}

print(people["Clare"][1])

for name, hobies in people.items():
    print(name)
    print("======")
    for hobby in hobies:
        print(hobby)