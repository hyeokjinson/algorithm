N=int(input())

maze=[]
for _ in range(N):
    count=0
    command=input()
    for t in command:
        if t.isdigit():
            count+=int(t)
    maze.append((command,count))

maze.sort(key=lambda x:(len(x[0]),x[1],x[0]))

for j in maze:
    print(j[0])