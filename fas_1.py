sr=" is max"
def max(a,b,c):
    if (a>b and a>c):
        return str(a)+sr
    elif (b>a and b>c):
        return str(b)+sr
    else:
        return str(c)+sr

print(max(2,4,5))