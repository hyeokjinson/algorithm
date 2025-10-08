if __name__ == '__main__':
    val=input()
    stack=list()
    res=0
    for idx in range(len(val)):
        if val[idx]=='(':
            stack.append(val[idx])
        elif val[idx]==')':
            if val[idx-1]=='(':
                stack.pop()
                res+=len(stack)
            else:
                stack.pop()
                res+=1
    print(res)