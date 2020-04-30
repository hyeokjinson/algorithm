import sys
N=int(input())

maze=[list(map(str,input().split())) for i in range(N)]

maze.sort(key=lambda x : (-int(x[1]),int (x[2]),-int(x[3],),x[0]))

for i in maze:
    print(i[0])