# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 02:28:25 2019

@author: nagendraSingh
"""
import sys
import math
import random


def neibhour(k, s, cmean, t):
    temp = []
    print('t is ', t)
    for i in range(s):
        # print('dis without round: ',cmean[k][-1]-cmean[i][-1])
        d = abs(cmean[k][-1] - cmean[i][-1])
        # print('distance is: ',d)
        if (d < t) and (i != k):
            temp.append(i)
    #    print('in function neighbours of ',k,' are ',temp)
    return temp


# _____________Handeling input1.txt file and extracting data from it________
f1 = open(sys.argv[1], "r")  # variable handles first input filr
content = f1.read()
data = content.split("\n")
s = int(data[0])  # number of states
n = int(data[1])  # number of "BIMARIES"
m = int(data[2])  # number of habits
t = float(data[3])  # thrashold value for neighbours
mn = m + n + 1
# print("S:",s," N:",n," M: ",m," T :",t)
for i in range(4):
    del data[0]
habit = []  # handles that habit causes for BIMARI or not
# print(data)
# ------------------extracting data in worst manner----------------------
# -raelly this is too much bad or you can say that it is like hardcoding
for i in range(m):
    habit.append(data[i])
# #f2=open(sys.argv[2],"r")
# print(habit)
for i in range(m):
    temp = habit[i].split(' ')
    #    print(temp)
    habit[i] = temp
hToD = []
for i in range(m):
    hToD.append([])
    for j in range(len(habit[i])):
        if habit[i][j] == '1':
            hToD[i].append(j + 1)
# print("habit is: ",habit)
# ---------------------------time to handle input2.txt-----------
f2 = open(sys.argv[2], "r")
temp = []  # temp container to get the length of input2.txt file
temp = f2.read().split("\n")
f2.close()
f2 = open(sys.argv[2], "r")
data1 = []  # actual data matrix for clustering
# ------------arranging data in matrix ----------------------------
for i in range(0, len(temp) - 1):  # last line have a tab so 1 less time iteration
    data1.append(list(map(float, f2.readline().split("\t")[:mn])))
# print(data1)
# -------------------Now i have data in matrix format ----------------
# ***************now actual work is remaining which is clustering--------
# ********but clustering is not that much complex it is just a cake work now

# ~~~~~~~~~~~~~~~~~~~~Start with centroids~~~~~~~~~~~~~~~~~~~~~~~~~~
centroids = []
cluster = []
distance = 0
loc = []
d = 1 / (s - 1)
loc.append(0)
for i in range(1, s):
    loc.append(loc[-1] + d)
# print("length of loc: ",len(loc))
for i in range(s):
    temp1 = []
    # print("value of s: ",s)
    for j in range(len(data1)):
        temp1.append(abs(loc[i] - data1[j][-1]))
    loc[i] = min(temp1)
    l = temp1.index(min(temp1))
    centroids.append(l)
# print(centroids)
cmean = []
for i in range(s):
    cmean.append(data1[centroids[i]])
# print('Cluster mean at starting : ',cmean)
c_old = cmean
for i in range(len(data1)):
    point = []
    for k in range(s):
        dis = 0
        for j in range(mn):
            tempo = abs(cmean[k][j] - data1[i][j])
            dis += tempo * tempo
        dis = round(math.sqrt(dis), 2)
        point.append(dis)
    l = point.index(min(point))
    for j in range(mn):
        cmean[l][j] = round((cmean[l][j] + data1[i][j]) / 2, 2)
# print("final cmean: ",cmean)
clusters = cmean

out = open(sys.argv[3], "w")
for i in range(s):
    for j in range(len(clusters[i])):
        print(clusters[i][j], end=" ", file=out)
    print(file=out)
