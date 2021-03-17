def air_position():
    for i in range(r):
        for j in range(c):
            if arr[i][j]==-1:
                return [i,0],[i+1,0]


def dust_move():
    temp=[[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if arr[i][j]>=5:
                val=0

                if i-1>=0 and arr[i-1][j]!=-1:
                    temp[i-1][j]+=arr[i][j]//5
                    val+=arr[i][j]//5
                if i+1<r and arr[i+1][j]!=-1:
                    temp[i+1][j]+=arr[i][j]//5
                    val+=arr[i][j]//5
                if j-1>=0 and arr[i][j-1]!=-1:
                    temp[i][j-1]+=arr[i][j]//5
                    val+=arr[i][j]//5
                if j+1<c and arr[i][j+1]!=-1:
                    temp[i][j+1]+=arr[i][j]//5
                    val+=arr[i][j]//5
                temp[i][j]-=val

    for i in range(r):
        for j in range(c):
            arr[i][j]+=temp[i][j]

def air_move():
    # 위칸 아래
    temp=arr[up[0]][c-1]
    for i in range(c-1,1,-1):
        arr[up[0]][i]=arr[up[0]][i-1]
    arr[up[0]][1]=0

    #위칸 오른쪽
    temp1=arr[0][c-1]
    for i in range(up[0]-1):
        arr[i][c-1]=arr[i+1][c-1]
    arr[up[0]-1][c-1]=temp

    #위쪽
    temp2=arr[0][0]
    for i in range(c-2):
        arr[0][i]=arr[0][i+1]
    arr[0][c-2]=temp1
    #왼쪽
    for i in range(up[0]-1,1,-1):
        arr[i][0]=arr[i-1][0]
    arr[1][0]=temp2

    #위
    temp=arr[down[0]][c-1]
    for i in range(c-1,1,-1):
        arr[down[0]][i]=arr[down[0]][i-1]
    arr[down[0]][1]=0

    #오른쪽
    temp1=arr[r-1][c-1]
    for i in range(r-1,down[0]+1,-1):
        arr[i][c-1]=arr[i-1][c-1]
    arr[down[0]+1][c-1]=temp

    #아래
    temp2=arr[r-1][0]
    for i in range(c-2):
        arr[r-1][i]=arr[r-1][i+1]
    arr[r-1][c-2]=temp1
    #왼쪽

    for i in range(down[0]+1,r-1):
        arr[i][0]=arr[i+1][0]
    arr[r-2][0]=temp2



if __name__ == '__main__':
    r,c,t=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(r)]

    up,down=air_position()

    for _ in range(t):
        dust_move()
        air_move()
    ans=0
    for i in range(r):
        for j in range(c):
            if arr[i][j]>0:
                ans+=arr[i][j]

    print(ans)