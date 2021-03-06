#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 15:55:56 2018

@author: ryan
"""

# -----------------------------------------------------
# imports
# -----------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib

#plt.style.use('classic')

SMALL_SIZE = 14
MEDIUM_SIZE = 18
BIGGER_SIZE = 36

plt.rc('font', size=MEDIUM_SIZE)         # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=MEDIUM_SIZE)  # fontsize of the figure title

# -----------------------------------------------------
# load the data
# -----------------------------------------------------

# file path
fpath = 'data/'
fname = 'use1.txt'
fname2 = 'use2.txt'

data = np.loadtxt(fpath + fname, dtype=float)
data2 = np.loadtxt(fpath + fname2, dtype=float)
data = (data + data2) / 2

time = data[:, 2]
time = np.reshape(time, [int(len(time) / 6), 6])
time = time.T
fig, ax = plt.subplots()

im = ax.imshow(np.log(time), origin=[0,0], cmap='summer')
#cbar = ax.figure.colorbar(im, ax=ax)


plt.title('ProjectQ Simulator Performance', fontsize=16, fontweight='bold')
plt.xlabel('Number of Qubits')
plt.ylabel('Circuit Depth')

xlocs, xlabels = plt.xticks()
plt.xticks(range(12), range(16, 28))

plt.yticks(range(6), range(5, 35, 5))

# Loop over data dimensions and create text annotations.
for i in range(len(time)):
    for j in range(len(time[0])):
        tstr = str(time[i, j])
        text = ax.text(j, i, tstr[:5],
                       ha="center", va="center", color="k")

plt.clim(-4, 4)
plt.savefig("projectq-new.pdf", format="pdf")
