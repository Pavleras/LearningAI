import unittest
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

def loadData():
    ctdata = []
    for i in range(100):
        delta = datetime.timedelta(days=random.randrange(1,200))
        start_date = datetime.date.today() - delta
        while (True):
            delta = datetime.timedelta(days=random.randrange(1,200))
            end_date = datetime.date.today() - delta
            if (start_date < end_date):
                break
        ctdata.append({"start_date": start_date, "end_date": end_date}) 
    return ctdata

def cycletime(start_date,end_date):
    difference = end_date - start_date
    return difference.days
    
ctdata = loadData()

x = []
y = []
for item in ctdata:
    ct = cycletime(item["start_date"],item["end_date"])
    item["cycle_time"] =  ct
    x.append(mdates.date2num(item["end_date"]))
    y.append(item["cycle_time"])
    
plt.scatter(x,y)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
ax = plt.gca()  # Get the current Axes instance
ax.xaxis.set_major_locator(plt.MaxNLocator(nbins=7))  # Show only every 7th label
plt.gcf().autofmt_xdate()
plt.show()
