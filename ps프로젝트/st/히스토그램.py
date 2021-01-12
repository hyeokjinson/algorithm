if __name__ == '__main__':
    n=int(input())
    graph=[]
    for _ in range(n):
        graph.append(int(input()))
    res=0
    cursor=0
    graph.append(0)
    stack=[(0,graph[0])]

    for i in range(1,n+1):
        cursor=i
        while stack and stack[-1][1]>graph[i]:
            cursor,temp=stack.pop()
            res=max(res,temp*(i-cursor))
        stack.append((cursor,graph[i]))
    print(res)