
while True:
    n=int(input())
    lt = 1
    rt = 50
    a = []
    if n==0:
        break
    while lt<=rt:
        mid=(lt+rt)//2
        a.append(mid)
        if mid==n:
            for x in a:
                print(x,end=' ')
            print()
            break
        else:
            if mid>n:
                rt=mid-1
            else:
                lt=mid+1