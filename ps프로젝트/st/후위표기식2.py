if __name__ == '__main__':
    n=int(input())
    s=input()
    alpha=[0]*26

    for i in range(n):
        alpha[i]=int(input())
    stack=[]
    for x in s:
        if x.isalpha():
            stack.append(alpha[ord(x)-ord('A')])
        else:
            if x=='+':
                num1=stack.pop()
                num2=stack.pop()
                stack.append(round(num1+num2,2))
            elif x=='-':
                num1=stack.pop()
                num2=stack.pop()
                stack.append(round(num2-num1,2))
            elif x=='*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(round(num2*num1,2))
            elif x=='/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(round(num2 /num1,2))
    print("%0.2f"%round(stack[0],2))