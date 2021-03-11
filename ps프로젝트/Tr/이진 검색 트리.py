import sys

sys.setrecursionlimit(10**6)

def postorder(start,end):
    if start>end:
        return
    div=end+1
    for i in range(start+1,end+1):
        if post[start]<post[i]:
            div=i
            break
    postorder(start+1,div-1)
    postorder(div,end)
    print(post[start])

if __name__ == '__main__':
    post=[]
    count=0

    while count<=10000:
        try:
            num=int(input())
        except:
            break
        post.append(num)
        count+=1

    postorder(0,len(post)-1)