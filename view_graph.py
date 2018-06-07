import youtube_grabber
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib as mpl
# mpl.rcParams['font.size'] = 9.0
# mpl.rcParams['lines.linewidth'] = 20000000

def graphs(videos,videoObj1, lst):

# create original of viewcount:
    vid1Title='First Place: \n' + videos['Video1']['Title']
    vid2Title='Second Place: \n' + videos['Video2']['Title']
    vid3Title='Third Place: \n' + videos['Video3']['Title']
    vid4Title='Fourth Place: \n' + videos['Video4']['Title']
    vid5Title='Fifth Place: \n' + videos['Video5']['Title']

    vid1Views=videos['Video1']['Views'].replace(',', '')
    vid2Views=videos['Video2']['Views'].replace(',', '')
    vid3Views=videos['Video3']['Views'].replace(',', '')
    vid4Views=videos['Video4']['Views'].replace(',', '')
    vid5Views=videos['Video5']['Views'].replace(',', '')

    

# create difference:
    firstTitle="First Place View Change: \n" + videoObj1['1'][0]
    firstViewDifference=lst[0]

    secondTitle="Second Place View Change: \n" +videoObj1['2'][0]
    secondViewDiff= lst[1]

    thirdTitle="Third Place View Change: \n" +videoObj1['3'][0]
    thirdViewDiff= lst[2]

    fourthTitle="Fourth Place View Change: \n" +videoObj1['4'][0]
    fourthViewDiff= lst[3]

    fifthTitle="Fifth Place View Change: \n" + videoObj1['5'][0]
    fifthViewDiff=lst[4]

    #start graphs:
    labels = vid1Title , vid2Title, vid3Title, vid4Title, vid5Title
    fracs = [int(vid1Views), int(vid2Views), int(vid3Views), int(vid4Views), int(vid5Views)]
    
    labels2 = firstTitle , secondTitle, thirdTitle, fourthTitle, fifthTitle
    fracs2 = [int(firstViewDifference), int(secondViewDiff), int(thirdViewDiff), int(fourthViewDiff), int(fifthViewDiff)]

    def make_autopct(fracValues):
        def my_autopct(pct):
            total = sum(fracValues)
            val = int(round(pct*total/100.0))
            return '{p:.2f}%  \n ({v:d})'.format(p=pct,v=val)
        return my_autopct

    explode = (0.05, 0, 0, 0, 0)

    the_grid = GridSpec(2, 2)

    plt.subplot(the_grid[0, 0], aspect=1)

    originalGraph = plt.pie(fracs, explode=explode, labels=labels,
                                        autopct=make_autopct(fracs),
                                        shadow=True, radius=1)

    plt.subplot(the_grid[1, 1], aspect=1)

    differenceGraph, texts, autotexts = plt.pie(fracs2, explode=explode, labels=labels2,
                                        autopct=make_autopct(fracs2),
                                        shadow=True, radius=1)

    for t in texts:
        t.set_size('x-small')
        t.set_multialignment('center')
    for t in autotexts:
        t.set_size('x-small')

    originalGraph.set_lw(40)


    plt.show()