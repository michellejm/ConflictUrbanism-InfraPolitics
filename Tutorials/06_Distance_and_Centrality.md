## Distances and Centrality

Through this exercise you will use QGIS to measure distances and calculate the relative centrality of each barrio. After completing these exercises you should be able to…

* Use distance and proximity based measures
* Conduct spatial joins
* Clip data to a boundary
* Explain and calculate a distance matrix
* Explain and calculate centrality


### Proximity measures in Medellín

#### Premise
We are interested in understanding which barrios have the most and the least access to municipal resources.   

#### Research questions:
* Where are the municipal resources concentrated?
* How far away from each resource is each barrio?
* Which barrios are the closest and which are the furthest?

ADVANCED
* Using a representative sample, how much does the travelling distance deviate from the direct distance?


#### Plan
We want to understand how near or far each barrio is to universities, hospitals, public buildings, and other institutions. For each barrio, we would like to calculate a centrality score compared to other barrios.

First we will upload a shape file of Medellín at the barrio level, a shapefile of the buildings, and a shapefil of the roads. We will clip all of the shapefiles to the boundary of Medellín. We will then find the center point for each barrio. Then we will calculate a distance matrix using selected building types. Finally, we will use simple addition to calculate a centrality index for each barrio, and visualize the result.

This could lead to projects of 'betweenness', network analysis, or centrality.

#### Data
The Data and shapefiles for this tutorial are in the [Data Folder for the class](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/tree/master/Data/06_Centrality), which you can download with the Green button again, or with the desktop app.

Medellín
1. MDL at the barrio level
2. MDL buildings
3. MDL roads


#### Setting Up

**Launch** QGIS. 
Set the CSRS to EPSG 21896, Bogota 1975/ Colombia West Zone, this is among the most accurate in terms of preserving shape and distance for this region. When you add EACH LAYER, change the CRS. If it asks, great! Change it then. Otherwise, double click on the layer, select 'General' and 'CRS'

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md1.png)

Select the `add vector data` button and navigate to the  folder and add the following layers: 
1. Barrio_Vereda.shp  (barrio boundaries)
2. medellin_colombia_osm_roads.shp
3. buildings.shp


![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md2.png)

**Save** your map project.

#### Inspect our files

Check the Attribute Table of the Roads file and notice that there are many different types of roads. We may want to think about that later. 

Check the Attribute Table of the buildings file. Notice that not all buildings have a name or a type. We will have to clean that up, too.

Finally, check what information we get about each Barrio, it's not much.

We immediately notice that some of the roads and buildings are outside of the city limits. We will deal with cleaning the buildings file AFTER we clear away what we don't want.

###### Buildings
Vector> Geoprocessing Tools > Clip

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md3.png)

The input vector layer is the buildings file, and the clip layer is the shapes. 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md7.png)

The new buildings file should appear on your map, though you may have to drag it on top of the boundaries file or double check the CRS. This is better, now we are only looking at the buildings we care about. 

You can Remove the old buildings file by right clicking on it and selecting 'Remove'

###### Roads

We will do the same for the roads.

The input vector layer is the roads file, and the clip layer is the shapes. 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md6.png)
 
####
Cleaning buildings

In the Attribute Table of the buildings file, you see that we are missing some information. This is common in datasets downloaded from Open Street Map... We know there is information, but we don't know what it is. To the best of your ability, fill in the missin pieces (i.e., bus station, or 'public_building') when in doubt, use a general term such as 'public building'. We are missing quite a few hospitals and schools, but this will get us started.

 
**Save** your map project.

#### Calculate Distance

Right now, we are looking at many polygons. This is problematic if we want to measure distances because we don't actually know where to measure from. Therefore, we are going to find the centroid of all the polygons. 

We will have to do this twice - once for the barrios and once for the buildings. 

Navigate to Vector > Geometry Tools > Polygon Centroids

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md9.png)

I'm going to start with the Barrio layer and call the new layer 'barrio_centers'

Again, they may be hiding behind another layer and their CRS may be incorrect.

Do the same for the buildings, I'm going to call mine "building_centers"

Now navigate to the 'Distance Matrix' tool in Vector > Analysis > Distance Matrix

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md10.png)

The Input layer is the barrio centers, the target layer is the buildings, and for each, the unique ID field is CODIGO and type

We are using CODIGO rather than 'Name' because some programs have their own encoding system that is not UTF-8, as a result, many characters with accents and other features become corrupted in these programs. The CODIGO column doesn't have any of these features. 

I'm going to call my distance matrix "barrio_buildings_matrix" It will output a csv of distances between each point.

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md11.png) 

Be sure to select 'Standard NxT' to get a matrix of values. 

If we go out and try to open this file, Excel may have a problem with it because of the encoding, so we are going to open it in a text editor such as Sublime or TextWrangler. 

We have a lot of data here. Some of it is irrelevant, indicated by the 'NULL' values. Since we should use data if we don't know what it is, we can't really use this file. Likewise, I was expecting larger numbers since the supposed unit of measurement is in meters. This is a bug in QGIS. I'm really sorry. You can try to change the Project settings to use WGS84, but it is unlikely to stick. We know a trick from the last tutorial that makes this work (1km = approx. .01 degrees). We will have to rely on that. 

But first let's go back to the data. We need to pick something that is both meaningful and that we have data for. We know that educational opportunities are essential for economic growth. We also have data about the location of universities. So let's use only universities as our metric. our metric for centrality is necessarily more narrow, and is a metric of educational centrality. 

Right click on the building_centers layer, and toggle the editing button. Click on 'select features by expression' We will set "type = 'university'  (remember to use single quotes, not double). 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md12.png) 

Now click on the 'building centers' layer again, select 'Save As', save as ESRI shapefile, only selected features, and 'add new layer to the map' I'm going to call mine "university_centers"

Now let's calculate the distance between each barrio and the universities. Return to the Distance Matrix step and do it again this time with our new, University-only layer (Vector > Analysis > Distance matrix), the Standard type, and we want the 'CODIGO' and 'type' fields to be preserved.

I'm going to call mine "university_barrios". It will be saved as a csv file on your computer. 

Add this file back into your project as a delimited text layer. DO NOT OPEN IT IN EXCEL. Excel will strip the leading zeros from your CODIGO column.

Load the csv you just made back into QGIS as a delimited file layer without any geometry.

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md14.png)

**Save** your map project.

#### Join

Now we want to join the distance matrix file to the barrio shape file. 

Double click on the Barrio_Vereda layer and select 'Join'

Join layer: university_barrio
Join field: ID
Target field: CODIGO

Select the 'custom field name prefix' and remove the content (QGIS has a 10 character limit, so keeping this text will remove all the header text from the census file)

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md15.png)

Click 'Apply' and then 'OK'

This join only exists in QGIS, so right click and 'Save As' ESRI Shape File. 
Add the new layer to the map

I'm going to call mine 'barrio_centrality'

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md16.png)


Inspect the Attribute Table of 'barrio centrality'. We still have degrees. Since we are really creating a comparative metric, that might be fine, but I don't like it anyhow, so we will change it to kilometers.

First make a new column to sum the degrees using the Open Field Calculator

We will make a new field, I will call mine 'sumdegrees' (Real decimal number with precision 2) and it will be all of the 'university' fields added together.

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md18.png)

Finally I'll turn the degrees into approximate kilometers, and make another column called 'total' which will be "sumdegrees" * 100

Save your changes by toggling the Editing button off.

**Save** your map project.

#### Making a thematic map representing centrality

Open the Properties menu, select the style, and use 'Graduates Symbols' based on the 'Total' column that you just made. Use the Jenks break, select 'Classify' and 'OK' You should see a map of the most and least isolated barrios in Medellín. 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md19.png)

Toggle off the points, the buildings, and change your roads to grey. 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md20.png)

We see from this that the western side of Medellín is more isolated than the Eastern side. If we were to add features such as mountains and rivers, it may become more apparent as to why this is. 

**Save** your map project.

#### Compare to what is on the ground

****DEPENDING ON YOUR VERSION, THIS MAY NOT WORK FOR YOU****
** YOU DO NOT NEED TO COMPLETE THIS PART TO COMPLETE the TUOTORIAL **

First, remove any layers without a geometry (the distance table)
Then turn OFF 'on the fly' CRS transformations by clicking on the Project CRS in the lower right hand corner, going to 'General' and unclicking 'on the fly'

Another way to analyze distance is along a real road. In QGIS, you can do this manually or computationally. We are going to use the manual approach, for a tutorial on the computational approach, see here. 

We are going to turn the buildings and barrio centroids layers back on because we will be using those to measure from.

We need the Road Graph Plugin for this.

Go to Plugins > Manage and Install Plugins > Road Graph Plugin

You will need to set up this tool. 

Navigate to Vector > Road Graph > Settings 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md21.png)

If we were to calculate the amount of time it takes to get places, we would have to set up the speed limit or average speed on each road or road segment. This is done by creating a column in your Attribute Table that corresponds to speed. In our roads file, all of the roads are classified by the type of road that they are. We could use this to get fairly specific about each road. Note that the customization of this tool happens mostly in your Attribute Table. So, if some roads are One-Way, that is indicated in the Attribute Table, 

We are going to set
Time:  Hours
Distance Unit: Kilometers
Topology tolerance: 3.0000 (this means it will wick up any point we select within 3km to get onto the road. For example, if the 

Layer: mdl_roads
Direction: 'Always use default'
Speed Field: 'Always use default'    km/hr


![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md22.png)

Once you finish making the settings, a Road Graph Box should appear in the left side panel. If it doesn't, go to View > Panels  and turn on the 'Shortest Path'

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md23.png)


Now, we want to compare distances, so I'm going to 'Select by Click' ![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md24'.png) a barrio and a university so that I will be able to find them in the Attribute Table. You have to have the layer name selected in the layers panel for this to work.

Now, pick where you want to start (i.e., one of the outer barrios) using the selector and pick your destination (one of the schools) and open the corresponding attribute to table to find the one that you selected.

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md26.png) 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md25.png) 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/md27.png) 


It looks like this is university_2 since it is the third in the list (they stayed in order, and the numbering started from zero), and barrio CODIGO 5008.

Now draw the line between them with the routing tool. Use the 'Select' crosses to pick your points - we will pick the barrio and the university we identified.

The road paths should calculate this for you automatically. You can save the output and compare it with the distance from our original calculation.


To complete the tutorial on your own, send a pdf of  to Michelle at mam2518@columbia.edu

______________________________________________________________________________________________________________

Tutorial written by Michelle McSweeney, for Conflict Urbanism: InfaPolitics, a seminar taught at Columbia University by the [Center for Spatial Research](http://c4sr.columbia.edu) in Fall 2017.

