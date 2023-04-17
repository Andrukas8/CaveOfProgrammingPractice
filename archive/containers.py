import random

people = ["Liam", "Olivia", "Noah", "Ava",
          "James", "Amelia", "William", "Emma"]

skills = ["coding", "art", "testing", "management", "marketing"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def create_people_skills():
    people_skills = dict()

    for person in people:
        skills_local = skills.copy()
        skill_1 = random.choice(skills_local)
        skills_local.remove(skill_1)
        skill_2 = random.choice(skills_local)
        skillset = (skill_1, skill_2)
        people_skills[person] = skillset

    return people_skills


person_index = 0


def choose_person():
    global person_index
    person = people[person_index % len(people)]
    person_index += 1
    return person


def main():
    people_skills = create_people_skills()
    print(people_skills)
    print()

    for i in range(4):
        skills = set()
        for day in days:
            people = [choose_person() for x in range(3)]
            for person in people:
                skills.update(people_skills[person])
            print(day, end=": ")
            print(", ".join(people), end=" -- ")
            print(", ".join(skills))


main()
