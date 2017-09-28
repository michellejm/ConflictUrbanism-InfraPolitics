# Web Scraping 
# *aka Getting data not available for download*

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

### General Idea
We will use Python, a programming language, and the Beautiful Soup package to scrape this site. Beautiful Soup (bs4) is designed to interact with the Internet *without* the use of a web browser (web browsers are Firefox, Chrome, etc.). If you MUST use a web browser (i.e., you are clicking on links), check out the [selenium](http://selenium-python.readthedocs.io/index.html) package. bs4 extracts information from webpages by searching the HTML and CSS to find elements (tags, id's, classes, etc.). It then returns to you whatever you ask for. bs4 comes pre-installed with Anaconda.

To make this work, we need to be able to *inspect* our websites. Inspecting a website means looking at the code the developer used to write it. 

### General Practices
When doing any programming, especially in the beginning, it is essential to write out the steps. Even if the steps seem very basic, it will help to write out how you plan to approach the problem. The logic can get very confusing very quickly, and writing down each step in the most minute detail will help keep your program organized.

### Understand the Website
The first thing we need to do is get a sense of how the site is organized.
1. Visit https://census2011.adrianfrith.com/place/798
This site has a main, city page then a list of links that take you to sub pages. Let's look at a subpage https://census2011.adrianfrith.com/place/798014. We see that the subpages have their own subpages. This tells us that we will have to:
  1. Start at the main page for Johannesburg *for each link on the JHB page, follow it to the main page*
  2. Follow each link to each 'Main Place' *for each link on the main page, follow it to the subpage*
  3. Follow each link to each 'Sub Place'
