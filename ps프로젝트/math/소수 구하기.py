if __name__ == '__main__':
    m,n=map(int,input().split())

    arr=[True]*(n+1)
    arr[0]=False
    arr[1]=False
    for i in range(n+1):
        if arr[i]:
            for j in range(i*2,n+1,i):
                arr[j]=False

    for i in range(m,n+1):
        if arr[i]:
            print(i)