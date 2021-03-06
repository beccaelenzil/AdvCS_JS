import matplotlib.pyplot as plt
from time import sleep
from random import shuffle

plt.ion()

y = [i for i in range(100)]
x = [i for i in range(len(y))]

for i in range(10):       ## Do the following 50 times
    plt.clf()             ## Clear the plot
    plt.bar(x,y)          ## Plot a bar chart
    plt.pause(0.5)        ## Pause
    #or sleep(0.5)        ## Pause
    shuffle(y)            ## Shuffle the data

plt.show()