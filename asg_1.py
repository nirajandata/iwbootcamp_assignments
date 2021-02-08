def numbs(texts):
    dicts = {}
    for i in texts:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1
    print(dicts)

numbs("hello")