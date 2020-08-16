# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:35:25 2019

@author: nagendra
"""
#import math
import sys
import numpy as np
import pandas as pd


input1=open(sys.argv[1],"r")
n=int(input1.readline())
#print('number of nodes: ',n)
values=[]
for i in range(n):
    temp=input1.readline().split(',')

    values.append([item.strip() for item in temp])
relation=[]
#print('values of nodes: ',values)
for i in range(n):
    relation.append(list(map(int, input1.readline().split()[:n])))
#print('relationship matrix: ',relation)
dependent=[]
#print('numver of nodes ',n)
for i in range(n):
    dependent.append([])
    for j in range(n):
        if(relation[j][i]==1):
            #print(i,' depends on ',j)
            dependent[i].append(j)
#print('Dependency: ',dependent)
input2=[]
import csv
with open(sys.argv[2], 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        input2.append([item.strip() for item in row])
#print('csv file is ',input2)
del(input2[0])
#print('csv file is ',input2)
nodes=[None]*n
for i in range(n):
    if(len(dependent[i])==0):
        x=[]
        total=len(input2)
        for j in range(len(values[i])):
            count=0
            for k in range(len(input2)):
                if(input2[k][i]==values[i][j]):
                    count+=1
            if(total!=0):
                x.append(count/total)
            else:
                x.append(0)
        nodes[i]=x
#print(nodes)

#print('values ',values)
i=0
for i in range(n):
    
   
    if(len(dependent[i])==0):
        pass
    else:
        #print(i,'ss2') 
        sets = []
        combinations=[]
        #sets.append(values[i])
        for j in range(len(dependent[i])):
            sets.append(values[dependent[i][j]])
        #print('set ',sets)
        length = len(sets)
        #combinations.append(Cartesian(sets, length))
        #print('combinations of ',i,'th variable: ',combinations)
        stackover=list(pd.MultiIndex.from_product(sets))
        #print('stackover is ',stackover)
        input2=pd.DataFrame(input2)
        data=input2.copy()
        #print(dependent[i])
        #print(i)
        #print(stackover)
        y=[]
        for idx, k in enumerate(stackover):
            #print(k)
           
            for p,q in zip(dependent[i],k):
                #print(p,q)
                input2=input2[input2[p]==q]
            x=[]
            for m in values[i]:
                if(input2.shape[0]!=0):
                    p=input2[input2[i]==m].shape[0]/input2.shape[0]
                    x.append(p)
                else:
                   x.append(0)
                
            y.append(x)  
            input2=data
       
        nodes[i]=np.array(y)

            
        

#print(nodes)
#print(dependent)
out=open(sys.argv[3],"w")
for i in range(n):
    if(len(dependent[i])==0):
        for j in range(len(nodes[i])):
            print(round(nodes[i][j],4),' ',end='',file=out)
    else:
        nodes[i]=nodes[i].transpose()
        for j in range(len(nodes[i])):
            for k in range(len(nodes[i][j])):
                print(round(nodes[i][j][k],4),' ',end='',file=out)
    print('',file=out)
out.close()

input1.close()