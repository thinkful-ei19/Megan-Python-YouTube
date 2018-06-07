import youtube_grabber
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib as mpl


def graphs(videos,videoObj1, lst):

# create original of viewcount:

    vid1Views=videos['Video1']['Views'].replace(',', '')
    vid2Views=videos['Video2']['Views'].replace(',', '')
    vid3Views=videos['Video3']['Views'].replace(',', '')
    vid4Views=videos['Video4']['Views'].replace(',', '')
    vid5Views=videos['Video5']['Views'].replace(',', '')

    vid1Title='First Place: \n'  + "Title: "+ videos['Video1']['Title']+ "\nViews: " +vid1Views
    vid2Title='Second Place: \n'  + "Title: "+ videos['Video2']['Title']+ "\nViews: " +vid2Views
    vid3Title='Third Place: \n'  + "Title: "+ videos['Video3']['Title']+ "\nViews: " +vid3Views
    vid4Title='Fourth Place: \n'  + "Title: "+ videos['Video4']['Title']+ "\nViews: " +vid4Views
    vid5Title='Fifth Place: \n'  + "Title: "+ videos['Video5']['Title']+ "\nViews: " +vid5Views

    

# create difference:
    firstViewDifference=lst[0]
    firstTitle="First Place View Change: \n" + "Title: " + videoObj1['1'][0] + "\nView Change: " +str(firstViewDifference)

    secondViewDiff= lst[1]
    secondTitle="Second Place View Change: \n" +"Title: "+ videoObj1['2'][0]+ "\nView Change: " +str(secondViewDiff)
    
    thirdViewDiff= lst[2]
    thirdTitle="Third Place View Change: \n" +"Title: "+videoObj1['3'][0]+ "\nView Change: " +str(thirdViewDiff)
    
    fourthViewDiff= lst[3]
    fourthTitle="Fourth Place View Change: \n" +"Title: "+videoObj1['4'][0]+ "\nView Change: "+str(fourthViewDiff)
    
    fifthViewDiff=lst[4]
    fifthTitle="Fifth Place View Change: \n" +"Title: "+ videoObj1['5'][0]+ "\n View Change: "+str(fifthViewDiff)

    #start graphs:
    labels = vid1Title , vid2Title, vid3Title, vid4Title, vid5Title
    fracs = [int(vid1Views), int(vid2Views), int(vid3Views), int(vid4Views), int(vid5Views)]
    
    labels2 = firstTitle , secondTitle, thirdTitle, fourthTitle, fifthTitle
    fracs2 = [int(firstViewDifference), int(secondViewDiff), int(thirdViewDiff), int(fourthViewDiff), int(fifthViewDiff)]
            


    # incase I want to go back to displaying both percentages and viewcounts together:
    # def make_autopct(fracValues):
    #     def my_autopct(pct):
    #         total = sum(fracValues)
    #         val = int(round(pct*total/100.0))
    #         return '{p:.2f}%  \n ({v:d})'.format(p=pct,v=val)
    #     return my_autopct

    # if the % is greater than 0% then go ahead and show it, if not then set that place to an empty string to not show:
    def my_autopct(pct):
        return ('%.2f' % pct) if pct > 0 else ''

    explode = (0.05, 0, 0, 0, 0)

    the_grid = GridSpec(2, 2)

    plt.subplot(the_grid[0, 0], aspect=1)

    patches, texts, autotexts = plt.pie(fracs, explode=explode,
                                        autopct='%1.0f%%', pctdistance=1.275,
                                        shadow=True, radius=1, wedgeprops = {'linewidth': 3})
    
    for t in texts:
        t.set_size('smaller')
        t.set_multialignment('center')
    for t in autotexts:
        t.set_size('x-small')
    
    plt.legend(patches, labels=labels, bbox_to_anchor=(1,1.025), loc="upper left")
    plt.subplots_adjust(left=0.4, bottom=0.1, right=1.25)

    plt.subplot(the_grid[1, 1], aspect=1)

    patches, texts, autotexts = plt.pie(fracs2, explode=explode,
                                        autopct=my_autopct,pctdistance=1.125,
                                        shadow=True, radius=1)

    for t in texts:
        t.set_size('smaller')
        t.set_multialignment('center')
    for t in autotexts:
        t.set_size('x-small')

    plt.legend(patches, labels=labels2, bbox_to_anchor=(1,1), loc="upper left")
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.6)

    plt.show()