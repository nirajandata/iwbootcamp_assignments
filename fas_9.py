def inp(pr):
    if (pr==1):
        return False
    elif (pr==2):
        return True
    else:
        for x in range(2,pr):
            if(pr%x==0):
                return False
    return True

print(inp(23))