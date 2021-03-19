from collections import deque, defaultdict
import math


def find_root(x, root):
    if x == root[x]:
        return x
    else:
        r=find_root(root[x], root)
        root[x]=r
        return r


def union_find(x, y, root):
    x_root=find_root(x, root)
    y_root=find_root(y, root)
    root[y_root]=x_root


def BFS(land, height, check, loc, group, N):
    direction=[(0, -1), (0, 1), (1, 0), (-1, 0)]
    q=deque()
    q.append(loc)
    check[loc[0]][loc[1]]=group

    while q:
        x, y=q.popleft()
        for dx, dy in direction:
            nx, ny=x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or check[nx][ny]: continue
            if abs(land[nx][ny] - land[x][y]) <= height:
                q.append([nx, ny])
                check[nx][ny]=group


def find_ladder(check, land, N):
    direction=[(0, -1), (0, 1), (1, 0), (-1, 0)]
    ladders=defaultdict(lambda: math.inf)

    for i in range(N):
        for j in range(N):
            current=check[i][j]
            for dx, dy in direction:
                nx, ny=i + dx, j + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N or check[nx][ny] == current: continue
                dist=abs(land[i][j] - land[nx][ny])
                ladders[(current, check[nx][ny])]=min(dist, ladders[(current, check[nx][ny])])
    return ladders


def kruskal(ladders, group):
    sum=0
    roots={_: _ for _ in range(1, group)}
    for (x, y), value in ladders:
        if find_root(x, roots) != find_root(y, roots):
            union_find(x, y, roots)
            sum+=value
        if len(roots.items()) == 1: return sum
    return sum


def solution(land, height):
    answer=0
    N=len(land)
    check=[[0 for _ in range(N)] for _ in range(N)]

    group=1
    for i in range(N):
        for j in range(N):
            if not check[i][j]:
                BFS(land, height, check, [i, j], group, N)
                group+=1

    ladders=find_ladder(check, land, N)
    ladders=sorted(ladders.items(), key=lambda x: x[1])

    answer=kruskal(ladders, group)
    return answer