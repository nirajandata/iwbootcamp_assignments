def rev(tup):
    return sorted(tup,key=lambda n: n[-1])

print(rev([(2,5),(1,3)]))