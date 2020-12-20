def solution(x,y,d1,d2,n,p):
    area=[0 for _ in range(5)]

    map1=[[0 for _ in range(n)]for _ in range(n)]

    for i in range(d1+1):
        map1[x+i][y-i]=5
        map1[x+d2+i][y+d2-i]=5

    for i in range(d2+1):
        map1[x+i][y+i]=5
        map1[x+d1+i][y-d1+i]=5
    for i in range(d1):
        k=1
        while(map1[x+i+k][y-i]!=5):
            map1[x+i+k][y-i]=5
            k+=1
    for i in range(d2):
        k=1
        while(map1[x+i+k][y+i]!=5):
            map1[x+i+k][y+i]=5
            k+=1

    for i in range(n):
        for j in range(n):

            if i<x+d1 and j<=y and map1[i][j]==0:
                map1[i][j]=1
            elif i<=x+d2 and j>y and map1[i][j]==0:
                map1[i][j]=2
            elif x+d1<=i and j<y-d1+d2 and map1[i][j]==0:
                map1[i][j]=3
            elif i>x+d2 and j>=-d1+d2 and map1[i][j]==0:
                map1[i][j]=4

    for i in range(n):
        for j in range(n):
            area[map1[i][j]-1]+=p[i][j]
    return (max(area)-min(area))

if __name__ == '__main__':
    n=int(input())
    arr=[list(map(int,input().split()))for _ in range(n)]
    ans=-1
    for i in range(n-2):
        for j in range(1,n-1):
            for k in range(1,j+1):
                for s in range(1,n-1-i-k):
                    try:
                        sub=solution(i,j,k,s,n,arr)
                        if ans==-1:
                            ans=sub
                        elif ans>sub:
                            ans=sub
                    except:
                        continue
    print(ans)