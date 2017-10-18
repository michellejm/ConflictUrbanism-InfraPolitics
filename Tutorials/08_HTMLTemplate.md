##Tutorial 5: Setting Up A Conflict Urbanism: Language Justice Case Study

This tutorial is required for all students in Conflict Urbanism: Language Justice. It introduces the format you will be working with and explains the template we expect you to use. Through editing the pre-made template, you will develop familiarity with HTML and CSS. These two languages drive both the structure and formatting of webpages. 

If you are already familiar with HTML and CSS, you may skip ahead to working directly with the template provided. You are requested *not* to change the style settings, so that everyone's project retains a similar aesthetic.

This tutorial is primarily an introduction to using the template we have provided. Whereas other tutorials in this series are more hands-on and technical, this one is really designed to get you up and running with the template you will use. 

By the end of this tutorial, you will be able to:
* Set up a Case Study for your project
* Edit an HTML template to add your own content
* Manually create links and embed objects into a website
* Utilize Elements, Tags, and Attributes to add functionality and navigation to a site.
* Navigate Selectors, Properties, and Values to add style to a site. 

## Set Up
For this tutorial, you will need:
* [Sublime](http://www.sublimetext.com/)
* [Chrome](https://www.google.com/chrome/)
* Case_Study Files, Download [here](https://drive.google.com/open?id=0B8IdSWLrkSd3WHNIN05fZlNJMk0) Or view the files [here](https://github.com/michellejm/ConflictUrbanism_LanguageJustice/tree/master/CaseStudy)


### Introduction to HTML/CSS

The following section is adapted from [here](http://learn.shayhowe.com/html-css/building-your-first-web-page/) and provides a good understanding of Web Basics. Please refer to it for more information. Likewise, if you are interested in diving deeper, work through the following (7 hour) [course](https://www.codecademy.com/learn/web), on Code Academy. 

A **Website** uses at least two languages:

**HTML**, *HyperText Markup Language*, gives content structure and meaning by defining content as headings, paragraphs, or images. 

**CSS**, *Cascading Style Sheets*, is used to style the appearance of content, using fonts, colors, etc.
</br>

*Below are web basics. Feel free to skip to Case Study*

### Three Common *HTML* terms:

*Elements*
Elements are designators that define the structure and content of objects within a page. Some of the more frequently used elements include multiple levels of `headings` (identified as `<h1>` through `<h6>`) and `paragraphs` (identified as `<p>`); the list goes on to include the `<a>`, `<div>`, `<span>`, `<strong>`, and `<em>`, and many more.

Elements are identified by the use of less-than and greater-than angle brackets, `< >`, surrounding the element name. Thus, an element looks like the following:

```html
<a>
```

*Tags*

The use of less-than and greater-than angle brackets surrounding an element creates a `tag`. Tags most commonly occur in pairs of opening and closing tags.

An `opening tag` marks the beginning of an element. It consists of a less-than sign followed by an element’s name, and then ends with a greater-than sign; for example, `<div>`.

A `closing tag` marks the end of an element. It consists of a less-than sign followed by a forward slash and the element’s name, and then ends with a greater-than sign; for example, `</div>`.

The `content` that falls between the opening and closing tags is the content of that element. An `anchor` link, for example, will have an opening tag of `<a>` and a closing tag of `</a>`. What falls between these two tags will be the content of the anchor link.

So, anchor tags will look a bit like this:

```html
<a> ... </a>
```

*Attributes*

Attributes are properties used to provide additional information about an element. The most common attributes include:
*	`id` : identifies an element
*	`class` : classifies an element
*	`src` : specifies a source for embeddable content
*	`href` : provides a hyperlink reference to a linked resthece

Attributes are defined within the opening tag after an element’s name. Generally, attributes include a name and a value. The format for these attributes consists of the attribute name followed by an equals sign and then a quoted attribute value. For example, an `<a> `element including an href attribute would look like the following:

So, anchor tags will look a bit like this:

```html
<a href="http://www.google.com/">Google</a>
```

### Setting Up an HTML Document:

**HTML** documents are *plain text* documents saved with an .html file extension rather than a .txt file extension. To write HTML, you need a plain text editor that you are comfortable using. We will use *Sublime Text* You may use *TextWrangler*, *NotePad*, *TextEdit*, etc. Do *NOT* use Microsoft Word or Pages ([read more about Plain Text versus Rich Text Formats](http://programminghistorian.org/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown)).

All HTML documents have a required structure that includes the following declaration and elements: `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>`.

The document type declaration, or `<!DOCTYPE html>`, informs web browsers which version of HTML is being used and is placed at the beginning of the HTML document. Because we are using the latest version of HTML, the document type declaration is simply `<!DOCTYPE html>`. Following the document type declaration, the <html> element signifies the beginning of the document.

Inside the `<html>` element, the `<head>` element identifies the top of the document, including any metadata (accompanying information about the page). The content inside the `<head>` element is not displayed on the web page itself. Instead, it may include the document title (which is displayed on the title bar in the browser window), links to any external files, or any other beneficial metadata.

All of the visible content within the web page will fall within the `<body>` element. A breakdown of a typical HTML document structure looks like this:


```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a web page.</p>
  </body>
</html>
```

```css
body,
p {
  margin: 0;
}
h1 {
  margin-top: 0;
}
```

The preceding code shows the document beginning with the document type declaration, `<!DOCTYPE html>`, followed directly by the `<html>` element. Inside the `<html>` element come the `<head>` and `<body>` elements. The `<head>` element includes the character encoding of the page via the `<meta charset="utf-8">` tag and the title of the document via the `<title>` element. The `<body>` element includes a heading via the `<h1>` element and a paragraph via the `<p>` element. Because both the heading and paragraph are nested within the <body> element, they are visible on the web page.

When an element is placed inside of another element, also known as nested, it is best practice to indent that element to keep the document structure well organized and legible. In the previous code, both the `<head>` and `<body>` elements were nested—and indented—inside the `<html>` element. The pattern of indenting for elements continues as new elements are added inside the `<head>` and `<body>` elements.


### Three Common *CSS* terms:

*Selectors:*

As elements are added to a web page, they are styled using CSS. A selector designates exactly which element or elements within the HTML to target and apply styles (such as color, size, and position) to. Selectors may include a combination of different qualifiers to select unique elements. For example, you may need to select every paragraph on a page, or  only one specific paragraph. Selectors generally target an attribute value, such as an id or class value, or target the type of element, such as `<h1>` or `<p>`.

Selectors are followed with curly brackets, `{}`, which surround the styles to be applied to the selected element. The selector here is targeting all `<p>` elements.

```css
p {
  margin: 0;
}
```

*Properties:*

Properties determine the style that will be applied to an element. Property names fall after a selector, within the curly brackets, `{}`, and immediately preceding a colon, `:`. There are numerous properties available, such as background, color, font-size, height, and width, etc. In the following code the color and font-size properties are applied to all `<p>` elements.

```css
p {
  color: ...;
  font-size: ...;
}
```

*Values*

Values determine the behavior of a property. Values can be identified as the text between the colon, `:`, and semicolon, ;. Here we are selecting all `<p>` elements and setting the value of the color property to be orange and the value of the font-size property to be 16 pixels.

```css
p {
  color: orange;
  font-size: 16px;
}
```

To review, in CSS the rule set begins with the selector, which is immediately followed by curly brackets. Within these curly brackets are declarations consisting of property and value pairs. Each declaration begins with a property, which is followed by a colon, the property value, and finally a semicolon.

It is a common practice to indent property and value pairs within the curly brackets. As with HTML, these indentations help keep the code organized and legible.


### Working with Selectors:

Selectors, as previously mentioned, indicate which HTML elements are being styled. Since selectors indicate the relationship between HTML and CSS, it is important to fully understand their functionality. There are three types of selectors: `type`, `class`, and `ID `.


*Type Selectors:*

Type selectors target elements by their element type. For example, if you want to target all division elements, `<div>`,  use a div type selector. The following code shows a type selector for division elements and the HTML it selects.

```css
div { ... }
```

```html
<div>...</div>          
<div>...</div>
```

*Class Selectors:*

Class selectors allow us to select an element based on the element’s class attribute value. Class selectors are more specific than type selectors. They select a particular group of elements rather than all elements of one type.

Class selectors allow us to apply the same styles to different elements at once by using the same class attribute value across multiple elements.

Within CSS, classes are denoted by a leading period, `.`, followed by the class attribute value. Here the class selector will select any element containing the class attribute value of awesome, including both division and paragraph elements.

```css
.awesome { ... }
```

```html
<div class="awesome">...</div>
<p class="awesome">...</p>
```

*ID Selectors:*

ID selectors are more precise than class selectors. They target one unique element at a time. Just as class selectors use an element’s class attribute value as the selector, ID selectors use an element’s id attribute value as a selector.

Regardless of which type of element they appear on, id attribute values can only be used once per page. If used they should be reserved for significant elements.

Within CSS, ID selectors are denoted by a leading hash sign, `#`, followed by the id attribute value. Here the ID selector will only select the element containing the id attribute value of sunshine.

```css
#sunshine { ... }
```

```html
<div id="sunshine">...</div>
```

Selectors are extremely powerful, and the selectors outlined here are the most common. These selectors are also only the beginning. Many more advanced selectors exist and are readily available.

### Referencing **CSS**:

To get the HTML file to read from the CSS file, reference the CSS file within the HTML file. The best practice for referencing the CSS file is to include all of the styles in a single external style sheet. This style sheet is referenced in the `<head>` element of the HTML document. Using a single external style sheet maintains the same style across an entire website and quickly make changes sitewide.

To create the external CSS file, use Sublime to create a new plain text file with a .css file extension. The CSS file *MUST* be saved within the same folder (or a subfolder) where the HTML file is located.

Within the `<head>` element of the HTML document, the `<link>` element is used to define the relationship between the HTML file and the CSS file. The rel attribute indicates that this line references a style sheet. The href (or hyperlink reference) attribute is used to identify the location, or path, of the CSS file.

Consider the following example of an HTML document `<head>` element that references a single external style sheet.

```html
<head>
  <link rel="stylesheet" href="main.css">
</head>
```

In order for the CSS to render correctly, the path of the href attribute value must indicate to where the CSS file is saved. In the preceding example, the main.css file is stored within the same location as the HTML file, also known as the root directory.

If the CSS file is within a subdirectory or subfolder, the href attribute value needs to reflect this. For example, if the main.css file were stored within a subdirectory named stylesheets, the href attribute value would be stylesheets/main.css, using a forward slash to indicate a subdirectory.

### Commenting Code:

HTML comments start with `<!-- and end with -->`. 
CSS comments start with `/*` and end with `*/`.
Note: If you would like to learn more, please follow further tutorials [here](http://learn.shayhowe.com/html-css/getting-to-know-html/).



## Setting Up a Case Study

For this part, we will walk through a case study. By the end of this tutorial, you will have created a case study you can use for your project. You can always edit your work as your project develops. 

![Add Layer](https://github.com/michellejm/ConflictUrbanism_LanguageJustice/blob/master/Images/casestudy.png)
 
1. Create a folder on your computer for this project. Everything you want to be displayed on your site MUST be kept in this folder (i.e., text, images, reports, etc.). 
	1. You can use the Case_Study.zip folder. This folder has the `.html` and `.css` files already in it. 
2. Open the `.html` and `'.css` files with sublime. (To specify which program is used to open a file, right click (or Command+click) on the file and select the program from 'Open With')
3. Also open the `.html` file in Chrome. (If Chrome is your default browser, you can double click on the file and it will open in Chrome)
	1. Chrome has developer tools that are useful for inspecting the code on your site.
	2. Go to  `View > Developer > Developer Tools` to open the `console` that shows you different parts of your site. If there is an error, you will be able to see it here.

![Tools](https://github.com/michellejm/ConflictUrbanism_LanguageJustice/blob/master/Images/developer.png)

The code for the Case Study is pasted below. This is the same as the template.html file you downloaded in the Case Study Folder. 

Every step is commented. More detailed comments follow this code block. You can follow the instructions in the code or go to the end if you want a more high-level introduction. Everytime you change the code in Sublime, `Save`. `Refresh` the web page and you should be able to see the changes. Note: Do not make any changes to the .css files. 

```html
<!-- Conflict Urbanism: Language Justice
     Center for Spatial Research
     Michelle McSweeney (mam2518@columbia.edu)

================================================================= -->
<!DOCTYPE html>
<html lang="en">

  <head>
  <!--Do not change: Main title as appears in window -->
  <title> Conflict Urbanism: Language Justice</title>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <!--Add: Project Keyword Description & Student Name  -->
  <meta name="description" content="">
  <meta name= "author" content="">
    
  <!--Do not change: boostrap -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

  <!--Do not change: css files required for case study -->
  <link href='css/conflict_main.css' rel='stylesheet' />
  <link href='css/conflict_cthese.css' rel='stylesheet' />
  
  <style>
  body {
    font-family: Arial, sans;
  }
  </style>
  </head>

<body>

  <div class="container main">
    <div class="row top-row">
      <div class="col-md-12">

        <!--Do not change these : Title  -->
        <h5><a href="index.html">Conflict Urbanism: Language Justice</a></h5>

        <!--Add: Case Study Title -->
        <h5>Case Study | Type Title Here </h5>

        <!--Add: Image Header: File Size: 1800x450.png. 
        Save your file as 'Header_image_1800x450.png in the <img> folder
        Use Illustrator Template in folder, if you require size setup-->
        <div class="img-padding">
          <img src="img/Header_image_1800x450.png" class="img-responsive" />
        </div>

      </div>
    </div>

<!--Note: We suggest dividing your case study ito many different components. Think of this as chapters of your paper. 
In this example, we have 7 sections. Below we set up a list for adding to the menu on left. 
You could use chapter 1, chapter 2 or give text titles. --> 

<div class="row">
  <div class="col-md-3 scrollspy">
    <div id="sticky-menu ">
      <ul id="nav" class="nav c4sr-nav" data-spy="affix">
        <!-- <li><a href="#section_id"><img src="img/dot-1.png" />Chapter_Name</a></li>-->
        <li><a href="#Text1"><img src="img/dot-1.png" />Introduction</a></li>
        <li><a href="#Text2"><img src="img/dot-1.png" />Text with Annotation</a></li>
        <li><a href="#Text3"><img src="img/dot-1.png" />Text with PDF</a></li>
        <li><a href="#Text4"><img src="img/dot-1.png" />Text with Image</a></li>
        <li><a href="#Text5"><img src="img/dot-1.png" />Text with Video</a></li>
        <li><a href="#Text6"><img src="img/dot-1.png" />Text with Interactive</a></li>
        <li><a href="#Text7"><img src="img/dot-1.png" />Text with Map</a><li>
      </ul>
    </div>
  </div>

<!--Note: You can start with the first few paragraphs and keep adding. Each <item> above has a referenced paragraph below. 
You can think of the above being a table of contents and below being the chapters, with actual text. 
If you add a chapter, go back to the Table of Contents and add a tab for it. --> 

  <!-- main -->
  <div class="col-md-6 body-text">

<!--Add: Text Paragraph -->
     <!-- <h5 id="section_id">Section Title</h5> -->
     <h5 id="Text1">Introduction to the cthese</h5>
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. <br/><br/>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. <br/><br/>

<!--Add: Text Paragraph with Annotation. 

We have designed annotations, so that they are responsive to where you are on the case study. 
These appear on the right column next to the footnote. To add a footnote, insert the following line of code. 
Please change numbers in order. Everytime, you add a footnote, you will be required to go to the footnote section of the code, 
to add in the text and link.

To add a footnote, insert: <div class="footnote footnote-1">1</div> 
Starting from #1, change as you proceed-->

    <h5 id="Text2">Text with Annotation</h5>
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. <div class="footnote footnote-1">1</div> Add Text: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.<div class="footnote footnote-2">2</div> It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. <br/><br/>

<!--Add: Text Paragraph with PDF report. 
To add a link to a PDF, save the file in the same folder and update link text 
Insert the following code: <a href='filename.pdf'>Download Report</a> -->
    <h5 id="Text3">Text with PDF</h5><br/>
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</br>
<a href='sample_report.pdf'>Download Report</a><br/><br/>

<!--Add: Text Paragraph with Image. 
To add an Image, save the file in the <img> folder 
Insert the following code: <img src="img/filename.png" class="img-responsive"/> -->
    <h5 id="Text4">Text with Image</h5><br/>
<img src="img/Sample_Image.png" class="img-responsive"/><br/>
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. <br/><br/>

<!--Add: Text Paragraph with Video. 
To add a Video, either upload to vimeo or use Youtube link 
Insert the following code: 
<div class="embed-responsive embed-responsive-4by3">
  <<iframe class="embed-responsive-item" src="weblink_of_video"></iframe>
</div>
-->
<h5 id="Text5">Text with Video</h5><br/>
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. <br/></br>
<!-- Example: Vimeo -->
<div class="embed-responsive embed-responsive-4by3">
  <<iframe class="embed-responsive-item" src="https://player.vimeo.com/video/152612971"></iframe>
</div>
</br>

<!--Add: Text with Interactive. 
As part of the project, you might design an interactive website. If you would like to include that in the case study, 
the easiest way might be linking that to an image. We suggest this as oppose to integrating them into your case study. 
Interactives might be heavier files and be difficult to load, instantly. Below, there are 3 examples.
-->

<h5 id="Text6">Text with Interactive</h5><br/>
<a href="Interactive.html" target='_blank' ><img src="img/Sample_Image_Interactive.png" class="img-responsive"/></a>

<br/>
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.<br/><br/> 

<iframe width='100%' height='500px' frameBorder='0' src='interactive.html'></iframe>

<br/><br/> 
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.<br/><br/> 

<iframe width='100%' height='500px' frameBorder='0' src= "http://c4sr.columbia.edu/conflict-urbanism-aleppo/index.html" name="iframe_x"></iframe> 
<p><a href="http://c4sr.columbia.edu/conflict-urbanism-aleppo/index.html" target="iframe_x">Language Justice Site</a></p>

<br/>

<!--Add: Text with Interactive Map. 
You can bring any project from mapbox editor, using the iframe method. 
In tutorial 4, we go over Mapbox basics, to make such an interactive map in mapbox editor.

Note: You can bring in any project, with the above code as long as you have your mapbox API key and map id
-->

<h5 id="Text7">Text with Map</h5><br/>
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.<br/><br/>
</br>

<!-- Copy iframe tab from Carto  -->
</br>
You can bring any project from Carto using the Embed (iFrame) method Just copy and paste the code from the Publish >> Embed option. 


Following is an example of the code that you copy/paste from Carto editor: 
<iframe width="100%" height="520" frameborder="0" src="https://michellejm.carto.com/viz/f07c01f8-85b7-11e6-96f9-0e05a8b3e3d7/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>
</br>

<!--Add: your name and description as follows -->
</br>
<hr>
your Name: <br/><br/>Description (Program, Year, Expertise)
<hr>
<br/><br/>
</div>

<!-- Add: footnotes with definitions
This is the code:
<div class="footnote-ref footnote-ref-1"><sup>1</sup>Title <a href= "www.c4sr.columbia.edu"> “Descriptive text”</a> Date </div> 
-->
<div class="col-md-3">
  <div class="footnotes">
    <div class="footnote-ref footnote-ref-1"><sup>1</sup>Title <a href= "www.c4sr.columbia.edu"> “Descriptive text”</a> Date </div>
    <div class="footnote-ref footnote-ref-2"><sup>2</sup>Test2 <a href= "www.c4sr.columbia.edu"> “Description ”</a> Date </div>
  </div>
</div>
</div>

<!-- Do not change -->        
  <div class="row red bottom-line">
    <div class="col-sm-12">
      <h5><center> Center for Spatial Research, Columbia University</center></h5>
    </div>
  </div>

</div>

<!-- Do not change -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" crossorigin="anonymous"></script>
    
<!-- Do not change !!! -->
<script>
$(document).ready(function() {

  // bootstrap affix menu
  $('#nav').affix({
    offset: {
      top: $('#nav').offset().top
    }
  });

  // footnote logic
  $('.footnote').each(function() {
    var f = $(this).attr('class').split(" ")[1];
    var num = f.split("-")[1];
    var top = $('.' + f).position().top;
    var num_c = num - 1;
    var offset = num_c * 32;
    var top_n = top - offset;
    
    // align footnote to position
    $('.footnote-ref-' + num).css({
      top: top_n
    });

    var final_p = $('.footnote-ref-' + num).position().top;
  });

  if ($("ul.c4sr-nav").css("display") == "none" ){
        $('.footnote-ref').each(function() {
          $(this).css({
            'top': 0,
            'margin-bottom': '10px'});
        });
  }

});
</script>

</body>
</html>
```

### Code Explained

* Add Title
```html
<!--Add: Case Study Title -->
<h5>Case Study | Type Title Here </h5>
```

*  Add Header Image
Save your file as 'Header_image_1800x450.png in the <img> folder. Use the Illustrator Template in the Case Studies folder, if you require size setup.
```html
<div class="img-padding">
<img src="img/Header_image_1800x450.png" class="img-responsive" />
</div>
```
* Add Chapter Titles
Add structure to your case study by dividing it into components, akin to chapters or sections in a paper. In this example, we have 7 sections. Below is a list for adding to the menu on the left. These titles are linked to positions in the text using the href attribute (href="#Text1" refers to id="Text1" in the remainder of the template)
```html
<div class="row">
  <div class="col-md-3 scrollspy">
    <div id="sticky-menu ">
      <ul id="nav" class="nav c4sr-nav" data-spy="affix">
        <!-- <li><a href="#section_id"><img src="img/dot-1.png" />Chapter_Name</a></li>-->
        <li><a href="#Text1"><img src="img/dot-1.png" />Introduction</a></li>
        <li><a href="#Text2"><img src="img/dot-1.png" />Text with Annotation</a></li>
        <li><a href="#Text3"><img src="img/dot-1.png" />Text with PDF</a></li>
        <li><a href="#Text4"><img src="img/dot-1.png" />Text with Image</a></li>
        <li><a href="#Text5"><img src="img/dot-1.png" />Text with Video</a></li>
        <li><a href="#Text6"><img src="img/dot-1.png" />Text with Interactive</a></li>
        <li><a href="#Text7"><img src="img/dot-1.png" />Text with Map</a><li>
      </ul>
    </div>
  </div>
```

* Add Chapter Text
Add text paragraphs for each chapter. The title of your chapter can be different (longer) than the one you use for the Table of Contents. 
```html
     <!-- <h5 id="section_id">Section Title</h5> -->
     <h5 id="Text1">Introduction to the course</h5>
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. <br/><br/>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. <br/><br/>
```

* Add Text with Annotations
We have designed annotations so that they are responsive to where you are on the case study. These appear on the right column next to the footnote. To add a footnote, insert the following line of code. Please change numbers in order. Everytime, you add a footnote, you will be required to go to the footnote section of the code, to add in the text and link. To add a footnote, insert the following code next to where you want the foot note. Start from #1, and change as you proceed.
```html
<div class="footnote footnote-1">1</div> 
```
Here's how it looks in the paragraph:
```
<h5 id="Text2">Text with Annotation</h5>
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. <div class="footnote footnote-1">1</div> Add Text: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.<div class="footnote footnote-2">2</div> It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. <br/><br/>
```
Then add details to `Footnotes Section` at *end* of the code. 
```html
<div class="col-md-3">
  <div class="footnotes">
    <div class="footnote-ref footnote-ref-1"><sup>1</sup>Title <a href= "www.c4sr.columbia.edu"> “Descriptive text”</a> Date </div>
    <div class="footnote-ref footnote-ref-2"><sup>2</sup>Test2 <a href= "www.c4sr.columbia.edu"> “Description ”</a> Date </div>
  </div>
</div>
</div>
```

* Add PDFs

To add a link to a PDF, save the file in the same folder and update link text. Insert the following code: 
```html
<a href='sample_report.pdf'>Download Report</a><br/><br/>
```

* Add Images

To add an Image, save the file in the <img> folder. Insert the following code:
```html
<img src="img/Sample_Image.png" class="img-responsive"/><br/>
```
* Add Video

To add a Video, either upload to vimeo or use Youtube link. Insert the following code: 
```html
<div class="embed-responsive embed-responsive-4by3">
  <<iframe class="embed-responsive-item" src="https://player.vimeo.com/video/152612971"></iframe>
</div>
```
* Add Interactive Features

If you would like to include interactive features in the case study, the easiest way might be linking your built object to an image. We suggest this as oppose to integrating them into your case study. Interactives might be heavier files and be difficult to load, instantly. Below, there are 3 examples.

1. Linking Image to an Interactive html:
```html 
<a href="filename.html"><img src="img/filename_interactive.png" class="img-responsive"/></a>
```

2. Embedding an Interactive html

```html
<iframe width='100%' height='500px' frameBorder='0' src='interactive.html'></iframe>
```

3. Embedding an entire website (test this!)

```html
<iframe width='100%' height='500px' frameBorder='0' src= "http://c4sr.columbia.edu/conflict-urbanism-aleppo/index.html" name="iframe_x"></iframe> 
<p><a href="http://c4sr.columbia.edu/conflict-urbanism-aleppo/index.html" target="iframe_x">Aleppo Site</a></p>
```
* Add a Map
<br>You can bring any project from carto, using the embed method. In Tutorial 3, we go over how to use Carto to embed maps.

Following is the code that you copy/paste from carto
```html
<iframe width="100%" height="520" frameborder="0" src="https://michellejm.carto.com/viz/f07c01f8-85b7-11e6-96f9-0e05a8b3e3d7/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>
```


* Add your Name
```html
<hr>
your Name: <br/><br/>Description (Program, Year, Expertise)
<hr>
```

To complete this tutorial, please send the template as an .html file to Michelle at mam2518@columbia.edu. Fill in:

* your name,
* a tentative project title, and 
* a tentative project description. 

You can leave the Lorem Ipsum in the template until you are creating the final product. 

_____________________
This tutorial was prepared by Michelle McSweeney for the Conflict Urbanism: Language Justice Course offered as part of the Mellon Grant for Architecture in the Humanities in the Center for Spatial Research. It is based on a tutorial written by Medeeha Merchant, for Conflict Urbanism: Aleppo taught in Spring 2016 also by the Center for Spatial Research.
