if __name__ == '__main__':
    n=int(input())
    arr=[int(input())for _ in range(n)]

    res=0
    for i in range(n-1,0,-1):
        if arr[i]<=arr[i-1]:
            res+=arr[i-1]-arr[i]+1
            arr[i-1]=arr[i]-1

    print(res)