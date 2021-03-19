# from collections import deque, defaultdict
# import math
#
#
# def bfs(land, height, check, loc, group, n):
#     dx = [1, 0, -1, 0]
#     dy = [0, -1, 0, 1]
#     q = deque()
#     q.append(loc)
#
#     while q:
#         x, y=q.popleft()
#
#         for i in range(4):
#             nx, ny=x + dx[i], y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0:
#                 if abs(land[nx][ny] - land[x][y]) <= height:
#                     q.append((nx, ny))
#                     check[nx][ny]=group
#
#
# def find_ladder(check, land, n):
#     dx=[1, 0, -1, 0]
#     dy=[0, -1, 0, 1]
#     ladders=defaultdict(lambda: math.inf)
#
#     for i in range(n):
#         for j in range(n):
#             current=check[i][j]
#             for i in range(4):
#                 nx, ny=i + dx[i], j + dy[i]
#                 if 0 <= nx < n and 0 <= ny < n and check[nx][ny] != current:
#                     dist=abs(land[nx][ny] - land[i][j])
#                     ladders[(current, check[nx][ny])]=min(dist, ladders[(current, check[nx][ny])])
#     return ladders
#
#
# def find_root(x, root):
#     if x == root[x]:
#         return x
#     else:
#         r=find_root(root[x], root)
#         root[x]=r
#         return r
#
#
# def union_find(x, y, root):
#     x_root=find_root(x, root)
#     y_root=find_root(y, root)
#     root[y_root]=x_root
#
#
# def kruskal(ladders, group):
#     sum=0
#     roots={_: _ for _ in range(1, group)}
#     for (x, y), value in ladders:
#         if find_root(x, roots) != find_root(y, roots):
#             union_find(x, y, roots)
#             sum+=value
#         if len(roots.items()) == 1: return sum
#     return sum
# def solution(land, height):
#     n = len(land)
#     check = [[0 for _ in range(n)] for _ in range(n)]
#
#     group = 1
#
#     for i in range(n):
#         for j in range(n):
#             if not check[i][j]:
#                 bfs(land, height, check, [i, j], group, n)
#                 group += 1
#
#     ladders = find_ladder(check, land, n)
#     ladders = sorted(ladders.items(), key=lambda x: x[1])
#
#     answer = kruskal(ladders, group)
#
#     return answer
#
# if __name__ == '__main__':
#     print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3))

import heapq


def solution(land, height):
    n=len(land)

    visit=[[0] * n for _ in range(n)]
    q=[]
    heapq.heappush(q, [0, 0, 0])
    visit_cnt=0
    max_count=n * n
    value=0
    dx=[1, 0, -1, 0]
    dy=[0, -1, 0, 1]

    while visit_cnt < max_count:
        v, x, y=heapq.heappop(q)
        if visit[x][y]:
            continue
        visit[x][y]=1
        visit_cnt+=1
        value+=v

        c_height=land[x][y]

        for i in range(4):
            nx=x + dx[i]
            ny=y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                n_height=land[nx][ny]
                if abs(c_height - n_height) > height:
                    heapq.heappush(q, [abs(c_height - n_height), nx, ny])
                else:
                    heapq.heappush(q, [0, nx, ny])

    return value