computer=int(input())
network=int(input())
virus_map=[[0 for _ in range(computer+1)] for _ in range(computer+1)]

for _ in range(network):
    x,y=map(int,input().split())
    virus_map[x][y]=1
    virus_map[y][x]=1

def bfs(virus_map,start):
    queue=[start]
    foot_print=[start]
    while queue:
        node=queue.pop(0)
        for i in range(len(virus_map[node])):
            if virus_map[node][i] and i not in foot_print:
                foot_print+=[i]
                queue+=[i]
    return len(foot_print)-1

print(bfs(virus_map,1))
