import sys

input=sys.stdin.readline
if __name__ == '__main__':
    left=list(input())
    right=[]
    m=int(input())

    for _ in range(m):
        cmd=input()
        if cmd[0]=='L' and left:
            right.append(left.pop())
        elif cmd[0]=='D' and right:
            left.append(right.pop())
        elif cmd[0]=='B' and left:
            left.pop()
        elif cmd[0]=='P':
            left.append(cmd[2])
    print(''.join(left+right[::-1]))