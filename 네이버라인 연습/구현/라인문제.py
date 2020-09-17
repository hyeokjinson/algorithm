from _collections import deque
time=0
c,b=map(int,input().split())
visit=[[0]*2 for _ in range(200001)]
q=deque()
q.append((b,0))

while True:
    c+=time
    if c>200000:
        print(-1)
        break
    if visit[c][time%2]:
        print(time)
        break
    for i in range(len(q)):
        current=q.popleft()
        currentPos=current[0]

        newtime=(current[1]+1)%2
        newPos=currentPos-1
        if newPos>=0 and not visit[newPos][newtime]:
            visit[newPos][newtime]=1
            q.append((newPos,newtime))

        newPos = currentPos+1
        if newPos<200001 and not visit[newPos][newtime]:
            visit[newPos][newtime] = 1
            q.append((newPos, newtime))
        newPos = currentPos * 2
        if newPos < 200001 and not visit[newPos][newtime]:
            visit[newPos][newtime] = 1
            q.append((newPos, newtime))
    time+=1
