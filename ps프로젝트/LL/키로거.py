from collections import deque
if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        s=input()
        left,right=[],[]
        for type in s:
            if type=='<':
                if left:
                    right.append(left.pop())

            elif type=='>':
                if right:
                    left.append(right.pop())
            elif type=='-':
                if left:
                    left.pop()
            else:
                left.append(type)
        left.extend(reversed(right))
        print(''.join(left))