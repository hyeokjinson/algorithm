l_s=list(input())
r_s=list()
t=int(input())
for _ in range(t):
    cmd=input()
    if cmd[0]=='L' and l_s:
        r_s.append(l_s.pop())
    elif cmd[0]=='D' and r_s:
        l_s.append(r_s.pop())
    elif cmd[0]=='B' and l_s:
        l_s.pop()
    elif cmd[0]=='P':
        l_s.append(cmd[2])

print(''.join(l_s+r_s[::-1]))