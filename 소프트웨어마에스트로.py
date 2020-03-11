import collections
import sys

N,K=map(int,input().split())
input_data=list(map(int,input().split()))
visit=[]
cnt=0
for _ in range(N):
    if len(input_data)<2:
        break
    for j in range(0,K):
        if input_data:
            node=input_data.pop(0)
        visit.append(node)
    cnt+=1
    mini=min(visit)
    input_data.append(mini)

print(cnt)
