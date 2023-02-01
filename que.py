class Queue():
    def __init__(self):
        self.myque = []
        print(self.myque)
    
    def push(self,item):
        self.myque.append(item)
        print(self.myque)
    
    def pop(self):
        print(self.myque.pop())
    
    def isempty(self):
        return len(self.myque) == 0      