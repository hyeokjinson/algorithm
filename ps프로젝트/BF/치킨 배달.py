def dfs(L,s):
    global res
    sum_=0
    if L==m:
        for i in range(len(house)):
            x1=house[i][0]
            y1=house[i][1]
            dis=2147000000
            for x in cb:
                x2=chicken[x][0]
                y2=chicken[x][1]
                dis=min(dis,abs(x1-x2)+abs(y1-y2))
            sum_+=dis
        if res>sum_:
            res=sum_
    else:
        for i in range(s,len(chicken)):
            cb[L]=i
            dfs(L+1,i+1)


if __name__ == '__main__':
    n,m=map(int,input().split())

    arr=[list(map(int,input().split()))for _ in range(n)]
    house=[]
    chicken=[]
    cb=[0]*m

    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                house.append((i,j))
            elif arr[i][j]==2:
                chicken.append((i,j))

    res=2147000000
    dfs(0,0)
    print(res)

