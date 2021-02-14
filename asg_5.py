def changes(x):
    a=len(x)
    if(a<3):
        return a
    if (a>=3):
        ch=x[-3:]

        if (ch=="ing"):
            return x+"ly"
        else:
            return x+"ing"         
    
print(changes("string"))