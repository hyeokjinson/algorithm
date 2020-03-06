import sys
from _collections import deque

class Deque(object):
    def __init__(self):
        self.input_data=[]
        self.size=0

    def push_front(self,num):
        self.size+=1
        return self.input_data.insert(0,num)
    def push_back(self,num):
        self.size += 1
        return self.input_data.append(num)
    def pop_front(self):
        if self.size==0:
            return -1
        else:
            self.size-=1
            return self.input_data.pop(0)
    def pop_back(self):
        if self.size==0:
            return -1
        else:
            self.size-=1
            return self.input_data.pop(-1)

    def Size(self):
        return self.size
    def empty(self):
        if self.size==0:
            return 1
        else:
            return 0
    def front(self):
        if self.size==0:
            return -1
        else:
            return self.input_data[0]
    def back(self):
        if self.size==0:
            return -1
        else:
            return self.input_data[-1]
n=int(sys.stdin.readline())
d=Deque()
for _ in range(n):
    command=sys.stdin.readline().split()
    if command[0]=="push_front":
        d.push_front(command[1])
    elif command[0]=="push_back":
        d.push_back(command[1])
    elif command[0]=="front":
        sys.stdout.write(str(d.front()))
        sys.stdout.write('\n')
    elif command[0]=="back":
        sys.stdout.write(str(d.back()))
        sys.stdout.write('\n')
    elif command[0]=="size":
        sys.stdout.write(str(d.Size()))
        sys.stdout.write('\n')
    elif command[0]=="empty":
        sys.stdout.write(str(d.empty()))
        sys.stdout.write('\n')
    elif command[0]=="pop_front":
        sys.stdout.write(str(d.pop_front()))
        sys.stdout.write('\n')
    elif command[0]=="pop_back":
        sys.stdout.write(str(d.pop_back()))
        sys.stdout.write('\n')