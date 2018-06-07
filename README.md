# Youtube Trending Graph Analysis

## Table of Contents:
- Technology Used
- Description
- Brief Overview of Files
- References

### Technology Used:
- Python
- Packages:
    - Beautiful Soup
    - Requests
    - MatPlotLib

### Description:
This app pulls data from the top 5 videos trending on YouTube and graph their view counts.  The app also compares the viewcount every 30 minutes and graphs the changes in viewcount so that users can see the rate at which the views are growing per hour.

### Checklist of MVP features:
    - Graph that shows top 5 trending videos and their viewcounts (shows that it is not necessarily dependent on overall viewcount but on rate that the viewcount is going up)
    - Graph that shows the difference 30 minutes makes on viewcount for each of the top 5 so that the user can see the rate of expansion

### Brief Overview of Files:
youtube-grabber.py
    - will grab the urls of the top 5 trending youtube videos by using BeautifulSoup.  Then the file will either use the YouTube api to check the viewcount of each video or use BeautifulSoup again to find the viewcount(depending on YouTube API capabilities and the information given from the original Beautiful Soup response)

compare-views.py
    - stores the original viewcounts/titles and then, after 30 minutes, grabs the viewcounts again based on their titles.
    - it then compares the original viewcount with the after 30 minute viewcount to generate a list of changes
    - these viewcounts, titles, and the difference list are then sent into the function found in view_graph to create the graphs

view-graph.py
    - uses the information taken from compare-views to correctly graph an original viewcount graph and a graph based on the differences in viewcounts after 30 minutes. Each graph is complete with a legend that shows the title an viewcount.

test.html
    - shows an example of the youtube page we are getting back from Beautiful Soup in order to grab the necessary elements (Does not affect rest of code, just there to provide an example)


### References:
-Used https://github.com/jessecordeiro/youtube-trending-videos-scraper/blob/master/youtube_trending_scraper/scraper.py as a base for ideas on how to work Beautiful Soup and get original HTML back, understood and changed based on needs for this app