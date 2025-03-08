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
    "GIScience Education for the Modern Era",
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
    # Display data in an interactive table
    st.dataframe(df, column_config={
        "Package": "📦 Package Name",
        "Description": "📖 Description",
        "Resource Link": "🔗 Documentation"
    })
    st.write("### Copy the links in the table and paste them into a web browser to access official documentation!")

elif menu_option == "View ArcGIS Pro Professional 2025 Study Guide":
    st.markdown("""
    ## ArcGIS Pro Professional 2025 Study Guide

    ### Purpose of the Study
    The ArcGIS Pro Professional study material focuses on applying a broad range of tools and functionality across ArcGIS to advance GIS concepts and knowledge to a project using best practices. It is designed for individuals with at least four years of applied experience in ArcGIS Pro.

    ### Target Audience
    This guide is intended for individuals with a minimum of four years of applied experience in ArcGIS Pro. They should be proficient in best practices and the uses of ArcGIS, demonstrating the ability to apply advanced GIS concepts to design and implement workflows, troubleshoot, and define and complete complex GIS projects. Typical roles may include GIS Specialist, GIS/Geospatial Analyst, Senior GIS Analyst, and GIS Manager.

    ### Candidate Qualifications
    A candidate should be capable of performing the following tasks:
    
    - Apply and interpret fundamental spatial statistics (spatial distribution of the data). (Use the [PySAL](https://pysal.org/) package for spatial statistics)
    - Configure and author advanced visualization techniques for maps and scenes. (Use [matplotlib](https://matplotlib.org/) or [plotly](https://plotly.com/python/) for visualization)
    - Understand and describe how a geolocator works. (Use [geocoder](https://geocoder.readthedocs.io/) for geocoding)
    - Use a network dataset to determine cost. (Use [networkx](https://networkx.github.io/) for network analysis)
    - Implement Python scripting using ArcPy. (ArcPy documentation available [here](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm))
    - Author Arcade expressions. (Arcade expressions are typically written in ArcGIS Pro, no direct Python package but integrated into ArcGIS workflows)
    - Perform advanced vector and raster analysis. (Use [rasterio](https://rasterio.readthedocs.io/en/latest/) for raster data and [shapely](https://shapely.readthedocs.io/en/stable/) for geometric operations)
    - Understand geodatabase design and operate within a multiuser geodatabase. (Use [fiona](https://fiona.readthedocs.io/en/stable/) for reading and writing spatial data formats)
    - Create, update, and delete features and attributes. (Use [geopandas](https://geopandas.org/) for spatial data management and operations)
    - Perform surface modeling and analysis. (Use [scipy](https://scipy.org/) for scientific computing and spatial interpolation)
    - Create and edit ModelBuilder models to automate complex workflows. (Use [arcpy](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm) for geoprocessing automation)
    - Create, manage, and troubleshoot a mosaic dataset. (Use [gdal](https://gdal.org/) for geospatial data processing)
    - Configure the user interface and environment. (No direct Python package for UI configuration, but ArcGIS Pro supports Python scripts and ModelBuilder for automation)
    - Define and determine an appropriate spatial reference system (coordinate reference systems, datums, and projections). (Use [pyproj](https://pyproj4.github.io/pyproj/stable/) for spatial reference system transformations)
    - Author, share, and retrieve items from a portal. (Use [arcgis](https://developers.arcgis.com/python/) for interacting with the ArcGIS API for Python)
    - Use web content or services to perform analyses. (Use [requests](https://docs.python-requests.org/en/latest/) for interacting with REST APIs and [arcgis](https://developers.arcgis.com/python/) for ArcGIS REST API access)
    - Author ArcGIS Pro Tasks. (ArcGIS Pro supports tasks but no direct Python package required)
    - Configure charts and infographics. (Use [matplotlib](https://matplotlib.org/) or [seaborn](https://seaborn.pydata.org/) for data visualization)
    - Configure map layouts and map series. (Use [folium](https://python-visualization.github.io/folium/) for interactive maps or [plotly](https://plotly.com/python/) for advanced GIS data plotting)
    - Configure data schema and attributes. (Use [geopandas](https://geopandas.org/) to manage and configure spatial data schemas)

    ### Skills and Areas of Study

    **1. Data Management (32%)**

    - Design a geodatabase based on project requirements. (Use [geopandas](https://geopandas.org/) for geospatial data management and [fiona](https://fiona.readthedocs.io/en/stable/) for data input/output)
    - Convert and aggregate data as per a given scenario. (Use [pandas](https://pandas.pydata.org/) for data manipulation and aggregation)
    - Implement spatial and attribute data integrity best practices while editing. (Use [shapely](https://shapely.readthedocs.io/en/stable/) for geometric operations and [geopandas](https://geopandas.org/) for data integrity)
    - Configure geodatabase behaviors. (No direct Python package, but ArcGIS Pro scripting via [arcpy](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm) can configure behaviors)
    - Manage coordinate systems and projections. (Use [pyproj](https://pyproj4.github.io/pyproj/stable/) for projections and coordinate systems)

    **2. Mapping and Visualization (20%)**

    - Use advanced cartographic techniques in ArcGIS Pro. (Use [matplotlib](https://matplotlib.org/) or [plotly](https://plotly.com/python/) for creating custom maps)
    - Select the appropriate data visualization technique. (Use [seaborn](https://seaborn.pydata.org/) for statistical visualization or [plotly](https://plotly.com/python/) for interactive visualizations)
    - Configure, author, and optimize visualization products. (Use [matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/) for optimization and design)
    - Ensure ArcGIS Pro is configured for visualization efficiency. (No direct package, but optimizing workflows with [arcpy](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm) will improve efficiency)

    **3. Sharing and Collaboration (17%)**

    - Identify the most effective processes for sharing content. (Use [requests](https://docs.python-requests.org/en/latest/) to handle HTTP requests for sharing)
    - Understand procedures for creating and sharing items. (Use [arcgis](https://developers.arcgis.com/python/) for sharing and managing ArcGIS content)
    - Learn the fundamentals of enabling collaborative workflows. (No direct package for collaboration, but [arcgis](https://developers.arcgis.com/python/) can be used for cloud-based collaboration)

    **4. Analytics (31%)**

    - Understand the use of Python in ArcGIS Pro. (Use [arcpy](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm) for geospatial analysis and automation)
    - Create and edit ModelBuilder models to automate workflows. (Use [arcpy](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm) for ModelBuilder scripting)
    - Learn the workflow, data, tools, settings, and parameters for performing analysis. (Use [scikit-learn](https://scikit-learn.org/stable/) for machine learning workflows and [scipy](https://scipy.org/) for scientific computing)
    - Perform raster data analysis. (Use [rasterio](https://rasterio.readthedocs.io/en/latest/) for raster data processing and analysis)
    - Perform vector data analysis. (Use [shapely](https://shapely.readthedocs.io/en/stable/) for vector analysis)

    By incorporating these Python packages, learners can enhance their ArcGIS Pro proficiency and deepen their understanding of spatial analysis, geospatial data handling, and mapping. For a comprehensive approach, the documentation links provided allow learners to explore each package further.
    """)

# Add additional pages for each How-To Guide
elif menu_option == "Guide to the Geographic Approach":
    st.markdown("""
    ## Guide to the Geographic Approach

    ### Overview
    The Geographic Approach is a framework for solving problems using GIS. It involves five key steps: Ask, Acquire, Examine, Analyze, and Act.

    ### Steps:
    1. **Ask**: Define the problem or question you want to solve.
    2. **Acquire**: Gather the necessary data from reliable sources.
    3. **Examine**: Explore and clean the data.
    4. **Analyze**: Use GIS tools to analyze the data spatially.
    5. **Act**: Present your findings and make informed decisions.

    ### Tools:
    - Use [arcpy](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm) for geoprocessing.
    - Use [geopandas](https://geopandas.org/) for spatial data manipulation.
    """)

elif menu_option == "GIScience Education for the Modern Era":
    st.markdown("""
    ## GIScience Education for the Modern Era

    ### Overview
    GIScience education focuses on teaching the principles and applications of GIS in a modern, technology-driven world.

    ### Key Topics:
    - Core GIS concepts (spatial data, coordinate systems, etc.).
    - Modern tools like cloud-based GIS platforms.
    - Hands-on projects and real-world applications.

    ### Tools:
    - Use [ArcGIS Online](https://www.arcgis.com/index.html) for cloud-based GIS.
    - Use [geopandas](https://geopandas.org/) for spatial data analysis.
    """)

elif menu_option == "Modern GIS":
    st.markdown("""
    ## Modern GIS

    ### Overview
    Modern GIS leverages cloud-based, mobile, and configurable tools to visualize and analyze data.

    ### Key Features:
    - Cloud-based platforms like ArcGIS Online.
    - Mobile GIS apps for field data collection.
    - Configurable tools for custom workflows.

    ### Tools:
    - Use [ArcGIS API for Python](https://developers.arcgis.com/python/) for web GIS.
    - Use [folium](https://python-visualization.github.io/folium/) for interactive maps.
    """)

elif menu_option == "Introduction to Imagery and Remote Sensing":
    st.markdown("""
    ## Introduction to Imagery and Remote Sensing

    ### Overview
    Learn the fundamentals of remote sensing, including how to prepare and render imagery, work with lidar and drone data, and analyze multidimensional and temporal data.

    ### Key Topics:
    - Remote sensing fundamentals.
    - Lidar and drone data processing.
    - Multidimensional and temporal data analysis.

    ### Tools:
    - Use [rasterio](https://rasterio.readthedocs.io/en/latest/) for raster data processing.
    - Use [gdal](https://gdal.org/) for geospatial data formats.
    """)

elif menu_option == "Health GIS":
    st.markdown("""
    ## Health GIS

    ### Overview
    Health GIS applies spatial analysis to public health data to improve decision-making.

    ### Key Topics:
    - Mapping disease outbreaks.
    - Analyzing healthcare access.
    - Visualizing environmental health factors.

    ### Tools:
    - Use [geopandas](https://geopandas.org/) for spatial data management.
    - Use [plotly](https://plotly.com/python/) for interactive health dashboards.
    """)

elif menu_option == "Introduction to Cartography":
    st.markdown("""
    ## Introduction to Cartography

    ### Overview
    Learn about planning, symbolizing, projecting, and presenting both static and interactive thematic maps.

    ### Key Topics:
    - Map design principles.
    - Thematic mapping techniques.
    - Interactive map creation.

    ### Tools:
    - Use [matplotlib](https://matplotlib.org/) for static maps.
    - Use [folium](https://python-visualization.github.io/folium/) for interactive maps.
    """)

elif menu_option == "Official Statistics Modernization GIS":
    st.markdown("""
    ## Official Statistics Modernization GIS

    ### Overview
    Learn how to use GIS for census data collection, monitoring, and dissemination.

    ### Key Topics:
    - Field data collection.
    - Real-time monitoring.
    - Data dissemination.

    ### Tools:
    - Use [arcpy](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm) for census data processing.
    - Use [geopandas](https://geopandas.org/) for spatial data analysis.
    """)

elif menu_option == "SDG Geospatial Learning Lab":
    st.markdown("""
    ## SDG Geospatial Learning Lab

    ### Overview
    Use ArcGIS to analyze and understand the 17 Sustainable Development Goals (SDGs).

    ### Key Topics:
    - SDG data visualization.
    - Geospatial analysis for SDGs.
    - Interactive dashboards.

    ### Tools:
    - Use [ArcGIS API for Python](https://developers.arcgis.com/python/) for SDG analysis.
    - Use [plotly](https://plotly.com/python/) for interactive dashboards.
    """)

elif menu_option == "GIS for Climate Resilience":
    st.markdown("""
    ## GIS for Climate Resilience

    ### Overview
    Use GIS to document climate hazards, assess risks, and develop solutions.

    ### Key Topics:
    - Climate hazard mapping.
    - Risk assessment.
    - Mitigation planning.

    ### Tools:
    - Use [rasterio](https://rasterio.readthedocs.io/en/latest/) for climate data analysis.
    - Use [geopandas](https://geopandas.org/) for spatial risk assessment.
    """)

elif menu_option == "GIS for Collaborative Communities":
    st.markdown("""
    ## GIS for Collaborative Communities

    ### Overview
    Explore hands-on tutorials and resources for applying modern mapping tools in collaborative GIS communities.

    ### Key Topics:
    - Collaborative mapping.
    - Community engagement.
    - Shared workflows.

    ### Tools:
    - Use [ArcGIS Online](https://www.arcgis.com/index.html) for collaborative mapping.
    - Use [folium](https://python-visualization.github.io/folium/) for interactive community maps.
    """)

elif menu_option == "Community Mapping for Racial Equity and Social Justice":
    st.markdown(""
