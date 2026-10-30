age = int(input())
distance = int(input())

standardfare = distance * 5

if age < 12:
    totalfare = standardfare * 0.5
elif age <= 59:
    totalfare = standardfare
else:
    totalfare = standardfare * 0.75

print(int(totalfare)) 

