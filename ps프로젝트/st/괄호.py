def check(s):
    stack=[]
    for x in s:
        if x=='(':
            stack.append(x)
        else:
            if not stack:
                print('NO')
                return
            else:
                stack.pop()
    if not stack:
        print('YES')
    else:
        print('No')

t=int(input())
for _ in range(t):
    s=input()
    check(s)