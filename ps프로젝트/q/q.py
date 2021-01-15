class fire:
    def __init__(self):
        self.queue=[]

    def push(self,num):
        self.queue.append(num)
    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.queue:
            return 0
        else:
            return 1

    def front(self):
        if not self.queue:
            return -1
        else:
            return self.queue[0]

    def back(self):
        if not self.queue:
            return -1
        else:
            return self.queue[-1]

if __name__ == '__main__':
    n=int(input())
    test=fire()
    res=[]
    for _ in range(n):
        cmd=input()

        if " " in cmd:
            cmd,num=cmd.split()

        if cmd=='push':
            res.append(test.push(num))
        elif cmd=='pop':
            res.append(test.pop())
        elif cmd=='size':
            res.append(test.size())
        elif cmd=='empty':
            res.append(test.empty())
        elif cmd=='front':
            res.append(test.front())
        elif cmd=='back':
            res.append(test.back())

    for i in res:
        print(i)
