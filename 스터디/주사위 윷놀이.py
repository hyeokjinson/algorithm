#처음에는 시작 칸에 말 4개가 있다.
#말은 게임판에 그려진 화살표의 방향대로만 이동할 수 있다.
#말이 파란색 칸에서 이동을 시작하면 파란색 화살표만 이동가능
#파란색이 아닌 칸에서 이동을 시작하면 빨간색 화살표만 이동 가능
#말이 도착칸에 도착하면 주사위에 나온 수 관계없이 이동 끝
#게임은 10개의턴,1턴당 1~5적혀있는 주사위 굴림,도착 칸에 있지 않은 말을 하나 골라 주사위에 나온 수 만큼 이동
#말이 이동을 마치는 칸에 다른 말이 있으면 그 말 못고름,단 이동을 마치는 칸이 도착 칸이면 고를 수 있음
#말이 이동을 마칠 때마다 칸에 적혀있는 수 가 점수에 추가
def dfs(L,sum_):
    global res
    if L==10:
        if sum_>=res:
            res=sum_
            return
    else:
        for i in range(4):
            h1,h2,move=horse_location[i],horse_location[i],jusa[L]
            if h1==5 or h1==10 or h1==15:
                h1=change_move[h1]
                move-=1
            if h1+move<=21:
                h1+=move
            else:
                for _ in range(move):
                    h1=map[h1]

            if ch[h1] and h1!=21:
                continue
            ch[h2],ch[h1],horse_location[i]=0,1,h1
            dfs(L+1,sum_+score[h1])
            ch[h2], ch[h1], horse_location[i] = 1, 0, h2
if __name__ == '__main__':
    jusa=list(map(int,input().split()))
    horse_location=[0 for _ in range(4)]
    ch=[0 for _ in range(33)]
    map=[0 for _ in range(33)]
    #외곽
    for i in range(21):
        map[i]=i+1
    map[21]=21
    #10에서 방향변환
    map[22],map[23],map[24]=23,24,30
    #20에서 방향변환
    map[25],map[26]=26,30
    #30에서 방향변환
    map[27],map[28],map[29]=28,29,30
    #25에서 40가는 방향
    map[30],map[31],map[32]=31,32,20
    change_move=[0 for _ in range(16)]
    change_move[5],change_move[10],change_move[15]=22,25,27

    score=[0 for _ in range(33)]
    for i in range(1,21):
        score[i]=i*2
    score[22],score[23],score[24]=13,16,19
    score[25],score[26]=22,24
    score[27],score[28],score[29]=28,27,26
    score[30],score[31],score[32]=25,30,35

    res=-2147000000
    dfs(0,0)
    print(res)