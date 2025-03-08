import streamlit as st
import pandas as pd

# List of GIS packages with descriptions and links
packages = [
    ("arcpy", "Core ArcGIS geoprocessing package.", "https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm"),
    ("arcgis", "ArcGIS API for Python (Web GIS).", "https://developers.arcgis.com/python/"),
    ("pyproj", "Coordinate reference system transformations.", "https://pyproj4.github.io/pyproj/stable/"),
    ("shapely", "Geometric operations like buffering and intersections.", "https://shapely.readthedocs.io/en/stable/"),
    ("fiona", "Reads/writes spatial data formats.", "https://fiona.readthedocs.io/en/stable/"),
    ("geopandas", "Extends pandas for spatial data.", "https://geopandas.org/"),
    ("rasterio", "Raster data processing and analysis.", "https://rasterio.readthedocs.io/en/latest/"),
    ("gdal", "Reads and writes geospatial data formats.", "https://gdal.org/"),
    ("pandas", "Data manipulation and analysis.", "https://pandas.pydata.org/"),
    ("numpy", "Numerical operations for raster and spatial data.", "https://numpy.org/"),
    ("matplotlib", "Basic plotting for geospatial visualization.", "https://matplotlib.org/"),
    ("seaborn", "Statistical visualization, useful for trends.", "https://seaborn.pydata.org/"),
    ("folium", "Creates interactive maps.", "https://python-visualization.github.io/folium/"),
    ("plotly", "Advanced interactive GIS data plotting.", "https://plotly.com/python/"),
    ("scipy", "Scientific computing, including spatial interpolation.", "https://scipy.org/"),
    ("scikit-learn", "Machine learning for GIS analysis.", "https://scikit-learn.org/stable/"),
    ("XGBoost", "Optimized machine learning algorithms.", "https://xgboost.readthedocs.io/en/stable/"),
    ("PySAL", "Spatial statistics and analysis.", "https://pysal.org/"),
    ("requests", "HTTP requests (ArcGIS REST API, etc.).", "https://docs.python-requests.org/en/latest/"),
    ("geocoder", "Geocoding and reverse geocoding.", "https://geocoder.readthedocs.io/"),
]

# Convert to DataFrame
df = pd.DataFrame(packages, columns=["Package", "Description", "Resource Link"])

# Streamlit App
st.title("📍 ArcGIS Python Packages Guide")
st.write("This application provides a list of useful Python packages for ArcGIS programming, including descriptions and resource links.")

# Display data in an interactive table
st.dataframe(df, column_config={
    "Package": "📦 Package Name",
    "Description": "📖 Description",
    "Resource Link": "🔗 Documentation"
})

st.write("### Click on the links in the table to access official documentation!")
