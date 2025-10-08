import heapq

if __name__ == '__main__':
    V,E=map(int,input().split())
    visited=[0 for _ in range(V+1)]
    graph=[list()for _ in range(V+1)]

    for _ in range(E):
        a,b,cost=map(int,input().split())
        graph[a].append((cost,b))
        graph[b].append((a,cost))

    q=[[0,1]]
    result=0
    while q:
        val,node=heapq.heappop(q)

        if not visited[node]:
            result+=val
            visited[node]=1
            for next_val,next_node in graph[node]:
                if not visited[next_node]:
                    heapq.heappush(q,(next_val,next_node))

    print(result)

