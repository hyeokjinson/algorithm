from _collections import deque

#체스판 말 갯수:k(1번~k번)
#이동방향:위,아래,왼쪽,오른쪽
#흰색인 경우 그 칸으로 이동,이동하는 칸에 말이 있으면 그곳에 스택 쌓기
#빨간색인 경우 이동하고 순서 reverse
#파란색인 경우 말의 이동방향을 역방향 한칸 이동 ,이동칸이 파란색인 경우 이동x
dx=[0,0,-1,1]
dy=[1,-1,0,0]
rev_direction={0:1,1:0,2:3,3:2}
def check():
    for i in range(n):
        for j in range(n):
            if len(start[i][j])>=4:
                return True
    return False

def solve():
    turn=0
    p=0
    while True:
        turn+=1
        if turn>1000:
            return -1
        for number in range(1,k+1):
            x,y,d=horse[number]
            nx,ny=x+dx[d],y+dy[d]

            if nx<0 or nx>=n or ny<0 or ny>=n or arr[nx][ny]==2:
                nd=rev_direction[d]
                nx,ny=x+dx[nd],y+dy[nd]

                if nx<0 or nx>=n or ny<0 or ny>=n or arr[nx][ny]==2:
                    horse[number][2]=nd
                    continue
                p=1
            if arr[nx][ny]==0:
                left=start[x][y][:start[x][y].index(number)]
                right=start[x][y][start[x][y].index(number):]
                start[x][y]=left
                start[nx][ny].extend(right)
                if len(start[nx][ny])>=4:
                    return turn
                for i in right:
                    horse[i][0],horse[i][1]=nx,ny
                if p==1:
                    horse[number][2]=nd
                p=0
            elif arr[nx][ny]==1:
                left = start[x][y][:start[x][y].index(number)]
                right = start[x][y][start[x][y].index(number):]
                start[x][y] = left
                right.reverse()
                start[nx][ny].extend(right)
                if len(start[nx][ny]) >= 4:
                    return turn
                for i in right:
                    horse[i][0], horse[i][1] = nx, ny
                if p == 1:
                    horse[number][2] = nd
                p = 0



if __name__ == '__main__':
    n,k=map(int,input().split())
    #0:흰색,1:빨간색,2:파란색
    arr=[list(map(int,input().split()))for _ in range(n)]
    start=[[[]*n for _ in range(n)] for _ in range(n)]
    horse=dict()
    for i in range(1,k+1):
        x,y,v=map(int,input().split())
        start[x-1][y-1].append(i)
        horse[i]=[x-1,y-1,v-1]
    print(solve())
