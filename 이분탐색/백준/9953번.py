while True:
    n=int(input())
    lt=0
    rt=100
    cnt=0
    if n==0:
        break
    while lt<=rt:
        mid=(lt+rt)//2
        cnt += 1
        if n==mid:
            break
        else:
            if mid>n:
                rt=mid-1
            else:
                lt=mid+1
    print(cnt)
