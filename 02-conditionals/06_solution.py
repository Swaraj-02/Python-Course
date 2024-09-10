#6- Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = int(input('Enter your distance in KM (e.g.- 1,10,33):- '))

if distance < 3:
    transportation = "Walk"
elif distance <= 15:
    transportation = "Bike"   
else:
     transportation = "Car"

print(transportation)