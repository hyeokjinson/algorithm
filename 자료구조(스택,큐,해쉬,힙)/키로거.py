from _collections import deque

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        typing=input()
        left,right=[],[]
        for type in typing:
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
