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
Upon completion, this app will pull data from the top 5 videos trending on YouTube and graph their view counts.  As an extended task, this app will also compare the views every hour and graph the change in viewcount so we can see the rate at which the views are growing per hour.

### Checklist of MVP features:
    - Graph that shows top 5 trending videos and their viewcounts (shows that it is not necessarily dependent on overall viewcount but on rate that the viewcount is going up)
    - Graph that shows the difference 1 hour makes on viewcount for each of the top 5 so we can see the rate of expansion

### Brief Overview of Files:
youtube-grabber.py
    - will grab the urls of the top 5 trending youtube videos by using BeautifulSoup.  Then the file will either use the YouTube api to check the viewcount of each video or use BeautifulSoup again to find the viewcount(depending on YouTube API capabilities and the information given from the original Beautiful Soup response)
view-graph.py
    - will use the information taken from youtube-grabber.py and graph the view counts of each video
compare-views.py
    - will store the viewcount and then compare the views of each video every hour so we can see the rate of change for each video
difference-in-an-hour-graph.py
    - will use the information from compare-views.py to graph the change in viewcount per hour for each video

### References:
-Used https://github.com/jessecordeiro/youtube-trending-videos-scraper/blob/master/youtube_trending_scraper/scraper.py as a base for ideas on how to work Beautiful Soup and get original HTML back, understood and changed based on needs for this app