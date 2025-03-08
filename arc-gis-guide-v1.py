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

# Sidebar for navigation
sidebar = st.sidebar
sidebar.title("Navigation")
menu_option = sidebar.radio("Select a page", [
    "Home", 
    "View ArcGIS Pro Professional 2025 Study Guide",
    "Guide to the Geographic Approach",
    "GIScience education for the modern era",
    "Modern GIS",
    "Introduction to Imagery and Remote Sensing",
    "Health GIS",
    "Introduction to Cartography",
    "Official Statistics Modernization GIS",
    "SDG Geospatial Learning Lab",
    "GIS for Climate Resilience",
    "GIS for Collaborative Communities",
    "Community Mapping for Racial Equity and Social Justice"
])

# Display the selected page
if menu_option == "Home":
    st.write("### GIS Packages List")
    st.dataframe(df, column_config={
        "Package": "📦 Package Name",
        "Description": "📖 Description",
        "Resource Link": "🔗 Documentation"
    })
    st.write("### Click on the links in the table to access official documentation!")

elif menu_option == "View ArcGIS Pro Professional 2025 Study Guide":
    st.markdown("""
    ## ArcGIS Pro Professional 2025 Study Guide
    ...
    """)  # The content for this page remains the same

elif menu_option == "Guide to the Geographic Approach":
    st.markdown("""
    ## Guide to the Geographic Approach
    Explore the geographic approach to problem-solving and its impact on GIS analysis. This method emphasizes understanding problems in their spatial context and applying GIS tools effectively to solve real-world challenges.
    """)

elif menu_option == "GIScience education for the modern era":
    st.markdown("""
    ## GIScience Education for the Modern Era
    GIScience education is evolving to meet the demands of modern technology. This curriculum emphasizes hands-on learning and adaptation to new tools and workflows in GIS technology.
    """)

elif menu_option == "Modern GIS":
    st.markdown("""
    ## Modern GIS
    Discover how GIS technology has adapted to a mobile, cloud-based, interconnected, and configurable world. This course explores how GIS solutions can be leveraged for data visualization and analysis, enabling better, data-driven decision-making.
    """)

elif menu_option == "Introduction to Imagery and Remote Sensing":
    st.markdown("""
    ## Introduction to Imagery and Remote Sensing
    Understand remote sensing fundamentals, learn to prepare and render imagery, work with lidar and drone data, analyze multidimensional and temporal data, extract information from remotely sensed data, and more.
    """)

elif menu_option == "Health GIS":
    st.markdown("""
    ## Health GIS
    This guide is for health professionals to connect maps, apps, data, and people to make more informed health decisions. It provides exercises and tutorials to develop expertise in GIS for health-related applications.
    """)

elif menu_option == "Introduction to Cartography":
    st.markdown("""
    ## Introduction to Cartography
    Learn about planning, symbolizing, projecting, and presenting both static and interactive thematic maps, providing an in-depth understanding of cartography in modern GIS workflows.
    """)

elif menu_option == "Official Statistics Modernization GIS":
    st.markdown("""
    ## Official Statistics Modernization GIS
    These tutorials teach you how to plan your work, conduct field data collection, monitor your operations, and disseminate authoritative data, all using ArcGIS tools for official statistics modernization.
    """)

elif menu_option == "SDG Geospatial Learning Lab":
    st.markdown("""
    ## SDG Geospatial Learning Lab
    Learn how ArcGIS tools can change the way you analyze and understand the 17 Sustainable Development Goals (SDGs), with applications for both new and experienced GIS users.
    """)

elif menu_option == "GIS for Climate Resilience":
    st.markdown("""
    ## GIS for Climate Resilience
    This curriculum helps you document climate hazards, identify risks, and come up with solutions using GIS to improve climate resilience for people and places.
    """)

elif menu_option == "GIS for Collaborative Communities":
    st.markdown("""
    ## GIS for Collaborative Communities
    Explore resources for applying modern GIS tools in collaborative workflows and building strong communities using GIS for social good.
    """)

elif menu_option == "Community Mapping for Racial Equity and Social Justice":
    st.markdown("""
    ## Community Mapping for Racial Equity and Social Justice
    A tutorial collection designed to equip young mappers with essential ArcGIS skills while applying a social justice framework to their local community mapping.
    """)

