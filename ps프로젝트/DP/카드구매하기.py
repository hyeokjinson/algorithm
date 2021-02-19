if __name__ == '__main__':
    n=int(input())

    arr=list(map(int,input().split()))
    dy=[0]*(n+1)
    arr.insert(0,0)

    for i in range(1,n+1):
        for j in range(i,n+1):
            dy[j]=max(dy[j],dy[j-i]+arr[i])

    print(dy[n])