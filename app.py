import folium
import requests 
import json

def create_map(location=[0, 0], zoom_start=2):
    """Create a base map centered at given coordinates"""
    return folium.Map(location=location, zoom_start=zoom_start)

def add_markers(map_obj, locations):
    """Add a marker to the map for each location"""
    for loc in locations:
        folium.Marker(location=[loc['lat'], loc['lng']],
            popup=loc['name'],
            icon=folium.Icon(color='blue')
        ).add_to(map_obj)
    
    return map_obj

def main():
    # Example locations 
    locations = [
        {'name': 'New York', 'lat': 40.7128, 'lng': -74.0060},
        {'name': 'San Francisco', 'lat': 37.8287, 'lng': -122.3553},
        {'name': 'Tokyo', 'lat': 35.6762, 'lng': 139.6503}
    ]

    # Create the map
    new_map = create_map()
    new_map = add_markers(new_map, locations)

    # Save to HTML file 
    new_map.save('travel_map.html')

if __name__ == "__main__":
    main()