import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import numpy as np
import operator
import pandas as pd

from Abstract import Conference
# ================================== read conferences csv ==================================
data = pd.DataFrame()
df = pd.read_csv('conferences.csv')
df['date'] = pd.to_datetime(df['date'])

# ================================== load into Conference and sort it ==================================
conferences = list()
for index in range(len(df)):
    C = Conference(df['nick_name'][index],df['date'][index])
    conferences.append(C)
sorted_conferences = sorted(conferences, key=operator.attrgetter('date'))

# ================================== timeline ==================================

fig, ax = plt.subplots(figsize=(8, 5))

# set the height of the text
levels = np.array([8,-7.5,7,-6.5, 6, -5, 4, -3, 2, -1, 1])

# Create the base line
start = min(df['date'])
stop = max(df['date'])
ax.plot((start, stop), (0, 0), 'k', alpha=.5)

# Iterate through releases annotating each one
for ii in range(len(sorted_conferences)):
    
    iname,idate = sorted_conferences[ii].nick_name,sorted_conferences[ii].date

    # draw the scatter of the timeline
    ax.scatter(idate, 0, s=5, facecolor='w', edgecolor='k', zorder=9999)

    # set level and vert for line and text
    level = levels[ii % 11]
    vert = 'top' if level < 0 else 'bottom'

    # Plot a line up to the text
    ax.plot((idate, idate), (0, level), c='r', alpha=.8)
    # Give the text a faint background and align it properly
    ax.text(idate, level, iname + idate.strftime("%Y-%m-%d"), rotation=0,
            horizontalalignment='center', verticalalignment=vert, fontsize=8,
            backgroundcolor=(1., 1., 1., .3))

# title
ax.set(title="System related conferences timeline")

# Set the xticks formatting
'''
format xaxis with 3 month intervals
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=3))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
fig.autofmt_xdate()
'''

# Remove components for a cleaner look
plt.setp((ax.get_yticklabels() + ax.get_yticklines() + list(ax.spines.values())), visible=False)
plt.tick_params(bottom=False,labelbottom=False)

plt.show()
