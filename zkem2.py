from sys import stdin
from _collections import deque

n=int(stdin.readline())
card_deque=deque(int(i+1) for i in range(n))

while len(card_deque) !=1:
    card_deque.popleft()
    card_deque.rotate(-1)
print(*card_deque)