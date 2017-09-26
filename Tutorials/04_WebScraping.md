# Web Scraping aka 
## Getting data not available for download

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
I *highly* encourage you to download [Anaconda](https://www.anaconda.com/download) for this tutorial. You will not need it for the remainder of the class, but it is an excellent environment to learn Python in. It also comes with all of the packages we will need. If you have used Python on your computer before, you may have some of the packages already. However, this tutorial is written for use in an iPython Notebook, which comes with Anaconda. 

### 
