if __name__ == '__main__':
    n,k,d=map(int,input().split())

    box=[list(map(int,input().split()))for _ in range(k)]

    lt=0
    rt=n

    while (lt+1)<rt:
        mid=(lt+rt)//2

        res=0

        for start,end,diff in box:
            if start>mid:
                continue
            res+=((min(end,mid)-start)//diff)+1

        if res>=d:
            rt=mid
        else:
            lt=mid
    print(rt)