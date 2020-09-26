from _collections import deque
import copy
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

#현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    return (direction+1)%8

#현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array,index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0]==index:
                return (i,j)
    return

#모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array,now_x,now_y):
    #1번부터 16번까지의 물고기를 차례대로 (낮은번호부터)확인
    for i in range(1,17):
        #해당 물고기의 위치를 찾기
        position=find_fish(array,i)
        if position:
            x,y=position[0],position[1]
            direction=array[x][y][1]
            #해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx=x+dx[direction]
                ny=y+dy[direction]
                #해당 방향으로이동 가능하면 이동 시키키
                if 0<=nx<4 and 0<=ny<4:
                    if not(nx==now_x and ny==now_y):
                        array[x][y][1]=direction
                        array[x][y],array[nx][ny]=array[nx][ny],array[x][y]
                        break
                direction=turn_left(direction)
#상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array,now_x,now_y):
    positions=[]
    direction=array[now_x][now_y][1]

    for i in range(4):
        #현재 방향으로 계속 이동하기
        now_x+=dx[direction]
        now_y+=dy[direction]
        #범위 벗어나는지 확인
        if 0<=now_x<4 and 0<=now_y<4:
            #물고기가 존재할때
            if array[now_x][now_y][0]!=-1:
                positions.append((now_x,now_y))
    return positions

def dfs(array,now_x,now_y,total):
    global res
    array=copy.deepcopy(array)

    total+=array[now_x][now_y][0] #현재 위치의 물고기 먹기
    array[now_x][now_y][0]=-1 #물고기 먹었으니깐 -1로 바꿈
    move_all_fishes(array,now_x,now_y) #전체 물고기 이동시키기

    #이제 상어가 이동할 차례니깐 이동가능한 위치 찾기
    positions=get_possible_positions(array,now_x,now_y)

    #이동할 위치가 없으면 종료
    if len(positions)==0:
        res=max(res,total)
        return
    for next_x,next_y in positions:
        dfs(array,next_x,next_y,total)


if __name__=="__main__":
    arr=[list(map(int,input().split()))for _ in range(4)]
    map_info=[[0]*4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            map_info[i][j]=[arr[i][j*2],arr[i][j*2+1]-1]

    res=0
    dfs(map_info,0,0,0)
    print(res)