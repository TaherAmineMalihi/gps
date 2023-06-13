from geopy.distance import distance

location = float(33.52451), float(-7.64116)
location2 = float(33.52442), float(-7.64066)

km = distance(location, location2)
miles = distance(location, location2).miles

print("Distance between postcodes:")
print(f"{km}")
print(f"{miles} miles")



