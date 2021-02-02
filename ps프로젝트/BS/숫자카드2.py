from collections import Counter

def check(v):
    lt=0
    rt=n-1
    cnt=0
    while lt<=rt:
        mid=(lt+rt)//2

        if arr[mid]==v:
            return 1
        elif arr[mid]>v:
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
    c=Counter(arr)

    res=[]

    for i in range(m):
        if check(arr1[i]):
            res.append(c[arr1[i]])
        else:
            res.append(0)

    for x in res:
        print(x,end=' ')