if __name__ == '__main__':
    n=int(input())
    cnt=0
    for _ in range(n):
        s=input()
        stack=[s[0]]
        for i in range(1,len(s)):
            if not stack:
                stack.append(s[i])
            elif stack[-1]==s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack)==0:
            cnt+=1
    print(cnt)
