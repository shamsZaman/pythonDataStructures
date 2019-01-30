class node:
    def __init__(self, data=None):
        self.data = data
        self.next=None
class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total +=1
            cur = cur.next
        return total
    def display(self):
        element =[]
        cur_node = self.head
        while cur_node.next !=None:
            cur_node = cur_node.next
            element.append(cur_node.data)
        print(element)
    def get(self,index):
        if index >= self.length():
            print("Error")
            return None
        cur_ind=0
        cur_node=self.head
        while True:
            cur_node = cur_node.next
            if (cur_ind -1) == index: return cur_node.data
            cur_ind +=1


my_list = linked_list()
my_list.append(45)
my_list.append("chaha")
my_list.append("piyara")


my_list.display()
print("element at 2nd index: %s" % my_list.get(2))

