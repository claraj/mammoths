import folium
import csv

mammoth_colors = {
    'Mammuthus columbi': 'green',
    'Mammuthus primigenius': 'blue',
    'Mammuthus hayi': 'purple',
    'Mammuthus exilis': 'red',
    'Mammuthus': 'orange'
    }

# Create map. Use terrain tiles instead of roads
mammoth_map = folium.Map(location=[40, -100], zoom_start=3, tiles='Stamen Terrain')

mammoth_lat_lng = []

# Read in mammoth_finds.csv. Use data to create markers, add to map
with open('mammoth_finds.csv', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    firstline = reader.__next__() # discard title column titles
    for line in reader:
        lat = line[3]
        lon = line[4]
        mammoth_lat_lng.append([lat, lon])
        marker_text = '%s found in %s, %s. %s.' % (line[0] , line[6] , line[5] , line[7])
        if line[1]:
            marker_text += ' %s %s ' % (line[1], line[2])

        color = mammoth_colors.get(line[0])  # Get color from dictionary

        marker = folium.Marker([lat, lon], popup=marker_text, icon=folium.Icon(color=color))
        marker.add_to(mammoth_map)


filename = 'mammoth_color_marker_map.html'
mammoth_map.save(filename)
print('Map saved to ' + filename)


