print('第一題')
k=0
while(k>=0):
    y=input('Enter the year(2018):')
    if y=='2018':
        m=['January','Febuary','March','April','May','June','July','August','September','October','November','December']
        w=['Sun','Mon','Tue','Wed','Thr','Fri','Sat']
        d=[31,28,31,30,31,30,31,31,30,31,30,31]
        n=1
        for i in range(12):
            print(m[i])
            for wi in w:
                print(wi,"\t",end="")
            print()
            for _ in range(n):
                print("\t",end="")
            for j in range(1,d[i]+1):
                print(j,"\t",end="")
                n+=1
                if n==7:
                    n=0
                    print()
            print()
        break
    else:
        print('錯誤')
        k+=1
print('第二題')
import numpy as np
import random as r
arrayA=np.zeros([7,5])
for i in range(7):
    for j in range(5):
        arrayA[i][j]=r.random()
print('arrayA的內容:\n',arrayA)
print('arrayA的形狀:',arrayA.shape)
print('arrayA的維度:',arrayA.ndim)
arrayB=arrayA.reshape(35)
print('arrayB的內容:\n',arrayB)
print('arrayB的形狀:',arrayB.shape)
print('arrayB的維度:',arrayB.ndim)
r.shuffle(arrayB)
print('arrayB洗牌後的內容:\n',arrayB)
print('arrayB的最大值:',max(arrayB))
print('arrayB的最小值:',min(arrayB))
print('arrayB的總和:',sum(arrayB))
print('arrayB的平均值:',sum(arrayB)/35)
listA=[]
listA.append(max(arrayB))
listA.append(min(arrayB))
listA.append(sum(arrayB))
listA.append(sum(arrayB)/35)
r.shuffle(arrayB)
listB=[]
listB.append(max(arrayB))
listB.append(min(arrayB))
listB.append(sum(arrayB))
listB.append(sum(arrayB)/35)
listC=[]
for i in range(len(listA)):
    listC.append(listA[i]+listB[i])
print('listC的算術平均數:',sum(listC)/len(listC))
print('第三題')
import pandas as pd
minder=pd.read_csv('gapminder.csv')
print('minder的內容:\n',minder)
print('minder的長度:',minder.size)
print('minder的形狀:',minder.shape)
print('minder的維度:',minder.ndim)
print('minder的前五筆的所有資料:\n',minder.head(5))
print('minder的後五筆所有資料:\n',minder.tail(5))
print('minder的第0列所有資料:\n',minder.iloc[0:1])
print('minder的第4列所有資料:\n',minder.iloc[4:5])
print('minder的第0行所有資料:\n',minder.iloc[:,0])
print('minder的第2行所有資料:\n',minder.iloc[:,2])
print('minder的前30筆之第3行所有資料:\n',minder.iloc[0:30,3])
print('minder的篩選:\n',minder[((minder['country']=='Benin')&(minder['continent']=='Africa')&(minder['year']==1957))|((minder['country']=='Benin')&(minder['continent']=='Africa')&(minder['year']==1972))])
print('minder篩選條件為含有A開頭國家的所有資的:')
c=0
c1=1
for it in minder['country']:
    if it[0]=='A':
        print(minder.iloc[c:c1,:])
    c+=1
    c1+=1