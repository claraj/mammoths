import folium
import csv

# Create map. Use terrain tiles instead of roads
mammoth_map = folium.Map(location=[40, -100], zoom_start=3, tiles='Stamen Terrain')

mammoth_lat_lng = []

# Read in mammoth_finds.csv. Use data to create markers, add to map
# CSV structure: name, abundance, abundance unit, latitude, longitude, state, county, comment

with open('mammoth_finds.csv', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    firstline = reader.__next__() # discard title column titles

    for line in reader:
        lat = line[3]
        lon = line[4]
        mammoth_lat_lng.append([lat, lon])

        # Marker text example: Mammoth found in Example County, MN. Comment. 
        marker_text = f'{line[0]} found in {line[6]}, {line[5]}. {line[7]}.' 
        if line[1]:
            marker_text +=  f' {line[1]}, {line[2]} '  # Abundance 

        marker = folium.Marker([lat, lon], popup=marker_text)
        marker.add_to(mammoth_map)

map_filename = 'mammoth_marker_map.html'
mammoth_map.save(map_filename)
print('Map saved to ' + map_filename)


