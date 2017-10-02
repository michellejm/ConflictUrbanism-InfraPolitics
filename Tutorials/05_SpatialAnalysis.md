## Analyzing Data

Through this exercise you will learn key tools of analysis using QGIS. After completing these exercises you should be able to…

* Use proximity based measures
* Understand the principles and applications of boolean operations
* Conduct spatial joins
* Explain and perform proportional split population estimates
* Create a basic density map (and understand the potential pitfalls of this type of visualization)
* Perform basic raster math operations
* Develop a raster based decision mapping methodology to answer a specific question
* Adapt a raster dataset to your own research needs through raster re-classification

### Proximity measures in Johannesburg

#### Premise
We are interested in understanding who lives in close proximity to the mines, and   

#### Research questions:
* Where are the mines?
* How many people live within a 2 km radius of the mines?
* What are the demographic breakdowns of those people?
* What is their proximity to gated versus informal settlements?

#### Plan
We want to know the demographic breakdown of people who live within 3km of the mines.
First we will upload the shape file of Johannesburg at the sub place level. Then we will add the census data to get a census map of Johannesburg. Then we will add the lat/long of the mines in the area, and create buffers around them. These buffers will represent the sphere of influence of each mine. We will then use a spatial join and proportional split to count the number of people living within 2km of the mine, and determine what the breakdown by race is.

#### Data
Johannesburg
1. JHB Census at the subplace level
2. JHB Subplace Boundaries
3. Mines in South Africa

Background Files (to make our map look nicer)
4. Waterways in South Africa [available here](www.gadm.org)
5. South Africa state borders [available here](http://www.gadm.org/country)

Another good place for South Africa shapefiles is [Mapcruzin](http://www.mapcruzin.com/free-south-africa-arcgis-maps-shapefiles.htm)

Datasets (1) and (2) came from [here](https://census2011.adrianfrith.com/). We downloaded the first one in [Tutorial 4](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/Tutorials/04_WebScraping.md). 
The shape files were downloaded with [this code](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/Data/04_Webscraping/driverKML.py). The kml files were then combined in QGIS using the MMQGIS plugin. Instructions [here](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/Tutorials/04-1_combiningGeometries.md). 

The mines file came from the [Mineral Resources Data System of the USGS](https://mrdata.usgs.gov/mrds/), where you can download the data at the country level. Our data has already been reduced to the state level, but we will need to trim it further. 

#### Setting Up

**Launch** QGIS. 
Set the CSRS to EPSG 2046, Hartebeesthoek94 Lo15, this is among the most accurate in terms of shape/relative size to nearby regions for South Africa. When you add EACH LAYER, change the CRS. If it asks, great! Change it then. Otherwise, double click on the layer, select 'General' and 'CRS'

Select the `add vector data` button and navigate to the  folder and add the following two Layers: 
* jhb_microunit_2011.shp
* jhb_mines.shp

* ZAF_adm2.shp
* ZAF_water_areas_dcw.shp
* ZAF_water_lines_dcw.shp

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/dm1.png)

Then select 'add delimited text layer' ![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb2.png) and add the 'jhb_census.csv' file (no geometry)

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb3.png)

We immediately notice that some of the mines are outside of the city limits.

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb1.png)

We want to get rid of the ones that are not relevant. 

Select Vector > Research Tools > Select by location

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb4.png)

The options are 'Select features in jhb_mines that intersect with features in jhb_microunit_2011'. 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb5.png)

Click 'OK' and close the dialog box. The mines in JHB city limits should appear in yellow. Right click on the mines layer and select 'Save As'.

Save the new file as an ESRI shape file, 'Save only selected features' and 'Add selection to the map' I'm going to call mine 'jhb_city_mines.shp'

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb6.png)

The new mines file should appear on your map, though you may have to drag it on top of the boundaries file. This is better, now we are only looking at the mines we care about. 

You can Remove the old jhb_mines file by right clicking on it and selecting 'Remove'

#### Join

Now we want to join the census file to the shape file. 

Double click on the jhb_micro_census layer and select 'Join'
![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb7.png)

Join layer: jhb_census
Join field: locID
Target field: Name

Select the 'custom field name prefix' and remove the content (QGIS has a 10 character limit, so keeping this text will remove all the header text from the census file)

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb8.png)

Click 'Apply' and then 'OK'

This join only exists in QGIS, so right click and 'Save As' ESRI Shape File. 
Add new layer to the map
I'm going to call mine 'jhb_micro_census'

#### Making a census map

Right now, we have raw numbers, we would prefer percentages of the total number of people in order to have a comparative sense for the areas.

Right click on 'jhb_micro_census', and 'Open Attribute Table'

Click on the Edit button (the little pencil) and then on the 'Add New Column' button. This column is going to be the percent of people identified as 'Black African'. 
![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb9.png)
Since there is a character limit, I'm going to call it 'PBlkAfric', using P to represent percent. Make sure the column is a Decimal type

All this did was add a column. Now, in the formula bar, I select the new column and then the epsilon to create a new formula. The formula builder will appear where you can select field names from the 'Fields' drop down. Enter the formula, 

("Black Afri" / "Total")*100

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb10.png)
Then select 'Update All' to fill the column. Repeat this for 'White', 'Coloured', and 'Indian or Asian'. These categories are deeply problematic in any context. For some readings on the topic, see [Mapping for Architecture Urbanism and the Humanities](https://www.zotero.org/groups/1596423/map_arch_urban_hums/items/collectionKey/MKE43DDN). 

Toggle the Editing button off and Save your changes.

**Save** your map project.

Open the Properties menu, select the style, and use 'Graduate Symbols' based on the 'Percent African Black' column that you just made. Use the Jenks break, select 'Classify' and 'OK' You should see a map of where the most Black Africans live in Johannesburg. 

We can still see the jhb_microunit_2011 file. We'd like to make that a little more uniform, so go to the Properties, Style, and change the fill type to just a border.

#### Proximity Measures

Now we will depart from questions about who lives where and turn our attention to the  relationship between the mines and demographics. Specifically we will ask: 
* How many people live within 3km of the mines, and what are the demographics of those people. 

To answer the first question, we will create a 3km buffer around the mines.

We will be creating a number of new layers during this portion of the exercise so you may want to create a new folder to hold all the buffer layers. I'm going to do that, and call it 'buffers'

##### Creating Buffers
* On your menu bar navigate to `Vector`>`Geoprocessing Tools` > `Buffer(s)`.

  * Choose jhb_city_mines as your input vector layer – this sets which layer the buffers are drawn around. 

  * Set the buffer distance to 2000. Note: the values in this field have the same units as the projection of your input datalayer and map project. Our map is projected in the EPSG 2046, Hartebeesthoek94 Lo15, which uses the WGS84 datum. The measurement is in meters. If you are using QGIS 2.14 or 2.18, there is a bug that causes the *project* datum to revert back to the default (or actually to Clarke 1866). This means that it cannot be measured in meters, and must be measured in degrees. If you were doing this for a final project, you may have to downgrade your software to version 2.8, which is the last version I know of without the bug.
  * To get around this, use .01 degree/km, so for 2km, we will make our input distance .02

  * Save your new shapefile as buffers/2k_mine_buffers.shp  
  
  			![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb11.png)

  * Click `OK`. Then Click `Close`. Your map should look something like the following: 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb12.png)

**Save** your map project

##### Making Estimates 
We would like to determine more generally how many people live near mines in Johannesburg – i.e. how many people are affected by the mines? 

In order to answer this question we will need to estimate the total population near mines. We will first use a coarse method of estimation and then we will refine our estimate using a more advanced technique. 

For our first approximation we will ask: how many people live in the microareas that intersect a 2km buffer around our mines?

* We will use the select by location tool to select all of the microareas that intersect one of our 2km buffers around the miness.

* Navigate to `Vector`>`Research Tools`>`Select by location`. And make the following selections: 

"Select features in 'jhb_micro_census' that interset features in '2kminebuffers'"
Include features that intersect and overlap/cross the input selection

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb13.png)


* Select ‘OK’ and then `Close`. 
* Your selections should look something like this: 
![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb14.png)

* We can already tell that this will be a very coarse way to estimate the population near each of the mines because some micro areas which intersect our buffers are very large and portions of the tract are very far away. 

* Despite this we now want to add up the total population within these selected micro areas.  To determine the total population of all of the microunit tracts that intersect 2km from a mine. To do this we will use the `Basic statistics` tool. Navigate to  `Vector`>`Analysis`>`Basic Statistics`. Select the input layer ('jhb_micro_census' and 'only selected features') and for now, we only want to add the Total column to first determine how many people live in the area. We would need to do this for every column if we wanted the full demographic breakdown. 
Click `OK`. 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb15.png)

To collect these results, you will need to copy & paste them. We will do that for this time just as an example. 

* We see that the total population of all of the micro areas that intersect a 2km buffer around a mine is 861,951.0. Make a note of this total we will compare it to the result we get in the next portion of the exercise. 

##### Proportional Split

Now we will refine our estimate of the population. We will estimate the population that lives precisely within our 2km buffers using using a method called *proportional split estimation*. A proportional split is a way to estimate the proportion of a quantitative attribute that falls within a portion of a polygon’s area. A proportional split is calculated in a few fairly simple steps. 

1. We calculate the area of each polygon unit 
2. Clip the polygons to the boundary of the study area (in our case the 2km buffers)
3. Calculate the area of the polygons after clipping them to the study area
4. Divide the area of the polygons within the study area by their original area to determine the proportion of the original area that falls within the study area
5. Multiply the attributes (for us, population in 2014) we wish to estimate by the proportion in order to estimate the proportion of the attribute that falls within the study area. 
Note: that proportional split estimation assumes that the attribute you are estimating is evenly distributed through out the polygon. In reality the population within each census tract is not evenly distributed nevertheless thus this is an estimate. 


**Calculating the area of the micro areas**
* Open the attribute table for the jhb_micro_census areas layer and select the field calculator – this will turn on editing mode, you are now altering the shapefile (we did this same thing before)

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb16.png)

* Create a new field, assign the Output field name as `Area`, the Output field type as `Decimal number (real)`, the Output field width as `10` and the Precision `2`. Open the Geometry menu and double click on `$area`
* Click `OK`

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb17.png)

* Scroll to the right in the attribute table for the jhb_micro_census and see the new field that you have added. If there are numbers there (not just zeros), select the `Toggle editing mode` button to exit the editing mode. You will be asked if you want to save your changes, say `yes`. 

* Note: the bug may have found you again. If this is the case (and you have all zeros in the Area column), navigate to the 'Project Properties' in 'Project' > 'Project Propoerties'

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb19.png) 

Under General and Select the **SECOND** WGS84

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb20.png)
 
**Clipping the micro areas to the 2km buffers**
* Next we will use the `clip` tool to clip the micro areas with the 2km buffers around the mines. 
* Navigate to `Vector`>`Geoprocessing Tools`>`Clip`
![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb22.png)

* The input vector layer is the layer you will clip (in our case the jhb census micro areas)
* The Clip layer is the layer you will use to clip the input layer (in our case the 2km buffers around the mines). 

* Save the Output shapefile within the buffers folder as `jhb_mine_2kclip`. 
* Click `OK` and then `Close`
* A new layer containing the micro areas clipped to the 2km buffers around the mines was added to your map. 
* Toggle the visibility of all of of the layers on your map off except for `jhb_mine_2kclip`. 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb21.png)


**Calculating the area of the clipped micro areas**
* Now we will calculate the area of these new polygons. 
* Open the attribute table for the clipped micro areas layer: `jhb_mine_2kclip`.
* Open the field calculator and again create a new field to calculate the new area of each polygon. 
* Set the Output field name as `AreaClip`, 
* Select `Decimal number (real)` as the output field type, Set the output field width as 10 and the precision as 2. Under the geometry menu select `$area`. Click `OK`. 
* Notice the new field that has been added to the far right of the attribute table called `AreaClip`
![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb23.png)
**Dividing the the area of the clipped micro areas by their original area**
* Again open the field calculator and calculate a new field. 
* Set the Output field name as `Proportion`, 
* Select `Decimal number (real)` as the output field type, Set the output field width as 10 and the precision as 2.
* Calculate `”AreaClip” / “Area”` -- i.e. the proportion of the original area that remained after the clip
* Click `OK`

**Multiplying the population by the proportion** 

* Now we will calculate one final field where we’ll multiply the attributes (for right now, total population in 2011) we wish to estimate by the proportion in order to estimate the proportion of the attribute that falls within the study area. 
* Set the Output field name as `pop2011_est`
* Select `Decimal number (real)` as the output field type, Set the output field width as 10 and the precision as 2.
* Calculate `"Proportion" * "Total"`
* Click `OK`
* End the edit session and say yes to saving the changes. 

Now we will compare the total estimated population within the buffers to the original rough population estimate we made at the beginning of this exercise using the select by location tool. 

* Navigate to `Vector`>`Analysis`>`Basic Statistics`.
* Select jhb_mine_2kclip as the Input vector layer
* Select pop2011_es as the Target field and note the Sum: 1,643,157.9
* Compare this to our original estimate of 861951.0

We would like to collect all of the demographic information. There's two ways we could do this. First, we could copy and paste every output of 'basic statistics' and save it into a text document and transform it. Or, we could do these staistics in Excel. Excel will prove easier and more intuitive since we've gotten what we need out of QGIS. DO NOT CLOSE your project - we are coming back. 

For now, right click, and 'Save As' csv. Don't add it to your project. We are moving to another program. 

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb26.png)

Download the csv and open it with Excel or Google Sheets. 

In cell AM1, enter a column name, I'm going to use the prefix buf to remind me it's the calculated buffers

In cell AM2, type `=(N2*AK2)`  Column N is 'Black African' and cell 2 is the first one with numbers in it. 
Hover over the bottom right corner to 'drag and fill' this formula for all of your rows.

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/jb27.png)

Repeat for 'Colored', 'Indian or Asian', and 'White'

* Scroll to the bottom of the page to calculate the sum for each group and in cell AM193, type `=SUM(AM2:AM191)`



______________________________________________________________________________________________________________

Tutorial written by Michelle McSweeney, for Conflict Urbanism: InfaPolitics, a seminar taught at Columbia University in Fall 2017. This tutorial is based heavily on one written by Dare Brawley, for *Mapping for the Urban Humanities*. Both were taught by the [Center for Spatial Research](http://c4sr.columbia.edu). 

