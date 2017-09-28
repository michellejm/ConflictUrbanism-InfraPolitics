# Web Scraping 
#### *aka Getting data not available for download*

### Premise
Often, the data we want is not available, or it is available on a website, but we cannot download it. American cities have done a very good job in recent years of developing "data portals" that allow for easy downloads of large amounts of data. If we only use that, we could probably still spend the rest of our lives analyzing and visualizing just what is there. 

However, sometimes (often times) our questions take us beyond the OpenData portals, and for this, we must figure out how to get the data from somewhere else. Our questions about Johannesburg is just such a case. We want census data. [We know it exists](http://www.statssa.gov.za), but there is nowhere to download it from. There is, however, one individual ([Adrian Firth](https://census2011.adrianfrith.com)) who built a website with all of this data available. It cannot be downloaded with one simple click, but it can be scraped, so that is what we are going to do. 

### Outcomes
By the end of this tutorial you will be able to:
* Determine if a website is scrape-able
* Estimate how difficult a website will be to scrape
* Identify the key components of a website that are needed to scrape the site
* Modify a Python program to scrape a website

### Downloads
I **highly** encourage you to download [Anaconda](https://www.anaconda.com/download) for this tutorial. You will not need it for the remainder of the class, but it is an excellent environment to learn Python in. It also comes with all of the packages we will need. If you have used Python on your computer before, you may have some of the packages already. However, this tutorial is written for use in an iPython Notebook, which comes with Anaconda. 
You maywant to use Google Chrome for this tutorial, and I will use Chrome. You can also use Firefox. Do NOT use Internet Explorer.

### General Idea
We have identified [a site](https://census2011.adrianfrith.com/place/798014056), and want the data in a format we can use (i.e., a csv, txt, xls, or other readable format). We also want the geometries that these numbers refer to. Looks like we can get both.

We will use Python, a programming language, and the Beautiful Soup package to scrape this site. Beautiful Soup (bs4) is designed to interact with the Internet *without* the use of a web browser (web browsers are Firefox, Chrome, etc.). If you MUST use a web browser (i.e., you are clicking on links), check out the [selenium](http://selenium-python.readthedocs.io/index.html) package. bs4 extracts information from webpages by searching the HTML and CSS to find elements (tags, id's, classes, etc.). It then returns to you whatever you ask for. bs4 comes pre-installed with Anaconda.

To make this work, we need to be able to *inspect* our websites. Inspecting a website means looking at the code the developer used to write it. 

Web scraping is highly specific to each site. The program we write will be based on the specific structure and organization of this site.

### Vocabulary
**List** An ordered set of values or strings [Male, Female, Black, White]
**Dictionary** An unordered set of key:value pairs.  {Male: 200, Female: 220, Black: 150, White:120}
**String** Words 'Male' 'Female'

HTML/CSS
**Element**

### General Practices
When doing any programming, especially in the beginning, it is essential to write out the steps. Even if the steps seem very basic, it will help to write out how you plan to approach the problem. The logic can get very confusing very quickly, and writing down each step in the most minute detail will help keep your program organized. [Flow charts and pseudocode](https://www.lynda.com/Programming-Foundations-tutorials/Writing-pseudocode/83603/90472-4.html) are invaluable tools in designing your program. It is much easier to think through the logic and then translate it into code than it is to do both at once. 
We will
1. Understand the organization of the website
2. Understand the organization of the data
3. Write a program that can 
    1. visit every site with data we want
    2. collect the data from that site
    3. Handle errors and problems
    4. Export the data to a csv file

### Understand the Website

#### Organization
The first thing we need to do is get a sense of how the site is organized.

Visit https://census2011.adrianfrith.com/place/798 We see that this site has a city page then a list of links that take you to the 'main pages'. Let's look at a mainpage https://census2011.adrianfrith.com/place/798014. We see that the mainpages have their own subpages. Let's look at a subpage https://census2011.adrianfrith.com/place/798014056. This seems to be the smallest areal unit, so that is what we want. It is good practice to go through an make sure it is fairly uniform throughout by clicking on som other mainpages and their subpages. 

Statistics only mean so much without a geometry associated with them. There seems to be a link on the right to download the geometries. This is great, we know we can get them. BUT! We only want to deal with one problem at a time. We are fairly sure we can get the geometries, so we will set that problem aside for the time being. 

Based on this structure, we will have to:
  1. Start at the main page for Johannesburg 
  *for each link on the JHB page, follow it to the main page*
  2. Follow each link to each 'Main Place' 
  *for each link on the main page, follow it to the subpage*
  3. Follow each link to each 'Sub Place'
  *read the data on this page*
 
#### Categories
As I flip through the pages, I see that the categories are not always in the same order, and not every category appears on every page (i.e., the category, 'White' only appears on some pages, but not all). There are also two categories called 'Other', this could cause problems. 

The ordering issue means I need to match the name of the category to my list of pre-defined categories (that is, I can't just fill by position in the page since the first category isn't always the first thing to be read). This means I will have to use something unordered such as a dictionary. 

All of the categories that appear across all pages are on the main JHB page. Fantastic! That will be my list.

#### Data
There seems to be raw numbers and percentages presented. I want the raw numbers, but not the percentages. The data also appears in 3 tables. I'd rather not have to deal with that, and would rather just make 1 big table of all the data (*I will come to regret this later, and would rewrite it with more time*)

### Inspecting the Pages
For this, Google Chrome is the best interface (I am a Firefox user, you can do this with FF, too, but I will use Chrome because it's easier to look at).
Go to the webpage you want to scrape. Right-click and select 'Inspect Element' 

![blank](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/ws1.png)

A box should appear on the right hand side with a lot of code. 

![blank](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/ws2.png)

There are a lot of tools here (at the bottom of this box) that could make our life easier. We won't use them now, but just know that they are there. 

Let's start with the JHB city site. We know that from here, we want to follow all of the links to other locations. 

If I move my cursor around in this box, it highlights different elements on the page. This indicates what part of the code on the right is making the page on the left. The code has little dropdown arrows. opening and closing those opens the containers that each thing sits in. Playing around like this, we see that the three grids are in three different containers. 
* Each container is called < table class="group">
* Each row is in a <tr class="datarow">
* The category is in the <td class = "namecell">
* The numbers are in the <td class = "datacell">
  
By right clicking on the title, I see that the top name is in the class attribute, 'topname'

![blank](https://github.com/michellejm/ConflictUrbanism-InfraPolitics/blob/master/img/ws2.png)
