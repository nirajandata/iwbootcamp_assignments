def inp(x):
    a=[]
    for i in x:
        if i not in a:
            a.append(i)
    return a

print(inp(["nirajan","dhakal","nirajan"]))