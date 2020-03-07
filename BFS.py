#인접행렬의 값이 1이라면 정점간의 간선이 존재한다는 것이고 0이라면 존재하지 않는다는 것이다.
graph={'A':['B'],
       'B':['A','C','H'],
       'C':['B','D','G'],
       'D':['C','E'],
       'E':['D','F'],
       'F':['E'],
       'G':['D'],
       'H':['B','I','J','M'],
       'I':['H'],
       'J':['H','K'],
       'K':['J','L'],
       'L':['K'],
       'M':['H']
       }
def bfs(graph,start_node):
    visit=[]
    queue=[]

    queue.append(start_node)

    while queue:
        node=queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

if __name__=="__main__":
    print(bfs(graph,'A'))