'''
this exercise aims at visualizing CT using a scatterplot
'''
import unittest
import random
import matplotlib.pyplot as plt
import datetime

ctdata = {}

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

for item in ctdata:
    ct = cycletime(item["start_date"],item["end_date"])
    item["cycle_time"] =  ct
    x = item["end_date"]
    y = item["cycle_time"]
    plt.scatter(x,y)

plt.show()


