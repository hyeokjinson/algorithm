from collections import deque
import sys

input=sys.stdin.readline
if __name__ == '__main__':
    n,atk=map(int,input().split())
    lt=0
    rt=10**18
    q=deque()
    for _ in range(n):
        a,b,c=map(int,input().split())
        q.append((a,b,c))


    while (lt+1)<rt:
        mid=(lt+rt)//2

        cur_hp=mid
        cur_atk=atk
        flag=False

        for i in range(n):
            if q[i][0]==1:
                if q[i][2]%cur_atk:
                    cur_hp-=((q[i][2]//cur_atk)*q[i][1])
                else:
                    cur_hp-=(((q[i][2]//cur_atk)-1)*q[i][1])
                if cur_hp<=0:
                    flag=True
                    break
            else:
                cur_atk+=q[i][1]
                cur_hp=min(mid,cur_hp+q[i][2])

        if flag:
            lt=mid
        else:
            rt=mid


    print(rt)