# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 02:28:25 2019

@author: nagendraSingh
"""
import sys
import math

f1 = open(sys.argv[1], "r")  # variable handles first input filr
content = f1.read()
data = content.split("\n")
s = int(data[0])  # number of states
n = int(data[1])  # number of "BIMARIES"
m = int(data[2])  # number of habits
t = float(data[3])  # thrashold value for neighbours
mn = m + n + 1
# print("S:",s," N:",n," M: ",m," T :",t)
f2 = open(sys.argv[2], "r")

clusters = []

for i in range(s):  # last line have a tab so 1 less time iteration
    clusters.append(list(map(float, f2.readline().split(" ")[:mn])))

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
Bimari = []
for i in range(s):
    Bimari.append([])
for i in range(s):
    for j in range(m):
        if clusters[i][j] > 0.7:
            Bimari[i].append(j + 1)
# print("Bimaries: ",Bimari)
for i in range(s):
    for j in range(n):
        if clusters[i][m + j] > 0.5:
            #            print('State: ',i+1,' habitual to habit: ',j+1)
            for k in range(len(hToD[j])):
                Bimari[i].append(hToD[j][k])
    Bimari[i] = list(set(Bimari[i]))
# print('final biimaris are: ',Bimari)
neighbours = []
for i in range(s):
    neighbours.append([])
    for z in range(s):
        # print('difference is : ',clusters[i][-1]-clusters[z][-1])
        if abs(clusters[i][-1] - clusters[z][-1]) < t:
            neighbours[i].append(z)
    temp = set([])
    #    print('neighbours of: ',i,' are ',neighbours[i])
    if len(neighbours[i]) > 1:
        for j in range(len(neighbours[i])):
            temp = temp | set(Bimari[neighbours[i][j]])
        #        print('temp is',temp)
        for j in neighbours[i]:
            Bimari[j] = list(temp)
            Bimari[j] = list(set(Bimari[j]))
out = open(sys.argv[3], "w")
for i in range(s):
    if len(Bimari[i]) == 0:
        print(0)
    else:
        for j in range(len(Bimari[i])):
            print(Bimari[i][j], end=" ", file=out)
        print(file=out)
