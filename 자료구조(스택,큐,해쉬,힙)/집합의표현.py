from _collections import deque

def union_parent(parent,a,b):
    a=find_union(parent,a)
    b=find_union(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b


def find_union(parent,x):
    if parent[x]!=x:
        parent[x]=find_union(parent,parent[x])
    return parent[x]


if __name__ == '__main__':
    n,m=map(int,input().split())

    parent=[0]*(n+1)

    for i in range(n+1):
        parent[i]=i

    for i in range(m):
        r,a,b=map(int,input().split())
        if r==0:
            union_parent(parent,a,b)

        elif r==1:
            if find_union(parent,a)==find_union(parent,b):
                print("YES")
            else:
                print("NO")


