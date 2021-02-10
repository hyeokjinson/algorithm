if __name__ == '__main__':
    n=int(input())

    arr=[]

    for _ in range(n):
        arr.append(int(input()))

    arr.sort()

    lt=0
    rt=n-1
    res=0
    if n==1:
        print(arr[0])
    else:
        while lt<rt:
            if arr[lt]<1 and arr[lt+1]<1:
                res+=(arr[lt]*arr[lt+1])
                lt+=2
            else:
                break
        while rt>0:
            if arr[rt]>1 and arr[rt-1]>1:
                res+=(arr[rt]*arr[rt-1])
                rt-=2
            else:
                break
        res+=sum([arr[i]for i in range(rt,lt-1,-1)])
        print(res)
