import sys

f = open(sys.argv[1],"r")
out= open(sys.argv[2],"w")
content = f.read()
f.close()
data=content.split('\n')

p=int(data[0]) #presentations per time slot
s=int(data[1]) #no. of parallel sessions
t=int(data[2]) #no. of time slots in each session
z=int(data[3]) #trade-off constant
ps=p*t      #number of presentations in per session
# #drop top 4 lines which contain previous info

for i in range(0,4):
    del data[0]
#number of sessions calculated
sc=0
#defining distance matrix with default value as 0
distance=[[0 for x in range(len(data)-1)] for y in range(len(data))]
#print(len(data))
#arranging data in distance matrix
for i in range(0,len(data)-1):
    d=data[i].split(' ')
    #print(d)
   # print(len(d))
    for j in range(0,len(d)):
     #   print(i," ",j)
        distance[i][j]=float(d[j])
#defining and arranging data in similarity matrix
similarity=[[0 for x in range(len(data)-1)] for y in range(len(data))]
'''print("this is distance matrix:")
for i in range(len(distance)):
    print(distance[i])
print("Similarity matrix:")
'''
for i in range(len(distance)):
    temp=[]
    temp=distance[i]
    for j in range(len(temp)):
        if(i!=j):
            similarity[i][j]=round(1-float(temp[j]),1)
'''for i in range(len(similarity)):
    print(similarity[i])
'''
#defining session matrix with sessions with 0 as default presentation
session=[[0 for x in range(ps)] for y in range(s)]


gvalue=0 #goodness vlaue
#------------------------here start the actual work--> code for first session----------------------------

# d is for tracing distance from all parallel sessions
d =[0 for x in range(len(distance[0]))]
#print("---------------------------game Start------------------------------")

#========================================Session 1 =============================================
pc=[0] #number of presentations scheduled
for i in range(1,ps):
    #max=gvalue
    temp1=temp
    for j in range(len(similarity[0])):
        if(j not in pc):
            temp1[j]=round(temp[j]+similarity[0][j],1)
    temp=temp1
    #print(temp)
    loc=None
    '''for j in range(len(temp1)):
        if(temp1[j]>max):
            #print(temp1[j])
            max=temp1[j]
            loc=j
    gvalue=max
    '''
    #maximum= max(temp)
    loc=temp.index(max(temp))
    temp[loc]=0
    #print(loc)
    session[sc][i] = loc
    pc.append(loc)
    #reduce remaining sessions by 1
sc+=1
#------------------------------------------first session is completed----------------------------------------------
#print(session[0])
#***********************************sessions between first and last**************************************
#print(s)
while(sc<s-1):
    d=[0 for x in range(len(distance[0]))]
    #--------------first element of sesson---------------------
    for j in range(p*s*t):
        if j not in pc:
            d[j]=d[j]+distance[session[0][0]][j]
    #print(d)
    loc = None
    loc=d.index(max(d))
    session[sc][0]=loc
    pc.append(loc)
    #print("first element of session: ",sc+1," is :",loc)
    #-----------remaining elements-----------------
    for i in range(1, ps):
        # max=gvalue
        temp=[0 for x in range(len(distance[0]))]
        for j in range(len(similarity[0])):
            if (j not in pc):
                temp[j] = round(temp[j] + similarity[session[sc][0]][j], 1)
        # print(temp)
        loc = None
        '''for j in range(len(temp1)):
            if(temp1[j]>max):
                #print(temp1[j])
                max=temp1[j]
                loc=j
        gvalue=max
        '''
        # maximum= max(temp)
        loc = temp.index(max(temp))
        temp[loc] = 0
        # print(loc)
        session[sc][i] = loc
        pc.append(loc)
    #print("session ",sc+1, "is :",session[sc])
    sc+=1 #increase no of calculated sessions by 1
'''finally end of these middle sessions now just one more loop to getting all the sessions
                        approximately .9 work is done out of 1'''
#---------------------------------END of middle sessions-----------------------------------------

#------------------------Let's deal with last session------------------------------------
j=0
#print(sc)
while(j<len(session[0])):
    for i in range(p*s*t):
        #print(p*s*t)
        if(i not in pc):
            session[sc][j]=i
            j += 1
            pc.append(i)
            break
        # print(session[sc])
        #print(i)
#-------------------End of final session--------------------------------
#arraging presentations in sessions
for i in range(s):
    session[i].sort()

'''till now i just completed half of work 
    beacause i did not deal with time slots yet 
        so let's play with time slots'''

#arraging sessions into time slots and printing them
for i in  range(len(session)):
    m=0
    for j in range(t):
        for k in range(p):
            print(session[i][m]+1,end=' ',file=out)
            #print(k)
            m+=1
        if(j<t-1):
            print("| ",end='',file=out)
    print("",file=out)
out.close()