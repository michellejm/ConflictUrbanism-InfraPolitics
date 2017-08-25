## Making Data 

### Making Data 01: Georeferencing a scanned paper map

#### Premise

In this exercise, you will explore some of the georeferencing tools available in QGIS and use them to georeference a 1902 map of the Bronx. You will learn how to use GIS tools to georectify raster datasets.  You will use the georeferenced map for the next exercise where you will digitize vector features from the map infomation. 

#### Notes on the data: 

The map you will be using for this exercise is Mumbai from YEAR (then Bombay). This is a public domain map, so we can use it freely. The wikimedia record for the map can be found [here](https://commons.wikimedia.org/wiki/File:Bombay_1909.jpg). We are using the highest resolution available (RESOLUTION)

You are going to use [OpenStreetMap](https://www.openstreetmap.org/about) (OSM)  as reference data for the georeferencing process.  OSM provides a free, open-source map of the world from public domain and volunteered data.

#### Before you begin
If you haven't already, download the GitHub repository for this course. Using the green button [here](https://github.com/michellejm/ConflictUrbanism-InfraPolitics), select `Download ZIP`. The Data folder will then have all of the datasets needed for tutorials. 

#### Setting up QGIS

Open QGIS:

![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef1.png)

You are going to use OSM data as the reference data for the georeferencing process. You can view the OSM basemap service is QGIS through the OpenLayers plugin.  This plugin does not come pre-installed with QGIS, so you will probably need to add it.  Under the plugins menu, select “Manage and Install Plugins…” 
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef2.png)

The plugins dialog will open.  Search for “Openlayers Plugin.”  Highlight it, and click “Install plugin”:

![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef3.png)

It may take a few seconds to install.  Close the plugins menu when finished.  The OpenLayers tools should now appear under the Web menu: 

![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef4.png)

This plugin will allow you to view a number of basemap services and steam them directly into your QGIS workspace.  Choose the OpenStreetMap>OpenStreetMap option.
Since you are working in a new QGIS project, the map should show the entire earth as the default: 
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef5.png)
Use the zoom in tool ![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef6.png) and zoom into Mumbai, India:
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef07.png)
Now you will access the georeferencing tools and match the scanned map to the OSM map.  

Under the Raster menu, select Georeferencer>Georeferencer:
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef8.png)

The Georeferencer screen will open:
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef9.png)

Click on the Add Raster button ![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef10a.png) and navigate to the JPEG image "Bronx1902Sheet2_Edit.jpg" from the class files in the directory MappingForTheUrbanHumanities-master\Class_Data\2_MakingData.  

It will appear in the georeferencer window:
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef10.png)

This map is from the years just after the 1896 plague, and while the infrastructure (and even some of the land) have changed, we an still navigate our way around using the docks, the bays, and some major roads.

Historical maps can be difficult to georeference, and this sheet poses a number of complications. The map projection is unclear and there are no ground control points or coordinates specified. Because of this, you will georeference by matching physical features represented on the map with their current counterparts (and their known coordinates). However, most of the features in this map have changed or no longer exist (or were never actually built in the first place). Thus, you will need to be very careful to choose locations that you are confident match up well with their contemporary counterparts. Fortunately, some things (such as docks in the East, and some structures have not changes). 

The QGIS georeferencer does not allow you to view both the scanned map and the workspace at the same time, so you will have to inspect both maps in turn and choose carefully to select locations to add georeferencing control points. 
One candidate is the Prince's Dock in Bombay Harbor which continues to exist largely its original configuration.  Use the georeferencer zoom tools ![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef11.png) to zoom to the south-oriented dock: ![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef11.png)
 
Identify as precise a location as possible (a corner of the dock will work nicely) and click on it in the georeferencing window using the add point tool ![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef17.png) When you do so, the Enter map coordinates window appears:
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef14.png)

If you knew the coordinates of this location, you could now add them manually, but since you do not, you must select them from the OSM data in the main QGIS window.  Click on the ![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef15.png) button to see the QGIS workspace.  
You may want to use the QGIS zoom tools to zoom in very closely to the conservatory.
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef12.png)

Once you do so, you will need to reactivate the add button tool ![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef17.png) by maximizing the georeferencing window and clicking the ![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef18.png) button again.  Once you select the same location on the workspace window, you will automatically be brought back to the georeferencing window where the assigned coordinates will be imputed.  
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef19.png)

At this point, if you are dissatisfied, you can move the assigned control points with the move GCP point tool ![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef20.png) or delete it entirely and start over with the delete point tool ![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef21.png) 
If satisfied, click the OK button and the point will be assigned and appear on the map.  Also, a link table entry will be generated on the bottom of the window:
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef22.png)

HERE 

To add a second point, repeat the same process.  It is a good idea to choose another point in a different portion of the map.  A street intersection or corner from the western portion of the map will work well for this as most of those streets continue to exist in the same configuration.  
Here, I have zoomed in to the northwestern most potion of the map where I add a ground control point at the very center of the intersection of Gun Hill Road and Tryon Ave:
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef23.png)

Repeat the same steps as used before to select the center of the same intersection from the OSM map and add the locations to the link table:
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef24.png)

You will need to add a minimum of four points to complete the georeferencing (although more is generally better).  Generate at least two more points of your own choosing and add them to the link table.

Be careful to make sure that the control points you add do in fact match.  This can be quite tricky as many of the features have changed or were not actually built as planned.  

Normally it is a good idea to choose control points from throughout the map.  However, in this case this will be difficult as there are few features in the eastern sections of the map that can be reliably associated with contemporary locations.
In this example, I have selected six control points:
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef25.png)

It is good practice to save the table of control points that you are building.  To do this, choose “Save GCP points as” under the file menu and save it in the .points format in the same location as the image. This will allow you to later recreate the work you have done:

![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef26.png)

Next, you will “transform” the image and create a georeferenced version of the scanned map image. In the georeferencer window, select transformation settings under the settings window:

![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef27.png)

Here you can select the transformation type (Polynomial 1 should be appropriate here), resampling method (Cubic is often used for resampled images and photos), output location and name, and the spatial reference system (here I have selected EPSG:3857, the pseudo Mercator projection used in the OSM data).  You can also opt to have the georeferenced layer added to QGIS when finished: 

![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef28.png)

Close the settings options and click on the start georeferencing button ![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef29.png).

After the transformation finishes, you should see the map appear in the QGIS workspace:
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef30.png)

You can make the scanned map layer partially transparent in the layer properties.  Right click on the map in the layer panel and select properties:
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef31.png)

On the left panel in the properties dialog, select Transparency, here you can adjust the global transparency with a slider: 
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef32.png)

Compare the georeferenced map with the Open Street Map layer.  Make sure that features appear to match up closely:
![blank](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/GeoRef33.png)

In the next exercise you will be using the sheet you georeferenced here and digitizing some of the features from it. 


______________________________________________________________________________________________________________

Tutorial adapted by Michelle McSweeney for *Conflict Urbanism: InfraPolitics*. Originally written by Eric Glass, for *Mapping for the Urban Humanities*.  


