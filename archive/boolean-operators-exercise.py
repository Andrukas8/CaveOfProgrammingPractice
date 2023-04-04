student = input("Are you a student? (y/n) : ")
pets = input("Do you have pets? (y/n) : ")
smokes = input("Do you smoke? (y/n) :")

is_student = student == "y"
has_pets = pets == "y"
does_smoke = smokes == "y"

student_can_rent = is_student and not has_pets and not does_smoke
non_student_can_rent = not is_student and not (does_smoke and has_pets)

can_rent = student_can_rent or non_student_can_rent

print(can_rent)