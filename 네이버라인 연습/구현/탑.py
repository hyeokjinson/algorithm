n=int(input())
top_list=list(map(int,input().split()))
stack=[]
res=[]
for i in range(n):
    while stack:
        if stack[-1][1]>top_list[i]:
            res.append(stack[-1][0]+1)
            break
        stack.pop()
    if not stack:
        res.append(0)

    stack.append((i,top_list[i]))

print(*res)
