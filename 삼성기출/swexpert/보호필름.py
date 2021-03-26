from copy import deepcopy

def check(board):
    ch=[0]*w
    board=list(board.values())
    for i in range(w):
        for j in range(d-k+1):
            column_found=True
            b=board[j][i]
            for K in range(1,k):
                column_found=(column_found and b==board[j+K][i])
            if column_found is True:
                ch[i]=1
                break
        if ch[i]==0:
            return False
    return True

def dfs(last_num,new_board,time):
    global min_time
    global board

    if time>=min_time:
        return
    elif check(new_board):
        min_time=min(min_time,time)
        return
    else:
        for next_row in range(last_num+1,d):
            if time+1<min_time:
                new_board[next_row]=a_type
                dfs(next_row,new_board,time+1)
                new_board[next_row]=b_type
                dfs(next_row,new_board,time+1)
                new_board[next_row]=board[next_row]

if __name__ == '__main__':
    t=int(input())
    for i in range(1,t+1):
        d,w,k=map(int,input().split())
        board={i:list(map(int,input().split()))for i in range(d)}
        a_type=[0 for _ in range(w)]
        b_type=[1for _ in range(w)]

        time=0
        if check(board):
            print("#{} {}".format(i,time))
            continue
        min_time=k

        for row_num in range(d):
            new_board=deepcopy(board)

            new_board[row_num]=a_type
            dfs(row_num,new_board,1)

            new_board[row_num]=b_type
            dfs(row_num,new_board,1)
        print("#{} {}".format(i,min_time))
