def Count(capacity):
    sum=0
    cnt=1

    for x in arr:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

if __name__ == '__main__':
    n,m=map(int,input().split())
    arr=[]
    for _ in range(n):
        arr.append(int(input()))

    lt=1
    rt=sum(arr)
    max_=max(arr)
    res=0
    while lt<=rt:
        mid=(lt+rt)//2

        if Count(mid)<=m and mid>=max_:
            res=mid
            rt=mid-1
        else:
            lt=mid+1
    print(res)
