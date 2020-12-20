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
    n=int(input())
    m=int(input())
    graph=[list(map(int,input().split())) for _ in range(n)]
    parent=[i for i in range(n+1)]
    a=list(map(int,input().split()))

    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                union_parent(parent,i+1,j+1)

    res = 'YES'
    parent_num = 0

    for i in range(len(a)):
        find_parent_num=find_parent(parent,a[i])

        if i==0:
            parent_num=find_parent_num
            continue
        if parent_num!=find_parent(parent,a[i]):
            res='NO'
            break
        parent_num=find_parent_num
    print(res)