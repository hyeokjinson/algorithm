def check(a):
    lt=0
    rt=n-1

    while lt<=rt:
        mid=(lt+rt)//2

        if arr[mid]==a:
            return 1
        elif arr[mid]>a:
            rt=mid-1
        else:
            lt=mid+1
    return 0

if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    m=int(input())
    arr1=list(map(int,input().split()))
    res=[]
    for x in arr1:
        res.append(check(x))

    for x in res:
        print(x,end=' ')
