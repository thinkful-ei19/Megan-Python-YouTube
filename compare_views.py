# store the current videoObj...then wait 1 hour...then create new videoObj(2) and store new data there
# find based on url name or title and compare the viewcounts

import youtube_grabber
from threading import Timer
import time
import difference_graph
import view_graph


view_graph.originalGraph()


videoObj1=dict()
lst = [None] * 5

def startCompare():

    videos= youtube_grabber.videoInfo()

    videoObj1['1']= [videos['Video1']['Title'], int(videos['Video1']['Views'].replace(',', ''))]
    videoObj1['2']= [videos['Video2']['Title'], int(videos['Video2']['Views'].replace(',', ''))]
    videoObj1['3']= [videos['Video3']['Title'], int(videos['Video3']['Views'].replace(',', ''))]
    videoObj1['4']= [videos['Video4']['Title'], int(videos['Video4']['Views'].replace(',', ''))]
    videoObj1['5']= [videos['Video5']['Title'], int(videos['Video5']['Views'].replace(',', ''))]
    return videoObj1
startCompare()

def endCompare(videoObj1):
    firstTitle=videoObj1['1'][0]
    firstView=videoObj1['1'][1]
    secondTitle=videoObj1['2'][0]
    secondView=videoObj1['2'][1]
    thirdTitle=videoObj1['3'][0]
    thirdView=videoObj1['3'][1]
    fourthTitle=videoObj1['4'][0]
    fourthView=videoObj1['4'][1]
    fifthTitle=videoObj1['5'][0]
    fifthView=videoObj1['5'][1]

    time.sleep(2)
    count=0
    videos= youtube_grabber.videoInfo()
    while count < 60:
        count=count+1
        video= videos['Video{}'.format(count)]
        if video['Title'] == firstTitle:
            difference= int(video['Views'].replace(',', '')) - firstView
            lst[0]=difference
        elif video['Title'] == secondTitle:
            difference= int(video['Views'].replace(',', '')) - secondView
            lst[1]=difference
        elif video['Title'] == thirdTitle:
            difference= int(video['Views'].replace(',', '')) - thirdView
            lst[2]=difference
        elif video['Title'] == fourthTitle:
            difference= int(video['Views'].replace(',', '')) - fourthView
            lst[3]=difference
        elif video['Title'] == fifthTitle:
            difference= int(video['Views'].replace(',', '')) - fifthView
            lst[4]=difference
    print(lst)
    return lst
            
endCompare(videoObj1)

difference_graph.differenceChart(videoObj1, lst)