def convert(x,y,arr):

    for i in range(x,x+3):
        for j in range(y,y+3):
            A[i][j]=1-A[i][j]

if __name__ == '__main__':
    n,m=map(int,input().split())
    A=[list(map(int,input()))for _ in range(n)]
    B=[list(map(int,input()))for _ in range(n)]
    cnt=0
    for i in range(0,n-2):
        for j in range(0,m-2):
            if A[i][j]!=B[i][j]:
                convert(i,j,A)
                cnt+=1
    flag=True
    for i in range(n):
        for j in range(m):
            if A[i][j]!=B[i][j]:
                flag=False
                break
    if not flag:
        print(-1)
    else:
        print(cnt)