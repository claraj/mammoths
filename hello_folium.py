""" First folium maps """

import folium

# Center map on downtown Minneapolis, zoom level 15
# Zoom 1 is the whole world, zoom 20 is max zoomed in. 15 is about a neighborhood.
map_mn = folium.Map(location=[44.975, -93.275], zoom_start=15)

# Add a marker for Minneapolis College, at 44.9729,-93.2831
folium.Marker([44.9729, -93.2831], popup='Minneapolis College').add_to(map_mn)

# And save
map_mn.save('hello_map.html')


# Create a new map showing the whole US
map_us = folium.Map(location=[40, -100], zoom_start=3)

map_us.save('us_map.html')



