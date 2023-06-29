# main.py
import random
import matplotlib.pyplot as plt
import numpy as np

list_values = [0,1]
list_results = []
total = 0
counter = 0 


def suma(a, b):
    return a + b

def average(scores):
    denominator = len(scores)
    numerator = 0

    for score in scores:
        numerator += score
    return numerator/denominator

def rand():
    return random.choice(list_values)

def calculator():
    
    if (rand()) == 1:
        return 1
    else:
        return -1


while(counter < 2000000):
    total += calculator()
    list_results.append(total)
    counter = counter + 1

plt.plot(list_results)
plt.show()


 


