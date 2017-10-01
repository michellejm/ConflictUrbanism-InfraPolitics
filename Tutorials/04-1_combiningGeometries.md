# Tutorial 4 Part 2
**Making 804 KML files into 1 ESRI Shapefile**

Now that we downloaded the KML Files, we need to merge all of the layers into one shapefile in order to use them efficiently. There are a few ways to do this. We will use the [MMQGIS plugin](https://www.google.com/search?q=mmqgis&ie=utf-8&oe=utf-8). You can download this plugin through the Plugin Repository that we used in the last 2 tutorials, located in QGIS at Plugins>Manage and Install Plugins> MMQGIS

### Upload KML files
Select 'Add Vector Layer' ![vector](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/dm1.png) and add all 804 kml files at the same time. It will be very colorful. 

Select 'MMQGIS' - if you installed it, it should be in your toolbar. If it isn't, save your project and reload QGIS. 

From MMQGIS, select Combine > Merge Layers ![merge](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/dm2.png)

A dialog box will appear. From there, select all of your layers (Ctrl+A or click on the first one, scroll to the bottom, and Shift+click on the last one). Select a location (it will fill in a temporary location by default - change this!)
![merge](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/dm3.png)

The new, merged file will appear in your project. It IS NOT permanently saved yet. 
Now, right click on the new layer you made, select 'Save As' and save it as an ESRI Shapefile. 

That's it. You should be able to close this project and open a new one with this new vector layer in it. 
