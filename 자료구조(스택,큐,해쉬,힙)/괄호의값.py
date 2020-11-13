import sys
def check_bracket(s):
    stack=[]
    for x in s:
        if x=='(' or x=='[':
            stack.append(x)
        elif  x==')' and stack:
            if stack[-1]=='(':
                stack.pop()
            else:
                stack.append(x)
        elif x==']' and stack:
            if stack[-1]=='[':
                stack.pop()
            else:
                stack.append(x)
        else:
            stack.append(x)
    if stack:
        return False
    else:
        return True

def solution(s):
    stack=[]
    for x in s:
        if x=='(' or x=='[':
            stack.append(x)
        elif x==')':
            if stack[-1]=='(':
                stack[-1]=2
            else:
                tmp=0
                for i in range(len(stack)-1,-1,-1):
                    if stack[i]=='(':
                        stack[-1]=tmp*2
                        break
                    else:
                        tmp+=stack[i]
                        stack.pop()
        elif x==']':
            if stack[-1]=='[':
                stack[-1]=3
            else:
                tmp=0
                for i in range(len(stack)-1,-1,-1):
                    if stack[i]=='[':
                        stack[-1]=tmp*3
                        break
                    else:
                        tmp+=stack[i]
                        stack.pop()
    return sum(stack)
if __name__ == '__main__':
    s=input()

    if check_bracket(s):
        print(solution(s))
    else:
        print(0)

