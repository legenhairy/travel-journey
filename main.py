import folium
import requests 
from dotenv import load_dotenv
from app import create_app

load_dotenv()

app = create_app()

def create_map(locations):
    """Create a base map, then expand by adding the route between each pair of locations"""
    base_map = folium.Map(location=[locations[0]['lat'], locations[0]['lng']], zoom_start=5)

    #Add a marker to the map for each location
    for loc in locations:
        folium.Marker(location=[loc['lat'], loc['lng']],
            popup=loc['name']
        ).add_to(base_map)

    return base_map

def main():
    # Example locations, will eventually ask for user input
    locations = [
        {'name': 'San Francisco', 'lat': 37.7749, 'lng': -122.4194},
        {'name': 'Las Vegas', 'lat': 36.1699, 'lng': -115.1398},
        {'name': 'Denver', 'lat': 39.7420, 'lng': -104.9915}
    ]

    # Create the travel map
    new_map = create_map(locations)

    # Add the line between the locations using Polyline
    # First, iterate over the list of dictionaries and pull out the tuple values
    coords = []
    for i in locations:
        coords.append([i['lat'], i['lng']])

    # Then, use the list of coordinate pairs to create our polyline
    for _ in locations:
        folium.PolyLine(
            locations=coords,
            color="#FF0000",
            weight=3,
            tooltip="From San Francisco to Denver",
        ).add_to(new_map)

    # Save to HTML file 
    new_map.save('travel_map.html')

if __name__ == "__main__":
    app.run(debug=True)