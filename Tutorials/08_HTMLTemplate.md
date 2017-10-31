## Setting Up A Conflict Urbanism: InfraPolitics Case Study

This tutorial introduces the html template we expect you to use. It is built on Bootstrap and customized for all the Conflict Urbanism courses. Through editing the pre-made template, you will develop familiarity with HTML and CSS. These two languages drive both the structure and formatting of webpages. 

If you are already familiar with HTML and CSS, you may skip ahead to working directly with the template provided. Please do  *not* to change the style settings, so that everyone's project retains a similar aesthetic. You can change the individual CSS for your individual project within reason (no pink text, lobster fonts, etc), but not the project CSS.

This tutorial is primarily an introduction to using the template we have provided so you can submit your final project.

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

* Case Study Template Files


### Introduction to HTML/CSS

The following section is adapted from [here](http://learn.shayhowe.com/html-css/building-your-first-web-page/) and provides a good understanding of Web Basics. Please refer to it for more information. Likewise, if you are interested in diving deeper, work through this (7 hour) [codeacademy course](https://www.codecademy.com/learn/web), on Code Academy. 

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

```

================================================================= -->
<!doctype html>
<html lang="en">
  <head>
    <!-- Change to your project's title -->
    <title>Project Title</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
    <!-- Site specific CSS -->
    <link rel="stylesheet" href="css/csr-casestudy.css">
    <link rel="stylesheet" href="css/footnotes.css">
    <!-- Webfont CSS -->
    <link type="text/css" rel="stylesheet" href="http://fast.fonts.net/cssapi/c28915cb-7a1f-477c-9084-e9e755ede452.css">

  </head>
  <body>
    <!-- Top navbar (do not change)-->
    <nav class = "navbar fixed-top c4sr-navbar" role="navigation" id="c4sr-navbar">
      <div class="container-fluid" id="c4sr-titlemobile">
          <div class="c4sr-menu-left">
              <a class = "navbar-link" href="http://c4sr.columbia.edu/conflict-urbanism-infrapolitics/seminar/index.html">Conflict Urbanism: InfraPolitics</a>
          </div>
          <div class ="c4sr-menu-right">
              <a class = "navbar-link" href="http://c4sr.columbia.edu/conflict-urbanism-infrapolitics/seminar/index.html">About</a>
              <a class = "navbar-link" href="http://c4sr.columbia.edu/conflict-urbanism-infrapolitics/seminar/index.html#projects">Projects</a>
              <a class = "navbar-link" href="http://c4sr.columbia.edu/conflict-urbanism-infrapolitics/seminar/index.html#people">People</a>
          </div>
      </div>
    </nav>
    <!-- Main content -->
    <div class="container-fluid">
    <div class="c4sr-contentwrapper">
      <div class ="row" id="top-row">
        <div class ="col-md-12" >
          <!-- Your project title -->
          <h2>Project Title: Subtitle that is standard for long academic titles</h4>
          <!-- Your name, degree program and school -->
          <div class="caption">Student Name, Second Student Name, Third Student Name</div>
          </div>
        </div>

    <!-- Side navigation menu -->
      <div class = "row">
        <div class = "col-md-3">
          <div class ="nav" id="sticky-menu">
            <ul class = "c4sr-sidenav">
              <!-- Make as many sections as fit your project  -->
              <!-- Change the href to match the associated h5 id tag -->
              <li><a href="#intro">Introduction</a></li>
              <li><a href="#first">Section One</a></li>
              <li><a href="#second">Section Two</a></li>
            </ul>
          </div>
        </div>

      <!-- Section for the text and images for your project -->
        <div class = "col-md-6 body-text">
          <!-- create your own id tag that matches the href you create in the sidenav section-->
          <h5 id ="intro">Introduction</h5><br/>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vel nibh condimentum, imperdiet nisi at, accumsan lectus. Vestibulum suscipit varius urna et tempus. Donec quam lorem, fermentum ut augue id, pretium lacinia sapien. Sed aliquam turpis placerat lectus condimentum, sit amet consequat mi rhoncus. Donec sit amet libero varius eros molestie vehicula. Nullam mollis arcu quis leo ullamcorper, eu sodales magna cursus. <a href="c4sr.columbia.edu">Vestibulum ante</a> ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis condimentum rutrum elit, id sagittis neque mollis nec.<div class="footnote">1</div> Nam ornare sit amet dui vel bibendum.<br/><br/> Aliquam at nunc quis erat faucibus laoreet. Nulla at lectus vehicula, ornare mi id, fringilla turpis. Maecenas sodales, lorem eu tincidunt laoreet, augue sapien blandit massa, in malesuada metus nibh tempus urna. Sed laoreet purus nisi, vel sodales lorem pulvinar vitae.

          <!-- embeded image -->
          <img src="img/testimage.png" class="img-fluid" id="c4sr-embed">
          <!-- image caption -->
          <div class="caption">This is a caption for your image</div>

          Ut at dolor vel quam venenatis dictum. Phasellus dapibus tincidunt ex, a tempus sapien lacinia at.
          <div class="footnote">2</div> Duis lobortis arcu in est eleifend tincidunt. Integer volutpat mi a nunc auctor, sodales sagittis massa fermentum. Cras purus purus, auctor at eros eu, maximus cursus enim. Cras efficitur eget elit auctor dapibus. In molestie nisl nunc, quis malesuada nunc scelerisque sit amet. Quisque ac quam facilisis, tempus justo quis, congue nunc. Quisque mauris arcu, porta nec purus id, blandit imperdiet mi.
          <br/><br/> Aliquam at nunc quis erat faucibus laoreet. Nulla at lectus vehicula, ornare mi id, fringilla turpis. Maecenas sodales, lorem eu tincidunt laoreet, augue sapien blandit massa, in malesuada metus nibh tempus urna. Sed laoreet purus nisi, vel sodales lorem pulvinar vitae.<div class="footnote">3</div>  Ut at dolor vel quam venenatis dictum. Phasellus dapibus tincidunt ex, a tempus sapien lacinia at. Duis lobortis arcu in est eleifend tincidunt. Integer volutpat mi a nunc auctor, sodales sagittis massa fermentum. Cras purus purus, auctor at eros eu, maximus cursus enim. Cras efficitur eget elit auctor dapibus. In molestie nisl nunc, quis malesuada nunc scelerisque sit amet. Quisque ac quam facilisis, tempus justo quis, congue nunc. Quisque mauris arcu, porta nec purus id, blandit imperdiet mi.<br/><br/>

          <h5 id="first">Section One</h5>
          Aliquam at nunc quis erat faucibus laoreet. Nulla at lectus vehicula, ornare mi id, fringilla turpis. Maecenas sodales, lorem eu tincidunt laoreet, augue sapien blandit massa, in malesuada metus nibh tempus urna. Sed laoreet purus nisi, vel sodales lorem pulvinar vitae. Ut at dolor vel quam venenatis dictum. Phasellus dapibus tincidunt ex, a tempus sapien lacinia at. Duis lobortis arcu in est eleifend tincidunt. Integer volutpat mi a nunc auctor, sodales sagittis massa fermentum. Cras purus purus, auctor at eros eu, maximus cursus enim. Cras efficitur eget elit auctor dapibus. In molestie nisl nunc, quis malesuada nunc scelerisque sit amet. Quisque ac quam facilisis, tempus justo quis, congue nunc. Quisque mauris arcu, porta nec purus id, blandit imperdiet mi.

          <!-- Embedded map or other item -->
          <!-- the src value could be to an html file you write -->
          <div class="embed-responsive embed-responsive-4by3">
            <iframe class="embed-responsive-item" id="c4sr-embed" height="700px"
            src="http://maps.stamen.com/toner/embed#10/40.7476/-73.9810" allowfullscreen>
            </iframe>
          </div>

          <!-- <img src="img/testimage.png" class="img-fluid" id="c4sr-img"> -->

          <div class="caption">This is a caption for your embedded item</div>

          Ut at dolor vel quam venenatis dictum. Phasellus dapibus tincidunt ex, a tempus sapien lacinia at. Duis lobortis arcu in est eleifend tincidunt. Integer volutpat mi a nunc auctor, sodales sagittis massa fermentum. Cras purus purus, auctor at eros eu, maximus cursus enim. Cras efficitur eget elit auctor dapibus. In molestie nisl nunc, quis malesuada nunc scelerisque sit amet. Quisque ac quam facilisis, tempus justo quis, congue nunc. Quisque mauris arcu, porta nec purus id, blandit imperdiet mi.<br/><br/>
          <h5 id="second">Section Two</h5>
          Aliquam at nunc quis erat faucibus laoreet. Nulla at lectus vehicula, ornare mi id, fringilla turpis. Maecenas sodales, lorem eu tincidunt laoreet, augue sapien blandit massa, in malesuada metus nibh tempus urna. Sed laoreet purus nisi, vel sodales lorem pulvinar vitae. Ut at dolor vel quam venenatis dictum. Phasellus dapibus tincidunt ex, a tempus sapien lacinia at. Duis lobortis arcu in est eleifend tincidunt. Integer volutpat mi a nunc auctor, sodales sagittis massa fermentum. Cras purus purus, auctor at eros eu, maximus cursus enim. Cras efficitur eget elit auctor dapibus. In molestie nisl nunc, quis malesuada nunc scelerisque sit amet. Quisque ac quam facilisis, tempus justo quis, congue nunc. Quisque mauris arcu, porta nec purus id, blandit imperdiet mi.<br/>
          <div class="mobile-warning">Please note: footnotes not visible on mobile.</div>
        <a class="btn btn-default btn-block c4sr-button c4sr-big-button" href="http://c4sr.columbia.edu/conflict-urbanism-infrapolitics/seminar/index.html">Return to Student Projects</a>
        </div>

        <!-- Footnotes -->
        <div class = "col-md-3">
          <div class = "footnotes">
            <!-- Footnote  1 -->
            <div class = "footnote-ref footnote-ref-1">
              <sup>1</sup>
              <a href="google.com">Content of footnote one</a>
            </div>
            <!-- Footnote 2 -->
            <div class = "footnote-ref footnote-ref-2">
              <sup>2</sup>
              <a href="google.com">Content of footnote two</a>
            </div>
            <!-- Footnote 3 -->
            <div class = "footnote-ref footnote-ref-3">
              <sup>3</sup>
              <a href="google.com">Content of footnote three</a>
            </div>

          </div>
        </div>
      </div>
      <footer class="footer c4sr-footer">
        <div class="container-fluid">
          <div class="row">
              <div class="col-md-3 c4sr-footer-id"><a href="http://c4sr.columbia.edu/" target="_blank">Center for Spatial Research<br/>Columbia University<br/></a><div class="cu-crown">
                  <img src="img/cu-crown.jpg" />
              </div></div>
              <div class="col-md-3">Graduate School of Architecture,<br/>Planning and Preservation<br/>Schermerhorn Hall Extension #654<br/>1172 Amsterdam Avenue<br/>New York, NY 10027<br/>
              </div>
              <div class="col-md-3"><a class="active" href="mailto:info@c4sr.columbia.edu">info@c4sr.columbia.edu</a><br/>Tel +1 212 555 1212<br/>Fax +1 212 555 1213</div>
              <div class="col-md-3"><a href="https://twitter.com/c4sr_columbia" target="_blank">Follow us on Twitter</a><br/><a href="mailto:c4sr-updates-join@lists.columbia.edu" target="_blank">Sign up for our Mailing List</a><br/></div>
          </div>
        </div>
      </footer>
    </div>
  </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
</body>
</html>

```


### Code Explained

* Add Title and establish dependencies. We will specify the characterset, and specify that it is responsive. Then add the Bootstrap, CSS, and Webfont CSS files

```
<!doctype html>
<html lang="en">
  <head>
    <!-- Change to your project's title -->
    <title>Project Title</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
    <!-- Site specific CSS -->
    <link rel="stylesheet" href="css/csr-casestudy.css">
    <link rel="stylesheet" href="css/footnotes.css">
    <!-- Webfont CSS -->
    <link type="text/css" rel="stylesheet" href="http://fast.fonts.net/cssapi/c28915cb-7a1f-477c-9084-e9e755ede452.css">

  </head>
  ```

* Leave the Navigation Bar Alone

```
  <body>
    <!-- Top navbar (do not change)-->
    <nav class = "navbar fixed-top c4sr-navbar" role="navigation" id="c4sr-navbar">
      <div class="container-fluid" id="c4sr-titlemobile">
          <div class="c4sr-menu-left">
              <a class = "navbar-link" href="http://c4sr.columbia.edu/conflict-urbanism-infrapolitics/seminar/index.html">Conflict Urbanism: InfraPolitics</a>
          </div>
          <div class ="c4sr-menu-right">
              <a class = "navbar-link" href="http://c4sr.columbia.edu/conflict-urbanism-infrapolitics/seminar/index.html">About</a>
              <a class = "navbar-link" href="http://c4sr.columbia.edu/conflict-urbanism-infrapolitics/seminar/index.html#projects">Projects</a>
              <a class = "navbar-link" href="http://c4sr.columbia.edu/conflict-urbanism-infrapolitics/seminar/index.html#people">People</a>
          </div>
	</div>
    </nav>
```

	  
* Open the main containers for the content and identify the Title & Group Members

```
    <!-- Main content -->
    <div class="container-fluid">
    <div class="c4sr-contentwrapper">
      <div class ="row" id="top-row">
        <div class ="col-md-12" >
          <!-- Your project title -->
          <h2>Project Title: Subtitle that is standard for long academic titles</h4>
          <!-- Your name, degree program and school -->
          <div class="caption">Student Name, Second Student Name, Third Student Name</div>
          </div>
        </div>
```

* Add structure to your case study by dividing it into components, akin to chapters or sections in a paper. In this example, we have 3 sections. Below is a list for adding to the menu on the left. These titles are linked to positions in the text using the href attribute (href="#intro" refers to id="intro" in the remainder of the template)
```
    <!-- Side navigation menu -->
      <div class = "row">
        <div class = "col-md-3">
          <div class ="nav" id="sticky-menu">
            <ul class = "c4sr-sidenav">
              <!-- Make as many sections as fit your project  -->
              <!-- Change the href to match the associated h5 id tag -->
              <li><a href="#intro">Introduction</a></li>
              <li><a href="#first">Section One</a></li>
              <li><a href="#second">Section Two</a></li>
            </ul>
          </div>
        </div>
```

* Add Chapter Text
Add text or image paragraphs for each chapter. The title of your chapter can be different (longer) than the one you use for the Table of Contents. 

```
      <!-- Section for the text and images for your project -->
        <div class = "col-md-6 body-text">
          <!-- create your own id tag that matches the href you create in the sidenav section-->
          <h5 id ="intro">Introduction</h5><br/>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vel nibh condimentum, imperdiet nisi at, accumsan lectus. Vestibulum suscipit varius urna et tempus. Donec quam lorem, fermentum ut augue id, pretium lacinia sapien. Sed aliquam turpis placerat lectus condimentum, sit amet consequat mi rhoncus. Donec sit amet libero varius eros molestie vehicula. Nullam mollis arcu quis leo ullamcorper, eu sodales magna cursus. <a href="c4sr.columbia.edu">Vestibulum ante</a> ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis condimentum rutrum elit, id sagittis neque mollis nec.<div class="footnote">1</div> Nam ornare sit amet dui vel bibendum.<br/><br/> Aliquam at nunc quis erat faucibus laoreet. Nulla at lectus vehicula, ornare mi id, fringilla turpis. Maecenas sodales, lorem eu tincidunt laoreet, augue sapien blandit massa, in malesuada metus nibh tempus urna. Sed laoreet purus nisi, vel sodales lorem pulvinar vitae.
```

* Annotations & Citations
You will use footnotes for citation. They are responsive to where you are on the case study, and appear on the right side of the page. To add a footnote, insert the following line of code. Please change numbers in order. Everytime you add a footnote, you will be required to go to the footnote section of the code, to add in the text and link. To add a footnote, insert the following code next to where you want the foot note. Start from #1, and change as you proceed.
```html
<div class="footnote footnote-1">1</div> 
```
Here's how it looks in the paragraph:
```
<h5 id ="intro">Introduction</h5><br/>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vel nibh condimentum, imperdiet nisi at, accumsan lectus. Vestibulum suscipit varius urna et tempus. Donec quam lorem, fermentum ut augue id, pretium lacinia sapien. Sed aliquam turpis placerat lectus condimentum, sit amet consequat mi rhoncus. Donec sit amet libero varius eros molestie vehicula. Nullam mollis arcu quis leo ullamcorper, eu sodales magna cursus. <a href="c4sr.columbia.edu">Vestibulum ante</a> ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis condimentum rutrum elit, id sagittis neque mollis nec.<div class="footnote">1</div> Nam ornare sit amet dui vel bibendum.<br/><br/> Aliquam at nunc quis erat faucibus laoreet. Nulla at lectus vehicula, ornare mi id, fringilla turpis. Maecenas sodales, lorem eu tincidunt laoreet, augue sapien blandit massa, in malesuada metus nibh tempus urna. Sed laoreet purus nisi, vel sodales lorem pulvinar vitae.
```

Then add the details to `Footnotes Section` at *end* of the code (initially at line 96)
``` 
<!-- Footnotes -->
        <div class = "col-md-3">
          <div class = "footnotes">
            <!-- Footnote  1 -->
            <div class = "footnote-ref footnote-ref-1">
              <sup>1</sup>
              <a href="google.com">Content of footnote one</a>
            </div>
            <!-- Footnote 2 -->
            <div class = "footnote-ref footnote-ref-2">
              <sup>2</sup>
              <a href="google.com">Content of footnote two</a>
            </div>
            <!-- Footnote 3 -->
            <div class = "footnote-ref footnote-ref-3">
              <sup>3</sup>
              <a href="google.com">Content of footnote three</a>
            </div>

          </div>
        </div>
      </div>
```

* Add Images

To add an Image, save the file in the <img> folder. Insert the following code:

```
          <!-- embeded image -->
          <img src="img/testimage.png" class="img-fluid" id="c4sr-embed">
          <!-- image caption -->
          <div class="caption">This is a caption for your image</div>
```


* Add Interactive Features

If you would like to include interactive features in the case study, the easiest way might be linking your built object to an image. We suggest this as oppose to integrating them into your case study. Interactives might be heavier files and be difficult to load.

1. Embed a map you made in a folder within your larger project's folder. If you map is in a folder called 'mymap', your src will be "mymap/mymapindex.html" or something similar

```
         <!-- Embedded map or other item -->
          <!-- the src value could be to an html file you write -->
          <div class="embed-responsive embed-responsive-4by3">
            <iframe class="embed-responsive-item" id="c4sr-embed" height="700px"
            src="http://maps.stamen.com/toner/embed#10/40.7476/-73.9810" allowfullscreen>
            </iframe>
          </div>

```

1. Linking Image to an Interactive html with an image as a placeholder:
```
<a href="filename.html"><img src="img/filename_interactive.png" class="img-responsive"/></a>
```


* Embed a map from another service using an iframe

```
<iframe width="100%" height="520" frameborder="0" src="YOUR_LINK"></iframe>
```

If you have questions about how to do things not covered in this tutorial, please do not hesitate to ask. 


To complete this tutorial, please 
* Change project title (39)
* Make another Section (55)
* Add an image (66)
* Embed a map you made (81)
* Update a Footnote (63 & 96)

Send the entire folder to Michelle.

_____________________
This tutorial was prepared by Michelle McSweeney for the Conflict Urbanism: InfraPolitics Course offered as part of the Mellon Grant for Architecture in the Humanities in the Center for Spatial Research. It is based on a tutorial written by Medeeha Merchant, for Conflict Urbanism: Aleppo taught in Spring 2016 also by the Center for Spatial Research.
The Template was created by Dare Brawley, based on a template from Medeeha Merchant.
