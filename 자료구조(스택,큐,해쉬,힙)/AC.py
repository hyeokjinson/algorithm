from _collections import deque


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s=input()
        n=int(input())
        res=input()
        res=res[1:-1]

        if ',' not in res and res!='':
            q=deque([int(res)])
        elif res!='':
            q=deque(map(int,res.split(',')))
        else:
            q=deque()


        flag=1
        cnt=0
        for x in s:
            if x=='R':
                cnt+=1
            else:
                if len(q)==0:
                    flag=0
                    break
                if cnt%2==0:
                    q.popleft()
                else:
                    q.pop()
        if cnt%2==1:
            q.reverse()
        if flag:
            print('[',end='')
            for i in range(len(q)):
                if i==len(q)-1:
                    print(str(q[i]),end='')
                else:
                    print(str(q[i])+',',end='')
            print(']')
        else:
            print('error')
