if __name__ == '__main__':
    n,m=map(int,input().split())
    matrix=[list(map(str,input()))for _ in range(n)]

    person=0
    col=[0]*n
    row=[0]*m
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]=='X'):
                col[i]=1
                row[j]=1
    cnt1=0;cnt2=0
    for i in range(n):
        if col[i]==0:
            cnt1+=1

    for j in range(m):
        if row[j]==0:
            cnt2+=1

    print(max(cnt1,cnt2))

