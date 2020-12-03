if __name__ == '__main__':
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    n,m,x,y,k=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    a_list=list(map(int,input().split()))
    directions=[(2,0,5,3,4,1),(1,5,0,3,4,2),(4,1,2,0,5,3),(3,1,2,5,0,4)]

    dice=[0]*6
    tmp=[0]*6
    for d in a_list:
        d-=1

        x=x+dx[d]
        y=y+dy[d]

        if x<0 or x>=n or y<0 or y>=m:
            x=x-dx[d]
            y=y-dy[d]
            continue
        for idx in range(6):
            tmp[idx]=dice[idx]
        for idx in range(6):
            dice[idx]=tmp[directions[d][idx]]

        if arr[x][y]:
            dice[5]=arr[x][y]
            arr[x][y]=0
        else:
            arr[x][y]=dice[5]
        print(dice[0])

