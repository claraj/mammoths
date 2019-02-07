import folium
from folium import plugins
import csv

# Create map. Use terrain tiles instead of roads
mammoth_map = folium.Map(location=[40, -100], zoom_start=3, tiles='Stamen Terrain')

# Read in mammoth_finds.csv. 
with open('mammoth_finds.csv', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    firstline = reader.__next__()    # discard title column titles
    mammoth_lat_lng = [ [ line[3], line[4] ] for line in reader ]   
    
# Generate Heatmap
# Provide list of [lat, lng] coordinates and HeatMap plugin does the rest.
mammoth_map.add_child(plugins.HeatMap(mammoth_lat_lng))

filename = 'mammoth_heatmap.html'
mammoth_map.save(filename)
print('Heatmap saved to ' + filename)




