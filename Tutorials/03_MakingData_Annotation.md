## Making Data and Storytelling

### Digitizing Features from a georeferenced map 

### Storytelling

#### Premise

In this exercise, you will explore some of the on-screen hand digitizing tools available in QGIS and use them to digitize houses, hospitals and other features from a georeferenced map.  You will convert raster spatial data into vector based features.

#### Notes on the data: 

The map you will be using for this exercise is the 1909 "Island of Bombay" map that you georeferenced in the previous exercise. If you have not already done so please complete the [Georeferencing](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/Tutorials/02_Georeferencing.md) exercise. 

### Digitizing Exercise

Open QGIS:

![DigitizingExercise](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/Digitize1.png)

Click on the add raster button ![DigitizingExercise](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/Digitize2.png) and navigate to the georeferenced image you made in the [Georeferencing](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/Tutorials/02_Georeferencing.md) exercise.  Since you verified its accuracy already, you will not need any basemap data for this exercise:
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef25.png)

This map is from the years after the plague had subsided and the population of the city was back up to nearly 1 million people (977,822). Every structure, road, and rail line is mapped.  In this exercise, you will create new vector datasets, and hand-digitize some residences, transit stations, and hospitals. You will then annotate the map with significant social and political events leading up to and folliwng the plague. 

The red on this map represents private structures. The black represents public structures. The vast majority of private structures at this time (and presently) are housing, though cotton mills and other factories are also red. One of the first things we notice is the large blocks of red in the southern part of the city and the scattering of small red squares across the city. The large blocks of red mostly represent large tenements whereas the small mostly represent houses. As you may expect from a colonial era, housing in Bombay was highly segregated. Likewise, as an island city, there was (and still is) a severe housing shortage for all but the wealthiest.

As we know, maps reflect who made them. This map was made by the British for the British government. Many informal housing arrangements are not represented on this map. 

After the 1896 plague, many people were forcibly moved to the northern parts of the city. Many of these people were poor, and affordable housing was not available. The Bombay City Improvement Trust was supposed to improve the city overall by building apartments, roads, and sanitation. It fell very short of that goal. However, development was started in Dadar, Matunga, Wadala, and Sion in 1899. These areas surround Dharavi. In 1896, Dharavi had a tannery and a small pottery industry. These industries cause a lot of pollution, the CIT did not invest here. Dharavi today is an informal settlement, built primarily by the people who moved there during the plague and those who moved there looking for work in the century since. Today it is one of the largest and most densely populated slums in the world (it is not the largest in the world, Asia, or even India, it is just in a really visible location). 

In this exercise, we will digitize some of the features in the northern area of Mumbai. Because of time, this dataset will not be comprehensive. 

Remove any transparency from the georeferenced map layer. Zoom into the northern area of the island so you can see Matunga, Wahira, and Dharavi:
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef26.png)

Next you will create a new point layer.  Under the layer menu, choose create new layer and new shapefile layer:
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef27.png)

 In the new vector dialog layer, choose type “Point”.  You can also create additional attribute fields for your dataset, if applicable.  Here, I have added a building “type” attribute and made it a text field with a maximum length of 80.  Select OK:
 
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef28.png)

Save the new file in the same directory with your map, and name it MumbaiBuildings1909.


 The layer will now appear in the Layers panel:
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef29.png)

Now begin editing by depressing the toggle editing tool ![DigitizingExercise](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/Digitize9.png) while the buildings layer is highlighted in the layers panel.  Now you can use the add feature tool ![DigitizingExercise](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/Digitize10.png) to start creating buildings.  Click on one of the buildings in the map.  An attribute dialog appears where you can type in attribute information for the feature you just created:
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef30.png)

There is no information on the map in regards to the type of building; however, the building I clicked on is labeled as a Fort, so I am entering that information now. It is a good idea to enter this information for any objects that you know their identity (forts, hospitals, train stations, etc.). Click OK when finished. 

Continue to digitize buildings in this corner of Bombay:
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef31.png)

If you want to move one of the point features you can use the move feature tool ![DigitizingExercise](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/Digitize13.png) if you want to delete a feature, you can select it with the select features tool ![DigitizingExercise](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/Digitize14.png) at use the delete key on the keyboard.  It is a good idea to regularly use the “save for selected laters” function to save your work as you digitize:  
![DigitizingExercise](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/Digitize15.png)

When finished, depress the toggle editing tool ![DigitizingExercise](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/Digitize16.png) to close the editing session
Next you will digitize the railways.  Create another new shapefile layer as above, but this time choose “Line” as the vector type and MumbaiRailways1909 as the file name:

![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef32.png)

Now when you toggle on editing and select the add features tool ![DigitizingExercise](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/Digitize19.png).  You will be digitizing line features.  As you click with the add features tool you can continue to add as many vertices to the line as you wish.  To complete the line segment, use the right mouse button. 

Line features are more complex than the point features you made earlier and a few more considerations need to be made. One issue regards the shape of the railways (or streets). You are going to digitize the ‘centerline,’ using a single line feature to represent the center of the path feature.  

You also must decide where to begin and end the individual line features.  A common practice is to create individual features between every intersection (or station), ending each feature at the next intersection.  In this way, you can represent the connectivity of the features, essentially modeling a network.  It is important then to make sure that the connecting features are exactly coincident.  You can make sure that you connect features while digitizing by taking advantage of snapping tolerances.  Snapping tools will automatically adjust the digitizing tools and ‘snap’ them to specified features as the cursor gets sufficiently close. 

To set snapping, select “snapping options” under the settings menu: 
![DigitizingExercise](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/Digitize20.png)

Set the snapping options for the current layer to be within 10 map units of a vertex or segment:
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef33.png)

Now the add feature tool will automatically snap to another feature’s vertex whenever the cursor comes within 10 meters.

Digitize the first feature using the add features tool ![DigitizingExercise](https://github.com/CenterForSpatialResearch/MappingForTheUrbanHumanities/blob/master/Tutorials/Images/MakingData01/Digitize22.png). Be careful to keep each vertex as close to the railway as possible.  The more vertices you add the smoother the railroad can be. Right click at the first station. 
![blank](https://github.com/michellejm/mapping_arch_urban_hums/blob/master/Images/georef34.png)

Begin the next feature at the endpoint of the first and continue to digitize the railroads. This method can be used to digitize the roads as well, but because of time constraints, we will stop here for this tutorial. If you want or need to digitize the southern section of Bombay, you will need to use the polygon tool to represent the blocks that are filled in, which functions similarly to the points and lines. 


______________________________________________________________________________________________________________

Tutorial written by Michelle McSweeney for *Conflict Urbanism: InfraPolitics* a seminar course taught at Columbia University in Fall 2017 by the Center for Spatial Research[http://c4sr.columbia.edu/, adapted from a tutorial written by Eric Glass, for *Mapping for the Urban Humanities*.

