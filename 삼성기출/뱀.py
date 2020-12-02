from _collections import deque

if __name__ == '__main__':
    n=int(input())
    k=int(input())
    d=[(0,1),(1,0),(0,-1),(-1,0)]

    arr=[[0]*(n+2) for _ in range(n+2)]

    for i in range(n+2):
        arr[0][i]=1
        arr[i][0]=1
        arr[i][n+1]=1
        arr[n+1][i]=1

    for _ in range(k):
        a,b=map(int,input().split())
        arr[a][b]=2

    L=int(input())
    L_arr=[]
    for _ in range(L):
        x,c=input().split()
        L_arr.append((int(x),c))

    res=0
    x,y=1,1
    now=0
    arr[1][1]=3
    loc=deque([[1,1]])

    while True:

        x=x+d[now][0]
        y=y+d[now][1]

        if arr[x][y]==2:
            arr[x][y]=3
            loc.append([x,y])
            res+=1
        elif arr[x][y]==0:
            arr[x][y]=3
            loc.append([x,y])
            del_x,del_y=loc.popleft()
            arr[del_x][del_y]=0
            res+=1
        else:
            res+=1
            break
        if len(L_arr)!=0:
            if L_arr[0][0]==res:
                if L_arr[0][1]=='L':
                    now=(now+3)%4
                elif L_arr[0][1]=='D':
                    now=(now+1)%4
                del L_arr[0]
    print(res)
