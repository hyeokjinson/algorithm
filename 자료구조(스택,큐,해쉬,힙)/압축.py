from _collections import deque

def result(s):
    q=deque()

    for i in range(len(s)):
        if s[i]!=')':
            if s[i]=='(':
                q.append(s[i])
            else:
                q.append(int(s[i]))
        else:
            length=0
            while q:
                value=q.pop()

                if value=='(':
                    break
                else:
                    # print(value)
                    if value>=10:
                        # print("value 초과:",value)
                        length+=value-10
                    else:
                        length+=1

            length=length*q[-1]+10
            q.pop()
            q.append(length)
    res=0
    print(q)
    for i in range(len(q)):
        if q[i]>=10:
            res+=q[i]-10
        else:
            res+=1
    print(res)




if __name__ == '__main__':
    s=input()

    result(s)