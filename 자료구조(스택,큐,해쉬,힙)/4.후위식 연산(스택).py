s=input()
res=0
stack=[]
for x in s:
    if x.isdecimal():
        stack.append(int(x))
    else:
       if x=='+':
           n2=stack.pop()
           n1=stack.pop()
           res=n1+n2
           stack.append(res)
       elif x=='-':
           n2 = stack.pop()
           n1 = stack.pop()
           res = n1 - n2
           stack.append(res)
       elif x=='*':
           n2 = stack.pop()
           n1 = stack.pop()
           res = n1 *n2
           stack.append(res)
       elif x=='/':
           n2 = stack.pop()
           n1 = stack.pop()
           res = n1 / n2
           stack.append(res)
for x in stack:
    print(x)