is_raining = True
is_windy = False
stay_inside = is_raining and is_windy
str(stay_inside)
print(stay_inside)

take_coat = is_raining or is_windy
print(str(take_coat))

take_umbrella = is_raining and not is_windy
print("Take umbrella " + str(take_umbrella))