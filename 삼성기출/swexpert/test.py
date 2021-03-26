from copy import deepcopy

def check(board):
    ch=[0]*w
    board=list(board.values())
    for i in range(w):
        for j in range(d-k+1):
            flag=True
            b=board[j][i]

            for K in range(1,k):
                flag=flag and b==board[j+K][i]
            if flag==True:
                ch[i]=1
                break
        if ch[i]==0:
            return False
    return True

def dfs(column_num,new_board,time):
    global min_time

    if time>=min_time:
        return
    elif check(new_board):
        min_time=min(min_time,time)
    else:
        for i in range(column_num+1,d):
            if time+1<min_time:
                new_board[i]=a_board
                dfs(i,new_board,time+1)
                new_board[i]=b_board
                dfs(i,new_board,time+1)
                new_board[i]=board[i]

if __name__ == '__main__':
    t=int(input())

    for idx in range(1,t+1):
        d,w,k=map(int,input().split())
        board={i:list(map(int,input().split()))for i in range(d)}
        min_time=k
        time=0
        a_board=[0for _ in range(w)]
        b_board=[1 for _ in range(w)]


        if check(board):
            print("#{} {}".format(idx,time))
            continue

        for i in range(d):
            new_board=deepcopy(board)

            new_board[i]=a_board
            dfs(i,new_board,1)

            new_board[i]=b_board
            dfs(i,new_board,1)
        print("#{} {}".format(idx,min_time))

