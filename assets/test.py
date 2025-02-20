import json
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load GeoJSON file
with open('assets/state_data.geojson', 'r') as f:
    geojson_data = json.load(f)

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame.from_features(geojson_data['features'])

# Check summary statistics
summary_stats = gdf['deathPer10K'].describe()
print(summary_stats)

# Display histogram to visualize distribution
plt.figure(figsize=(8,5))
plt.hist(gdf['deathPer10K'].dropna(), bins=20, edgecolor='black')
plt.xlabel("deathPer10K")
plt.ylabel("Frequency")
plt.title("Distribution of deathPer10K")
plt.show()
