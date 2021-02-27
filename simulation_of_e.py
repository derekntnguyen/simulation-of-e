#  -*- coding: utf-8 -*-
'''
P4
Derek Nguyen
Created: 2019-03-06
Modified: 2019-03-06
Due: 2019-03-06
'''

# %% codecell

import numpy as np
import matplotlib # used to create interactive plots in the Hydrogen package of the Atom IDE
matplotlib.use('Qt5Agg') # used to create interactive plots in the Hydrogen package of the Atom IDE
import matplotlib.pyplot as plt

def esim(numTrials = 100000):
    '''
    Simulation of the mysteries of e by summing randomly generated numbers [0,1] and counting the number of calculations before the value is >= 1
    Parameters:
    numTrials, the number of trials you wish the simulation to perform
    '''
    simy = np.zeros(numTrials) # preallocate data

    for trial in np.arange(numTrials): # intialize loop that adds random numbers together until >= 1
        count = 1
        x = np.random.uniform(0,1)
        while x <= 1:
            x += np.random.uniform(0,1)
            count += 1

        simy[trial] = count # assigns number of numbers added together to data array

    avg = np.average(simy) # averages data

    plt.hist(simy)
    plt.title('Mystery of e')
    plt.xlabel('Number of Numbers Summed')
    plt.ylabel('Distribution')

    print('The average number of summed numbers = {}'.format(avg))

esim()
