class node:
    def __init__(self,data=None):
        self.data=data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: Index out of range")
            return None
        cur_indx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_indx == index: return cur_node.data
            cur_indx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: Index out of range")
            return None
        cur_indx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_indx == index:
                last_node.next = cur_node.next
                return
            cur_indx += 1

    def insert_after_value(self, data_after, data_to_insert):
        new_node = node(data_to_insert)
        cur = self.head
        while True:
            if cur.data == data_after:
                if cur.next == None:
                    cur.next = new_node
                    return
                new_node.next = cur.next
                cur.next = new_node
                return
            cur = cur.next

    def remove_by_value(self, value):
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur.data == value:
                last_node.next = cur.next
                return
            



my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.remove_by_value(2)

my_list.display()