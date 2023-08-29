import geopandas as gpd
from shapely.geometry import mapping
from fiona.crs import from_epsg

# Read the shapefile
shapefile_path = "path/to/your/shapefile.shp"
gdf = gpd.read_file(shapefile_path)

# Create a buffer of 100 feet
buffer_distance = 100  # in feet
buffered_gdf = gdf.copy()
buffered_gdf['geometry'] = gdf.geometry.buffer(buffer_distance)

# Reproject the buffered GeoDataFrame to a new CRS (Coordinate Reference System)
target_crs = from_epsg(4326)  # WGS 84
reprojected_gdf = buffered_gdf.to_crs(target_crs)

# Print the first few rows of the reprojected GeoDataFrame
print(reprojected_gdf.head())
