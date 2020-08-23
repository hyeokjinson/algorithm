from _collections import deque
matrix=[list(map(int,input().split()))for _ in range(5)]
moves=list(map(int,input().split()))
result=[]
cnt=0
while moves:
    node=moves.pop(0)
    if len(result)==0:
        result.append(matrix[node-1].pop())
        continue
    print(result)
    if result[-1]==matrix[node-1][-1]:
        result.pop()
        matrix[node-1].pop()
        cnt+=1
    else:
        result.append(matrix[node-1].pop())

print(cnt)