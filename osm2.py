from geopy.geocoders import ArcGIS
import os
import folium
import webbrowser
import csv

while True:
    filename = "potholes.txt"
    filepath = "C:/Users/Amine/OneDrive/Bureau/OSM" 
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    nom = ArcGIS()
    where = input('write a place: ')
    cor = nom.geocode(where)
    name = "C:/Users/Amine/OneDrive/Bureau/OSM/MAP.html"
    # Define the coordinates
    latitude = cor.latitude
    longitude = cor.longitude
    print((latitude, longitude))
    location = (f"{where},{latitude},{longitude}")
    #print(location)
    print(os.path.join(filepath, filename))
    with open(os.path.join(filepath, filename), "a") as file:
        file.write(str(location) + "\n")
        file.close()
    with open(os.path.join(filepath, filename), 'r') as pile:
        csv_reader = csv.reader(pile)
        map=folium.Map()

        for row in csv_reader:
            text = (f"{row[0]}\nlatitude:{row[1]}\nlongtitude:{row[2]}")
            
            map.add_child(folium.Marker([row[1],row[2]],text,icon=folium.Icon(color='red')))
            map.save(name)
    webbrowser.open(name)