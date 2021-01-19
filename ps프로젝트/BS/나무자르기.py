if __name__ == '__main__':
    n,m=map(int,input().split())

    arr=list(map(int,input().split()))
    arr.sort()
    lt=1
    rt=arr[-1]
    while lt<=rt:

        mid=(lt+rt)//2
        cnt=0
        for i in arr:
            if i>=mid:
                cnt+=i-mid
        if cnt>=m:
            lt=mid+1
        else:
            rt=mid-1
    print(rt)
