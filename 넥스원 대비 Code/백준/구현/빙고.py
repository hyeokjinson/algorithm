def col_check():
    cnt=0
    for col in range(5):
        if sum(visit[col])==5:
            cnt+=1
    return cnt

def row_check():
    cnt=0

    for i in range(5):
        sum_ = 0
        for j in range(5):
            if visit[j][i]==1:
                sum_+=1
        if sum_==5:
            cnt+=1
    return cnt
def cross_left():
    cnt=0
    sum_=0
    for idx in range(5):
        sum_+=visit[idx][idx]
    if sum_==5:
        cnt+=1
    return cnt

def cross_right():
    cnt=0
    sum_=0
    for idx in range(5):
        sum_+=visit[idx][4-idx]
    if sum_==5:
        cnt+=1
    return cnt
def bingo(check,res):

    for i in range(5):
        for j in range(5):
            if check==board[i][j]:
                visit[i][j]=1
                cnt1=col_check()
                cnt2=row_check()
                cnt3=cross_left()
                cnt4=cross_right()
                res_cnt=cnt1+cnt2+cnt3+cnt4
                if res_cnt>=3:
                    return res
    return 0

if __name__ == '__main__':

    board=[list(map(int,input().split()))for _ in range(5)]
    game=[list(map(int,input().split()))for _ in range(5)]
    visit=[[False]*5 for _ in range(5)]

    res=0
    answer=0
    for i in range(5):
        if answer:
            break
        for j in range(5):
            res+=1
            check_val=game[i][j]
            answer=bingo(check_val,res)
            if answer:
                print(answer)
                break