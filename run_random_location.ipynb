import webbrowser
import random
import geopandas as gpd
from shapely.geometry import Point
import requests
from io import BytesIO
import zipfile

# URL to the shapefile in your GitHub repository
shapefile_url = "https://github.com/rshortd1/random_place_in_the_world/raw/main/ne_10m_land.zip"

def fetch_shapefile(url):
    response = requests.get(url)
    with zipfile.ZipFile(BytesIO(response.content)) as z:
        z.extractall("shapefile")
    return gpd.read_file("shapefile/ne_10m_land.shp")

# Fetch the land shapefile from GitHub
land = fetch_shapefile(shapefile_url)

def random_land_location():
    while True:
        # Generate random coordinates
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        point = Point(longitude, latitude)
        
        # Check if the point is within any land polygon
        if land.contains(point).any():
            url = f"https://www.google.com/maps/@{latitude},{longitude},12z"
            webbrowser.open(url)
            break

if __name__ == "__main__":
    random_land_location()
