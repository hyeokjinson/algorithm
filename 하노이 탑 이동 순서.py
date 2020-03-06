import sys
input=sys.stdin.readline()

move_cnt=0
move_log=[]

def move(x,first,sec,third):
    if x==1:
        move_log.append([first,third])
    else:
        move(x-1,first,third,sec)
        move_log.append([first,third])
        move(x-1,sec,first,third)

move(int(input),1,2,3)
print(len(move_log))
for i,j in move_log:
    print(i,j)
