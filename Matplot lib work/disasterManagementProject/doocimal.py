from decimal import *
'''
primitive_name=['Arattupuzha','Paralam','Alapad','Arimbur','Parakkad','Manalur','Venkitangu','Puranattukra','Mullassery','Killannur','Thanikkudam','Pananchery','Cherumkuzhy','Mannamangalam','Muttithadi','Kallur','Varandarapilly','Puthukkad','Nenmanikkara','Thalore','Thekkumkara','Anjur','Velur']
primitive_lat=[10.419211969584994,10.453313928866258,10.442509752384353,10.491800750359669,10.508341861511541,10.486399379602604,10.523531897679728,10.548846961768067,10.537371057165666,10.600820692667064,10.573822450450448,10.56099745304629,10.517793527435932,10.486736968036654,10.457365398163857,10.45398917742028,10.423601540228997,10.423939196947213,10.438458089376343,10.46040396543842,10.629852274963469,10.599521449868867,10.641628150265788  ]
primitive_lon=[76.22118737795664,76.18548181432212,76.15904596432347,76.14943292796035,76.14462640977877,76.1054876188717,76.10377100523542,76.1504628961421,76.08866480523619,76.21912744159312,76.26204278249999,76.31903435522433,76.313197868861,76.34341026885944,76.32418419613316,76.29843499158903,76.31869103249707,76.26341607340902,76.25242974613687,76.25483300522764,76.24825919985203,76.15634266976933,76.16075371982838]
t = open('data2.txt','w')

for i in range(len(primitive_name)):
    t.write(primitive_name[i])
    t.write(' ')
    t.write(str(primitive_lat[i]))
    t.write(' ')
    t.write(str(primitive_lon[i]))
    t.write(' ')
    t.write('\n')
'''


t = open('name_lat_lon.txt','r')
t=t.read()
primitive_name=[]
primitive_lat=[]
primitive_lon=[]

t=str(t)
q=t.split('\n')
#print(q)

for tt in q:
    
    
    #print(tt)
    rr= tt.split()
    if(rr!=[]):

        primitive_name.append(rr[0])
        primitive_lat.append(float(rr[1]))
        primitive_lon.append(float(rr[2]))

import utm
import math
import matplotlib.pyplot as plt
#Encampment- ocoordinates of camps
#Campno - respective camp numbers


citylat = 10.538417938893527
citylong = 76.21270285966565
10.535852147343157, 76.21432132545365
print(len(primitive_name))
print(len(primitive_lat))
print(len(primitive_lon))
t=[]
t1=[]
final=[]
finalco=[]
#x,y,zone,ut =utm.from_latlon(26.84677777777777,80.94627777777777)
#x1,y1,zone,ut = utm.from_latlon(26.84697777777777,80.94697777777777)
for k in range(len(primitive_lat)):
    t.append(primitive_lat[k])
    t.append(primitive_lon[k])
    final.append(t)
    x1,y1,zone,ut = utm.from_latlon(primitive_lat[k],primitive_lon[k])
    t1.append(x1)
    t1.append(y1)
    finalco.append(t1)
    t=[]
    t1=[]
'''
print(x)
print(y)
plt.plot(x,y,'ro')
plt.plot(x1,y1,'ro')
print(math.sqrt((x1-x)*(x1-x)+(y1-y)*(y1-y)))
plt.show()
'''

c=0
for x in finalco:
    plt.plot(x[0],x[1],marker = ".",markersize=20,c='red')
    plt.annotate(primitive_name[c],(x[0],x[1]))
    c=c+1
#plt.show()
cityx,cityy,zone,ut = utm.from_latlon(citylat,citylong)
plt.plot(cityx,cityy,'.',markersize = 20,c='blue')
plt.annotate('Thrissur',(cityx,cityy))

encamp = 5
Encampment=[]

t=[]




encamp=5
for i in range(encamp):
    x=math.cos(math.radians(360/5*i))*5000+cityx
    y=math.sin(math.radians(360/5*i))*5000+cityy
    plt.plot(x,y,'bo',marker="*",markersize=15)
    t.append(x)
    t.append(y)
    Encampment.append(t)
    #print(math.degrees(math.atan2((y-cityy),(x-cityx))))
    t=[]
Campno=[]

c=0
for x in finalco:
    r =(math.degrees(math.atan2((x[1]-cityy),(x[0]-cityx))))
    if(r<0):
        r=360+r 
    r=math.floor(r/(360/encamp))
    #print(r)
    #print(primitive_name[c])
    #print("*")
    Campno.append(r)
    c=c+1

#print(Encampment)
############################FINAL PLOT###########################
plt.show()
c=0
for x in finalco:
    plt.plot(x[0],x[1],marker = ".",markersize=20,c='red')
    plt.annotate(Campno[c],(x[0]+1,x[1]+1),size=15)

    c=c+1
#plt.show()
cityx,cityy,zone,ut = utm.from_latlon(citylat,citylong)
plt.plot(cityx,cityy,'.',markersize = 20,c='blue')
plt.annotate('Thrissur',(cityx,cityy))
c=0

for i in range(encamp):
    x=math.cos(math.radians(360/5*i))*5000+cityx
    y=math.sin(math.radians(360/5*i))*5000+cityy
    plt.plot(x,y,'bo',marker="*",markersize=15)
    plt.annotate(str(i),(x,y),size=15)

plt.show() 

################################################################
campnames=[[] for j in range(encamp)]
camplatlong=[[] for j in range(encamp)]
campcor=[[]for j in range(encamp)]




for i in range(len(Campno)):
    t=Campno[i]
    #print(t)
    
    #print(primitive_name[i])
    campnames[t].append(primitive_name[i])
    camplatlong[t].append(final[i])
    campcor[t].append(finalco[i])
    
    
    #camplatlon[t].append(final[i])
    #campcor[t].append(finalco[i])
   
c=0
for x in finalco:
    plt.plot(x[0],x[1],marker = ".",markersize=20,c='red')
    plt.annotate(Campno[c],(x[0]+1,x[1]+1),size=15)

    c=c+1
#plt.show()
cityx,cityy,zone,ut = utm.from_latlon(citylat,citylong)
plt.plot(cityx,cityy,'.',markersize = 20,c='blue')
plt.annotate('Thrissur',(cityx,cityy))
c=0

for i in range(encamp):
    x=math.cos(math.radians(360/5*i))*5000+cityx
    y=math.sin(math.radians(360/5*i))*5000+cityy
    plt.plot(x,y,'bo',marker="*",markersize=15)
    plt.annotate(str(i),(x,y),size=15)


    
    



def circularsort(new,xnew,ynew):
    import matplotlib.pyplot as plt

   

    t = len(new)
    rr=[]
    l=[]
    e=[]
    d=[]
    a=[]
    for i in range(t):
        
        tx = new[i][0]
        
        ty= new[i][1]
        rr.append(tx)
        rr.append(ty)
        l.append(rr)
        rr=[]
    for rr in l:
        if(rr[1]>0):
            d.append(rr)
        else:
            a.append(rr)
    #print(a[0])
    #print(d)

    for i in range(len(a)):
        for j in range(0,len(a)-1):


            if((a[j][0])<(a[j+1][0])):


                t = a[j]
                a[j]=a[j+1]
                a[j+1]=t
    for i in range(len(d)):
        for j in range(0,len(d)-1):
            if((d[j][0])<(d[j+1][0])):
                t = d[j]
                d[j]=d[j+1]
                d[j+1]=t
    #print(a)
    #print(d)
    a=a+d[::-1]
    #print(a)
    count=0
    tt=xnew,ynew
    for k in a:

        

        #plt.scatter(k[0],k[1],500,marker='*')
        if(count>0):
        
            plt.plot([tt[0],k[0],],[tt[1],k[1]],c='black')
        tt=k
        count=count+1
    k=a[0]
    plt.plot([xnew,k[0],],[ynew,k[1]],c='green',linestyle='dashed')
    k=a[len(a)-1]
    plt.plot([xnew,k[0],],[ynew,k[1]],c='green',linestyle='dashed')
    ttt =[]
    ttt.append(xnew)
    ttt.append(ynew)
    a.append(ttt)
    
    return(a)
f = open("return.txt", "w")






for i in range(encamp):
    print("ENCAMPMENT",end=" ")
    
    print(str(i))
    strr = "ENCAMPMENT"+str(i)
    f.write(strr)
    f.write('\n')
    rrr=[]
    rr=[]
    q=(circularsort(campcor[i],Encampment[i][0],Encampment[i][1]))
    for t in q:
        rx,ry=utm.to_latlon(t[0],t[1],zone,ut)
        rr.append(rx)
        rr.append(ry)
        rrr.append(rr)
        rr=[]
    print(rrr)
    f.write(str(rrr))
    f.write('\n')
    print("******************")
    strr="******************"
    f.write(strr)
    f.write('\n')
    f.write("")
    f.write('\n')
    
'''
#r1x,r1y,zone,ut=utm.from_latlon(10.530282777436431, 76.19870014534766)
r2x,r2y,zone,ut=utm.from_latlon(10.522187543870007, 76.21148690752484)
r3x,r3y,zone,ut=utm.from_latlon(10.57277737711064, 76.2132908018902)
#plt.plot(r1x,r1y,'yo')
plt.plot(r2x,r2y,c='magenta',marker="<",markersize=10)
plt.plot(r3x,r3y,c='magenta', marker="<",markersize=10)
plt.show()
'''
#plt.show()
t = open('resource.txt','r')
r = t.read()
resource_lat=[]
resource_lon=[]
resource_cor=[]
rrr=[]
q=r.split('\n')
for tt in q:
    tt=tt.split(' ')
    resource_lat.append(float(tt[0]))
    resource_lon.append(float(tt[1]))
    resource_x,resource_y,zone,ut=utm.from_latlon(float(tt[0]),float(tt[1]))
    rrr.append(resource_x)
    rrr.append(resource_y)
    resource_cor.append(rrr)
    rrr=[]
print(resource_lat)
print(resource_lon)
plt.show()
for i in range(encamp):
    x=math.cos(math.radians(360/5*i))*5000+cityx
    y=math.sin(math.radians(360/5*i))*5000+cityy
    plt.plot(x,y,'bo',marker="*",markersize=15)
    plt.annotate("Encamp"+str(i),(x,y),size=15)
for i,j in resource_cor:
    plt.plot(i,j,color='magenta',marker='>',markersize=15)
    plt.annotate('Resource Spot',(i,j),size=15)
total=1000000000
c=0
f= open('resourcereturn.txt','w')
#plt.show()
for k in Encampment:
    total=1000000000
    for r in resource_cor:
        t = math.sqrt((k[0]-r[0])*(k[0]-i)+(k[1]-r[1])*(k[1]-r[1]))
        if(total>t):
            total=t
            finalx=r[0]
            finaly=r[1]
    plt.plot([k[0],finalx],[k[1],finaly],color='red')
    print("Encapment ",end='')
    f.write("Encapment ")
    print(str(c))
    f.write(str(c))
    f.write('\n')
    print("Resource Spot")
    f.write("Resource Spot")
    f.write('\n')
    c=c+1
    print(finalx)
    finallat,finallon = utm.to_latlon(finalx,finaly,zone,ut)
    f.write(str(finallat))
    print(finaly)
    f.write(" ")
    f.write(str(finallon))
    f.write('\n')
    print()
plt.show()
plt.show()
c=0
############final plot######################################
'''
for x in finalco:
    plt.plot(x[0],x[1],marker = ".",markersize=20,c='red')
    plt.annotate(Campno[c],(x[0]+1,x[1]+1),size=15)

    c=c+1
#plt.show()
cityx,cityy,zone,ut = utm.from_latlon(citylat,citylong)
plt.plot(cityx,cityy,'.',markersize = 20,c='blue')
plt.annotate('Thrissur',(cityx,cityy))
c=0

for i in range(encamp):
    x=math.cos(math.radians(360/5*i))*5000+cityx
    y=math.sin(math.radians(360/5*i))*5000+cityy
    plt.plot(x,y,'bo',marker="*",markersize=15)
    plt.annotate(str(i),(x,y),size=15)
for k in a:
        #plt.scatter(k[0],k[1],500,marker='*')
        if(count>0):
        
            plt.plot([tt[0],k[0],],[tt[1],k[1]],c='black')
        tt=k
        count=count+1
        k=a[0]
        plt.plot([xnew,k[0],],[ynew,k[1]],c='green',linestyle='dashed')
        k=a[len(a)-1]
        plt.plot([xnew,k[0],],[ynew,k[1]],c='green',linestyle='dashed')
for i,j in resource_cor:

    plt.plot(i,j,color='magenta',marker='>',markersize=15)
    plt.annotate('Resource Spot',(i,j),size=15)
    for k in Encampment:
        total=1000000000
        for r in resource_cor:
            t = math.sqrt((k[0]-r[0])*(k[0]-i)+(k[1]-r[1])*(k[1]-r[1]))
            if(total>t):
                total=t
                finalx=r[0]
                finaly=r[1]
        plt.plot([k[0],finalx],[k[1],finaly],color='red')
plt.show() 
##########################################################
'''