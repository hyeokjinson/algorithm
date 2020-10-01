if __name__ == '__main__':
    n,m=map(int,input().split())
    arr=[list(map(int,input().strip()))for _ in range(n)]
    max_ = -2147000000
    for i in range(n):
        for j in range(m):
            if i>0 and j>0 and arr[i][j]==1:
                arr[i][j]+=min(arr[i-1][j-1],arr[i-1][j],arr[i][j-1])
            max_=max(max_,arr[i][j])

    print(max_*max_)
