def check(budget):
    sum_=0

    for i in arr:
        if i>=budget:
            sum_+=budget
        else:
            sum_+=i
    return sum_

if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    m=int(input())

    arr.sort()
    lt=1
    rt=arr[-1]
    res=0
    while lt<=rt:
        mid=(lt+rt)//2

        if check(mid)<=m:
            res=mid
            lt=mid+1
        else:
            rt=mid-1
    print(res)





