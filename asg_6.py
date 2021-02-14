def checks(x):
    x1=x.find("not")
    x2=x.find("poor")

    if (x1>x2) and (x2>0):
        x=x.replace(x[-x1],"good")
        print(x)
    else:
        print(x)

checks("the lydhikj is not that poor !")