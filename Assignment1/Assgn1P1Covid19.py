import numpy as np
import matplotlib.pyplot as plt
a1=np.zeros((100, 50))

rows = np.arange(100)
cols=np.arange(50)
r2=np.random.choice(rows,2)
c2=np.random.choice(cols,2)
a1[r2[0]][c2[0]]=1
a1[r2[1]][c2[1]]=1
t=0
g=[]
g1=[]
sum=0
while sum<5000:  
  row=np.random.choice(rows,8)
  col=np.random.choice(cols,8)
  t1=a1[row[0]][col[0]]
  t2=a1[row[1]][col[1]]
  t3=a1[row[2]][col[2]]
  t4=a1[row[3]][col[3]]
  a1[row[0]][col[0]]=a1[row[4]][col[4]]
  a1[row[1]][col[1]]=a1[row[5]][col[5]]
  a1[row[2]][col[2]]=a1[row[6]][col[6]]
  a1[row[3]][col[3]]=a1[row[7]][col[7]]
  a1[row[4]][col[4]]=t1
  a1[row[5]][col[5]]=t2
  a1[row[6]][col[6]]=t3
  a1[row[7]][col[7]]=t4
  for i in rows:
   for j in cols:
    if(a1[i][j]==1):
      array_1_to_4 = np.arange(start = 1, stop =5)
      v=np.random.choice(a = array_1_to_4, p = [.25,.25,.25,.25])
      if(v==1):
       a1[i][(j-1)%50]=1
      if(v==2):
       a1[(i-1)%100][j]=1
      if(v==3):
       a1[i][(j+1)%50]=1
      if(v==4):
       a1[(i+1)%100][j]=1
      t1=0
      t2=0
      t3=0
      t4=0
  sum=0
    
  for i in rows:
   for j in cols:
    sum=sum+a1[i][j]  
  t=t+1
  g.append(sum)    
  g1.append(t)
plt.plot(g1, g)
plt.xlabel("No of iterations")
plt.ylabel("No of cases")
