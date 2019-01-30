class queue:
    def __init__(self):
        self.que = []
    def view(self):
        for item in range(len(self.que)):
            print(self.que[item])
    def push(self, item):
        
        self.que.append(item)
    def pop(self):
        
        item = self.que.pop(0)
        print("poped", item)

def main():
    
    a = queue()
    a.push(1)
    a.push(3)
    a.push(5)
    a.view()
    a.pop()
    a.view()

print(main())