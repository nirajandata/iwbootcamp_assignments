def even_num(l1):
    a=len(l1)
    l2=[]
    for i in range(a):
     if(l1[i]%2==0):
      l2.append(l1[i]) 
    return l2
print(even_num([1,2,4,5,6,7,9]))