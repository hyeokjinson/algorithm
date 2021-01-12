if __name__ == '__main__':
    n=int(input())
    #초기값 설정
    max_H=-1
    max_h_id=-1
    min_L=1001
    max_L=-1
    graph=[]

    for _ in range(n):
        L,H=map(int,input().split())
        graph.append((L,H))
    #최대 높이 y좌표와 x좌표,초기 x좌표값,마지막 x좌표값
        if L<min_L:
            min_L=L
        if L>max_L:
            max_L=L
        if max_H<H:
            max_h_id=L
            max_H=H

    val=[0]*(max_L+1)

    for x,y in graph:
        val[x]=y
    
    res=0
    tmp=0
    for i in range(max_h_id+1):
        if val[i]>tmp:
            tmp=val[i]
        res+=tmp

    tmp=0
    for i in range(max_L,max_h_id,-1):
        if val[i]>tmp:
            tmp=val[i]
        res+=tmp
    print(res)