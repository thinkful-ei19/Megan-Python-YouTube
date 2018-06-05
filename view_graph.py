import youtube_grabber
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


videos= youtube_grabber.videoInfo()

vid1Title='First Place: ' + videos['Video1']['Title']
vid2Title='Second Place: ' + videos['Video2']['Title']
vid3Title='Third Place: ' + videos['Video3']['Title']
vid4Title='Fourth Place: ' + videos['Video4']['Title']
vid5Title='Fifth Place: ' + videos['Video5']['Title']

vid1Views=videos['Video1']['Views'].replace(',', '')
vid2Views=videos['Video2']['Views'].replace(',', '')
vid3Views=videos['Video3']['Views'].replace(',', '')
vid4Views=videos['Video4']['Views'].replace(',', '')
vid5Views=videos['Video5']['Views'].replace(',', '')

labels = vid1Title , vid2Title, vid3Title, vid4Title, vid5Title
fracs = [int(vid1Views), int(vid2Views), int(vid3Views), int(vid4Views), int(vid5Views)]


explode = (0.05, 0, 0, 0, 0)

the_grid = GridSpec(2, 2)

# plt.subplot(the_grid[0, 0], aspect=1)

# plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)

# plt.subplot(the_grid[0, 0], aspect=1)

# font = {'weight'   : 'bold'}

# plt.pie(fracs, explode=explode, textprops=font, labels=labels, autopct='%.0f%%', shadow=True)

plt.subplot(the_grid[0, 0], aspect=1)

patches, texts, autotexts = plt.pie(fracs, explode=explode, labels=labels,
                                    autopct='%.0f%%',
                                    shadow=True, radius=1)

# # Make the labels on the small plot easier to read.
for t in texts:
    t.set_size('smaller')
for t in autotexts:
    t.set_size('x-small')
autotexts[0].set_color('y')

# plt.subplot(the_grid[1, 1], aspect=1)

# # Turn off shadow for tiny plot with exploded slice.
# patches, texts, autotexts = plt.pie(fracs, explode=explode,
#                                     labels=labels, autopct='%.0f%%',
#                                     shadow=False, radius=0.5)
# for t in texts:
#     t.set_size('smaller')
# for t in autotexts:
#     t.set_size('x-small')
# autotexts[0].set_color('y')

plt.show()