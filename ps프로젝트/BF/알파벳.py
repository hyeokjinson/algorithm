import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(x,y,cnt):
    global res

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<r and 0<=ny<c:
            if ch[ord(arr[nx][ny])-65]==0:
                ch[ord(arr[nx][ny])-65]=1
                dfs(nx,ny,cnt+1)
                ch[ord(arr[nx][ny])-65] = 0
    res=max(res,cnt)



if __name__ == '__main__':
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    r,c=map(int,input().split())
    arr=[list(map(str,input().strip()))for _ in range(r)]
    ch=[0]*26
    res=-2147000000
    ch[ord(arr[0][0])-65]=1
    dfs(0,0,1)
    print(res)