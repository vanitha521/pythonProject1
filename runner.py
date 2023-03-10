def runner(n,arr):
    a=max(arr)
    #print(a)
    arr.sort(reverse=True)
    #print(arr)
    p=sorted(set(arr),reverse=True)
    print(p[1])



runner(5,[2,3,6,6,5])


