## Before/After Slider of Mumbai


1. Set up your dependencies.

CSS – In addition to the Leaflet CSS we’re including Bootstrap as well as CSS that will allow us to use Bootstrap glyphicons thanks to Lennard Voogdt and this project.


<link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.css" />
<link rel="stylesheet" href="css/leaflet.awesome-markers.css">

JS - jQuery, jQuery-ui, code that allows users on touch devices to use the map and the code from Graham that creates the map (the map creation function is in jquery.beforeafter-map-0.11.js).


<script type="text/javascript" src="http://code.jquery.com/jquery-2.1.1.min.js"></script>
<script type="text/javascript" src="http://code.jquery.com/ui/1.11.0/jquery-ui.min.js"></script>
<script type="text/javascript" src="js/jquery.ui.touch-punch.min.js"></script> 
<script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
<script type="text/javascript" src="js/jquery.beforeafter-map-0.11.js"></script>

HTML - create an overall div and a div that holds the before and after map instances (note that the ID for these is before and after, respectively).

   <div id="map-container">
        <!-- Make sure to give the map divs height and width 
         I do it with the map class -->
        <div id="before" class="map"></div>
        <div id="after" class="map"></div>
    </div>

2. Create the Leaflet maps

Set up the maps:

    var center = [38.895, -77.020];
        var zoom = 12;
        var before = L.map('before', {
                attributionControl: false,
                inertia: false,
                minZoom: 12
            }).setView(center, zoom);
            
        var after = L.map('after', {
                inertia: false,
                minZoom: 12
            }).setView(center, zoom);

Populate them with layers. In this case I'm using a MapBox TileLayer that we edited a bit:

    L.tileLayer('http://{s}.tiles.mapbox.com/v3/spatial.map-qgihrqg5/{z}/{x}/{y}.png').addTo(before); // 
    L.tileLayer('http://{s}.tiles.mapbox.com/v3/spatial.map-qgihrqg5/{z}/{x}/{y}.png').addTo(after); // 

3. Add features to the map

We will also add some before/after features. Red will be before and blue will be after. Note that if you wanted to simply add a traditional Leaflet marker you would use:

 L.marker([38.895, -77.060]).addTo(before);

but we wanted to use colored markers and Bootstrap glyphicons. Perhaps drink before and relax with music after?

    #BEFORE (red)    
    var circle = L.circle([38.895, -77.020], 2000, {
        color: 'red',
        fillColor: 'red',
        fillOpacity: 0.5
    }).addTo(before);

    L.marker([38.895, -77.060], {icon: L.AwesomeMarkers.icon({icon: 'glass',  prefix: 'glyphicon',markerColor: 'red'}) }).addTo(before);
    L.marker([38.895, -77.050], {icon: L.AwesomeMarkers.icon({icon: 'glass',  prefix: 'glyphicon',markerColor: 'red'}) }).addTo(before);
    L.marker([38.895, -77.040], {icon: L.AwesomeMarkers.icon({icon: 'glass',  prefix: 'glyphicon',markerColor: 'red'}) }).addTo(before);

    #AFTER (blue)
    var circle = L.circle([38.895, -77.020], 2000, {
        color: 'blue',
        fillColor: 'blue',
        fillOpacity: 0.5
    }).addTo(after);

    L.marker([38.905, -77.010], {icon: L.AwesomeMarkers.icon({icon: 'headphones',  prefix: 'glyphicon',markerColor: 'blue'}) }).addTo(after);
    L.marker([38.915, -77.000], {icon: L.AwesomeMarkers.icon({icon: 'headphones',  prefix: 'glyphicon',markerColor: 'blue'}) }).addTo(after);
    L.marker([38.925, -76.990], {icon: L.AwesomeMarkers.icon({icon: 'headphones',  prefix: 'glyphicon',markerColor: 'blue'}) }).addTo(after);

4. Use the beforeAfter function to create the final maps and slider

The beforeAfter function is in the jquery.beforeafter-map-0.11.js file created by Graham MacDonald.

$('#map-container').beforeAfter(before, after);

5. Play with your map