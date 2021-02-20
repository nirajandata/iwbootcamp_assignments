def inp(text):
    s,l=0,0
    for i in text:
        if i.isupper():
            s+=1
        elif i.islower():
            l+=1
        else:
            pass
    return "upper one is "+str(s)+" and lower one is "+str(l)

print(inp("DFSDdsdskfhjs"))
            