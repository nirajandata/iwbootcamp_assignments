def inp(dict1,key):
    print(dict1)
    del dict1[key]
    return(dict1)

dict1={1:3,5:7}
print(inp(dict1,5))