def inp(x):
    occ={}
    x=x.split()
    for i in x:
        if i in occ:
            occ[i]+=1
        else:
            occ[i]=1
    return occ
print(inp("my name is nirajan dhakal"))