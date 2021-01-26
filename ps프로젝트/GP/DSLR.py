from collections import deque

if __name__ == '__main__':
    T=int(input())

    for _ in range(T):
        a,b=map(int,input().split())

        visit=[False]*10000
        cmd=''
        q=deque()
        q.append([a,''])

        v=['D','S','L','R']

        while q:
            x,cmd=q.popleft()

            if x==b:
                break

            if x*2<10000:
                d=x*2
            else:
                d=(x*2)%10000

            if x>0:
                s=x-1
            else:
                s=9999
            l=(x*10)%10000+x//1000
            r=x//10+(x%10)*1000

            temp=[d,s,l,r]

            for i in range(4):
                if not visit[temp[i]]:
                    visit[temp[i]]=True
                    q.append([temp[i],cmd+v[i]])
        print(cmd)

