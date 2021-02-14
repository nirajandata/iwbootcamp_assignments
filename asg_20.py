l1=['abc','xyz','aba','1231']
a=0
for i in l1:
    if (len(i)>=3) and (i[0]==i[-1]):
        a+=1
print(a)
