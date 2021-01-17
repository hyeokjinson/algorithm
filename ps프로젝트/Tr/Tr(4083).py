import sys
input=sys.stdin.readline

def n_v_t(node_n):
    cnt=1
    visited[node_n]=True

    for i in range(len(tree[node_n])):
        next=tree[node_n][i]
        if not visited[next]:
            cnt+=n_v_t(next)
    return cnt

def n_o_e(node_n):
    cnt=len(tree[node_n])
    passed[node_n]=True

    for i in range(len(tree[node_n])):
        next=tree[node_n][i]
        if not passed[next]:
            cnt+=n_o_e(next)
    return cnt

cnt=0
while True:
    cnt += 1
    n,m=map(int,input().split())
    passed=[False]*1002
    visited=[False]*1002
    if n==0 and m==0:
        break
    tree = [[] for _ in range(n + 1)]

    for _ in range(m):
        a,b=map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)

    res=0

    for i in range(1,n+1):
        if not visited[i]:
            v=n_v_t(i)
            e=n_o_e(i)

            if v-1==e/2:
                res+=1
    if res>=2:
        print("Case %d: A forest of %d trees."%(cnt,res))
    elif res==1:
        print("Case %d: Threre is one tree." % cnt)
    elif res==0:
        print("Case %d: No trees."%cnt)

