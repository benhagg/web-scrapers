from geopy.geocoders import Nominatim
import csv

addresses = []
Llatitude = []
Llongitude = []
with open("Dairy plant addy.txt", 'r') as f:
    addresses = f.readlines()
for address in addresses:
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(address)
    if location:
        slatitude = location.latitude
        slongitude = location.longitude
        Llatitude.append(slatitude)
        Llongitude.append(slongitude)
    else:
        Llatitude.append("")
        Llongitude.append("")

with open("-LatLong-.csv", 'w', newline='') as f:
     writer = csv.writer(f)
     writer.writerow(['Address', 'Latitude', 'Longitude'])
     for address, lat, lon in zip(addresses, Llatitude, Llongitude):
         writer.writerow([address, lat, lon])