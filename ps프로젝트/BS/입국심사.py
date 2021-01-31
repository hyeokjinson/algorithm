def check(x):
    cnt=0

    for i in range(n):
        cnt+=x//arr[i]
    return cnt

if __name__ == '__main__':
    n,m=map(int,input().split())

    arr=[]

    for _ in range(n):
        arr.append(int(input()))

    lt=1
    rt=max(arr)*m

    while lt<=rt:
        mid=(lt+rt)//2

        if check(mid)>=m:
            res=mid
            rt=mid-1
        else:
            lt=mid+1
    print(res)