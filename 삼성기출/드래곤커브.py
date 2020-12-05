if __name__ == '__main__':
    dx=[0,-1,0,1]
    dy=[1,0,-1,0]
    n=int(input())
    map=[[0]*101 for _ in range(101)]

    for i in range(n):
        curve=[]
        x,y,d,g=map(int,input().split())
        curve.append(d)
        map[x][y]=1

        for _ in range(g):
            temp=[]
            for i in range(len(curve)):
                temp.append((curve[-i-1]+1)%4)
            curve.extend(temp)

        for i in curve:
            nx=x+dx[i]
            ny=y+dy[i]
            map[nx][ny]=1
            x,y=nx,ny
    res=0
    for i in range(100):
        for j in range(100):
            if map[i][j] and map[i+1][j] and map[i+1][j+1] and map[i][j+1]:
                res+=1
    print(res)