def inp(a):
    a=abs(a)
    if (a<=1):
        return a
    return inp(a-1)*a

print(inp(3))