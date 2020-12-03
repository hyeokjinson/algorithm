if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    b,c=map(int,input().split())
    res=0

    for i in range(n):
        if arr[i]>0:
            arr[i]-=b
            res+=1
        if arr[i]>0:
            res+=arr[i]//c
            if arr[i]%c!=0:
                res+=1
    print(res)
