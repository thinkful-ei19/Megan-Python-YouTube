import requests
import json
import html
from bs4 import BeautifulSoup



def videoInfo():
    response= requests.get('https://www.youtube.com/feed/trending')

    bssoup = BeautifulSoup(response.text, "html.parser")

    findVideos= bssoup.find_all(attrs={"class": "expanded-shelf-content-item"})


    videoObj=dict()

    count=0
    for videoComponent in findVideos:
        count= count+1
        video=dict()
        titlePart = videoComponent.find(attrs={"class": "yt-lockup-title"})
        titleLink = titlePart.find("a")
        titleUrl = titleLink.get('href')
        titleName = titleLink.get('title')
        infoOnVideo = videoComponent.find(attrs={"class": "yt-lockup-meta-info"})
        viewCount = infoOnVideo.contents[1].string.split(" ")[0]
        video['Title']= titleName
        video['URL']= titleUrl
        video['Views']= viewCount
        videoObj['Video{}'.format(count)]=video

    return videoObj

