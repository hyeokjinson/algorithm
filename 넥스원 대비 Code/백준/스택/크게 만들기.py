if __name__ == '__main__':
    n,k=map(int,input().split())
    numbers=input()
    stack=list()
    for num in numbers:
        while len(stack)>0 and int(stack[-1]) < int(num) and k>0:
            stack.pop()
            k-=1
        stack.append(num)
    print("".join(stack[:n-k]))
    if k:
        print("".join(str(stack[:-k])))
    else:
        print("".join(stack))