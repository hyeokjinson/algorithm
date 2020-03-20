class Stack(object):
    def __init__(self):
        self.items=[]
        self.visit=[]
    def push(self,value):
        self.items.append(value)

    def pop(self,value):
        value=self.items.pop()
        if value is not None:
            return value
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)
    def function(self,value):
        result=0
        for i in range(0,len(self.items)):
            if items is not value:
                return True
            else:
                return False

if __name__=="__main__":
    stack=Stack()
    input_data=[]
    stack.push(input_data)
    add_data=[]

    input_data.append(input().split())
    for i in range(0,len(input_data)):
        if function(input_data[0]):
            node=input_data.pop(0)
            stack.push(node)
    


