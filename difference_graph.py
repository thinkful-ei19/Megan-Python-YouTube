import youtube_grabber
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def differenceChart(videoObj1, lst):
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

    labels = firstTitle , secondTitle, thirdTitle, fourthTitle, fifthTitle
    fracs = [int(firstViewDifference), int(secondViewDiff), int(thirdViewDiff), int(fourthViewDiff), int(fifthViewDiff)]

    def make_autopct(fracValues):
        def my_autopct(pct):
            total = sum(fracValues)
            val = int(round(pct*total/100.0))
            return '{p:.2f}%  \n ({v:d})'.format(p=pct,v=val)
        return my_autopct

    explode = (0.05, 0, 0, 0, 0)

    the_grid = GridSpec(2, 1)

    plt.subplot(the_grid[0, 0], aspect=1)

    patches, texts, autotexts = plt.pie(fracs, explode=explode, labels=labels,
                                        autopct=make_autopct(fracs),
                                        shadow=True, radius=1)

    for t in texts:
        t.set_size('smaller')
        t.set_multialignment('center')
    for t in autotexts:
        t.set_size('x-small')


    plt.show()