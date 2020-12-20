def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

if __name__ == '__main__':
    n,q=map(int,input().split())
    graph=[[]*(n+1) for _ in range(n+1)]

    for _ in range(n-1):
        p1,p2,r=map(int,input().split())
        graph[p1].append([r,p2])
        graph[p2].append([r,p1])




    for _ in range(q):
        k,v=map(int,input().split())
        res=0
        parent = [i for i in range(n + 1)]
        for edge in graph[v]:
            cnt,a=edge
            if cnt>=k:
                if find_parent(parent,a)!=find_parent(parent,v):
                    union_parent(parent,a,v)
                    res+=1
        print(res)

