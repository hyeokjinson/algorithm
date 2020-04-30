import sys

maze=[]
ans=0

maze=[list(map(str,input()))for i in range(8)]

for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            if maze[i][j]=="F":
                ans+=1

print(ans)