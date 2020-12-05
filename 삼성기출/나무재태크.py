from _collections import deque
import sys
input=sys.stdin.readline
dx=[1,0,-1,0,-1,1,1,-1]
dy=[0,-1,0,1,1,1,-1,-1]


def spring():
    sum_=0
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                dead=deque()
                live=[]

                check[i][j].sort()

                while check[i][j]:
                    year=check[i][j].pop(0)
                    if maps[i][j]<year:
                        dead.append(year)
                    else:
                        maps[i][j]-=year
                        year+=1
                        live.append(year)
                check[i][j].extend(live)

                while dead:
                    year=dead.popleft()
                    maps[i][j]+=(year//2)

def fall():

    for i in range(n):
        for j in range(n):
            tree_age=check[i][j][:]
            for age in tree_age:
                if age%5==0:
                    for d in range(8):
                        nx=i+dx[d]
                        ny=j+dy[d]

                        if 0<=nx<n and 0<=ny<n:
                            check[nx][ny].append(1)

def winter():

    for i in range(n):
        for j in range(n):
            maps[i][j]+=arr[i][j]







if __name__ == '__main__':
    n,m,k=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    maps=[[5]*(n) for _ in range(n)]
    check=[[[]*(n)for _ in range(n)]for _ in range(n)]
    cnt = 0


    for _ in range(m):
        x,y,z=map(int,input().split())
        check[x-1][y-1].append(z)

    for _ in range(k):
        spring()
        fall()
        winter()

    for i in range(n):
        for j in range(n):
            cnt+=len(check[i][j])
    print(cnt)
