## Webmaps

This tutorial is formatted a little differently from the others. You will pick one of three projects to work on and work in groups of 1-3. 

The city/project combination are designed around the maps we have already made. Unlike the GIS tutorials, this is not a step-by-step process, but rather, an opportunity to take what you've learned in the tutorials and use it to make a webmap. Regardless which city you are researching, you may wish to pick your project based on the map you plan to make rather than the city it is centered on.

### Outcomes

1. Mumbai: Add a timeline slider to your map using Leaflet timeline plugin

2. Johannesburg: Multiple census layers on a leaflet map using Leaflet layers control plugin

3. Medellín: Show distance metrics using the Route360 plugin 



* Using the geojson we exported from [Tutorial 3](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/Tutorials/03_Annotation.md), you will make a map with a timeline slider that makes popups appear in a sequence. 

* Using QGIS, you will export the census data we joined to the microunit layer and the mines in Johannesburg both as geojsons. You will then style these layers and add them as layers in Leaflet. 

* Using the API for the Route360 plugin, you will make a map illustrating how far someone can get walking or driving in Medellín. 

### Set Up (For ALL Projects)

You must have a text editor installed such as [Sublime Text](https://www.sublimetext.com/)

Create a new HTML document. I'm going to call mine `mymap.html`. Set up your directory (folder) structure. I'm going to put all of these folders and the mymap.html file in a folder called 'mymap'.

* `css`
* `data`
* `img`
* mymap.html
* `js`

Set up a local server.

**PLUGIN for ALL COMPUTERS INSTRUCTIONS**

If running a local server from the command line has not worked for you before, please install [this Web Server plugin](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb?hl=en) on Google Chrome. This plugin will allow you to view your page as if you were viewing it on the Internet. You MUST use Google Chrome to view your webmap. You will also use Google Chrome for the HTML Tutorial.

When you launch the new app, you will be prompted to select a folder. Choose your mymap folder. Make a note of the address for your local server, in my case below, it is http://127.0.0.1:8887/

![add](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/wp1.png)

The mymap.html file should appear as a selection. Select that and you will have a blank screen.

**ADVANCED for MAC INSTRUCTIONS**

First you need to make sure you have Python installed. Check if you have Python installed and which version it is. We will be using Python to run a local server.

### (Mac) Check which Python version you have (if any)

1. Open a Terminal Window 
2. Type `$ python -V` hit 'Return'
4. Make a note of which Python version you have, you will need it later.

	![img](https://github.com/CenterForSpatialResearch/NYCDHWeek/blob/master/Images/pythontest.png)
	* if Python is installed make note of which version you have installed, you will need it later

### (Mac) Set up a local server

We will run a local server from our computers. The details of this are far beyond this tutorial, for more on  the technical details, visit the [Mozilla Developer site](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Set_up_a_basic_working_environment). For more on how the web works the difference between a local and remote server, [read this](https://devdojo.com/blog/technology/local-vs-remote-servers).

1. In a Terminal window, navigate to the folder where you have saved your html file (directions below on how to "navigate"). In my case it is in Documents > MappingForTheUrbanHumanities_2017 > Class_Data >3_Webmaps. To navigate there, I type the following commands (don't type the $, that just indicates that you are in the Terminal):

	* `$ cd Desktop`
	* `$ cd CUIP` 
	* `$ cd webmap`
	* `$ cd mymap`
	
2. If you have Python 3, type:

	* `$  python -m http.server`  
	
2. If you have Python 2, type:

	* `$ python -m SimpleHTTPServer`
	
3. Return to your browser window (Chrome, Firefox, or Safari) and type `localhost` in the navigation bar. The mymap.html file should appear as a selection. Select that and you will have a blank screen.


## Set up the HTML document.

Open the 'mymap.html' document in a text editor such as Sublime (recommended), Text Wranger, TextEdit, Notepad or similar (do NOT use MS Word or similar)

Set up the structure of your document. For more discussion, revisit [Tutorial 3 on Annotation with Leaflet](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/Tutorials/03_Annotation.md)

```
<!DOCTYPE html>
<html>
<head>
.
.
.

</head>

<body>
.
.
.
</body>
</html>

```

All projects will need three basic scripts to get started. 

Load the basic scripts you will need.
1. *Download basic libraries.* We have already done this step for you. But for reference we downloaded the Leaflet.js library from [here](http://leafletjs.com/download.html). And we downloaded the jQuery library from [here](http://jquery.com/download/).  

2. *Name your map.* The `<title>` tag contains the name of your map that will appear at the top of the browser window.

3. *Import Leaflet's CSS.* Leaflet comes with its own CSS styles that specify how certain elements, like the zoom buttons, should look. We have placed this css file in the `css` folder and now need to tell our index.html document where to find it.
	`<link rel="stylesheet"  href="css/leaflet.css"/>`
	
4. *Import Javascript libraries.* Now we need to import the Leaflet and jQuery javascript libraries. We have likewise saved these in the `js` folder in our webmaps directory. 
	`<script src="js/leaflet.js"></script>`
	`<script src="js/jquery-3.2.1.min.js">  </script>`
	
5. *Set the size of your map.* Using CSS syntax we will set the size of the map to fill a full browser window: 
	`<style> #map{position: absolute; top:0; bottom:0; left:0; width: 100%;} </style>`
	
6. *Close the <header> tag.*


```
<html>
<head>
	<title> MY_MAP_TITLE </title>
	
	\\CSS Files
	<link rel="stylesheet"  href="css/leaflet.css"/> 
	
	\\ Javascript files
	<script src="js/leaflet.js"></script>
	<script src="js/jquery-3.2.1.min.js">  </script>

	<style>
	#map{position:absolute; top:0; bottom:0; left:0; width: 100%;}
	</style>


</head>

```

Here we diverge. Please go to your tutorial:


1. Map of Historical Mumbai with a timeline slider so popups indicating events appear as the slider is moved, and an image slider so the user can slide between 1909 Bombay and 2017 Mumbai.

2. Census and Mines map of Johannesburg where users can toggle the census layers.

3. Distance map of Medellín where users can move a point and see how far they could get in a car in 10, 20, and 30 minutes.




To complete this tutorial, submit your working FOLDER
______________________________________________________________________________________________________________

Tutorial written by Michelle McSweeney, for Conflict Urbanism: InfaPolitics, a seminar taught at Columbia University by the [Center for Spatial Research](http://c4sr.columbia.edu) in Fall 2017.

