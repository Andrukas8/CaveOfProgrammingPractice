# The Fridge
temp = float(input("Get temperature: "))

STATUS_COLD = "Fridge too cold"
STATUS_OK = "Fridge OK"
STATUS_WARM = "Fridge too warm"
STATUS_BROKEN = "Fridge broken"

status = STATUS_BROKEN

if temp <= 0:
    status = STATUS_COLD
elif temp <= 4:
    status = STATUS_OK
elif temp <= 6:
    status = STATUS_WARM
else:
    status = STATUS_BROKEN

print(status)

