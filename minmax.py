def num(n):
    #print(min(n))
    #print(max(n))
    n.sort()

    print(n)
    min=0
    max=0
    for i in range(int(len(n)/2)):
        min=min+n[i]
    print(min)
    for i in range(int(len(n)/2),len(n)):
        max=max+n[i]
    print(max)


num([21,13,16,18,24,67,32,54,89,76])


