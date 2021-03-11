if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    x=int(input())

    lt=0
    rt=n-1
    count=0
    interval_sum=0
    arr.sort()

    while lt<rt:
        tmp=arr[lt]+arr[rt]

        if tmp==x:
            count+=1
        if tmp<x:
            lt+=1
        else:
            rt-=1
    print(count)
