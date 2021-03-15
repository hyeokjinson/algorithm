def dfs(start):
    ch[start]=False
    dy[start][0]=dis[start]
    dy[start][1]=0
    num[start][0].append(start)
    for i in graph[start]:
        if ch[i]:
            dfs(i)
            dy[start][0]+=dy[i][1]
            dy[start][1]+=max(dy[i][0],dy[i][1])

def trace(cur,pre): # 현재 노드와 이전노드가 포함되었는지 안되었는지
    trace_check[cur]=False

    if pre==0:# 이전노드가 포함되었다면
        for i in graph[cur]:#현재 노드는 포함 할 수 없음
            if trace_check[i]:
                trace(i,1)
    else:#이전 노드가 포함 되어 있지 않다면
        if dy[cur][0]>dy[cur][1]:#현재 노드를 포함한 부분이 더 크다면
            trace_result.append(cur)#현재 노드 포함
            for i in graph[cur]:#다음 노드 포함 안시킴
                if trace_check[i]:
                    trace(i,0)
        else:#현재 노드를 포함하지 않은 부분이 크다면
            for i in graph[cur]:
                if trace_check[i]:
                    trace(i,1)


if __name__ == '__main__':
    n=int(input())
    dis=[0]+list(map(int,input().split()))
    graph=[[] for _ in range(n+1)]
    ch=[True for _ in range(n+1)]
    dy=[[0,0] for _ in range(n+1)]
    num=[[[],[]]for _ in range(n+1)]

    for _ in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)

    trace_result=[]
    trace_check=[True for _ in range(n+1)]

    trace(1,1)
    trace_result.sort()
    print(max(dy[1][1],dy[1][0]))
    print(*trace_result)