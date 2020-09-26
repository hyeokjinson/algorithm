while True:
    s=input()
    if s=='.':
        break
    stack=[]
    tmp=True
    for x in s[:-1]:
        if x=='(' or x=='[':
            stack.append(x)
        else:
            if x==')':
                if not stack or stack[-1]=='[':
                    tmp=False
                    break
                elif stack[-1]=='(':
                    stack.pop()
            elif x==']':
                if not stack or stack[-1]=='(':
                    tmp=False
                    break
                elif stack[-1]=='[':
                    stack.pop()
    if tmp and not stack:
        print('yes')
    else:
        print('no')