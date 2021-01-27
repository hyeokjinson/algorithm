def Count(x):
    ep=arr[0]
    cnt=1
    for i in range(1,n):
        if arr[i]-ep>=x:
            cnt+=1
            ep=arr[i]
    return cnt

if __name__ == '__main__':
    n,c=map(int,input().split())
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    lt=1
    rt=arr[-1]

    while lt<=rt:
        mid=(lt+rt)//2

        if Count(mid)>=c:
            res=mid
            lt=mid+1
        else:
            rt=mid-1

    print(res)