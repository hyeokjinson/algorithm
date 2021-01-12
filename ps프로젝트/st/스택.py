def stacks(s):
    cmd=s.split()[0]

    if len(s.split())>1:
        number=s.split()[1]

    if cmd=='push':
        stack.append(number)
    elif cmd=='top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif cmd=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd=='size':
        print(len(stack))
    elif cmd=='empty':
        if not stack:
            print(1)
        else:
            print(0)


n=int(input())
stack=[]
for _ in range(n):
    stacks(input())