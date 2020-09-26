from _collections import deque
sub=input()
n=int(input())
for i in range(n):
    sub2=input()
    dq = deque(sub)
    for x in sub2:
        if x in dq:
            if x!=dq.popleft():
                print("%d No"%(i+1))
                break
    else:
        if len(dq)==0:
            print("%d YES"%(i+1))
        else:
            print("%d No" % (i + 1))

